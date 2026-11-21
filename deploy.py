
import os
import shutil
import toml
import argparse
import pwd
import grp

# ANSI color codes
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
RESET = "\033[0m"


def get_original_user():
    """
    Detect the user who invoked the script.

    When running through sudo, SUDO_USER contains
    the original username. Otherwise, use the
    current process user.
    """
    sudo_user = os.environ.get("SUDO_USER")

    if sudo_user:
        return pwd.getpwnam(sudo_user)

    return pwd.getpwuid(os.getuid())


def resolve_path(path, user):
    """
    Resolve deployment paths relative to the original user's
    home directory when they are relative or use ~.
    """
    if path == "~":
        return user.pw_dir

    if path.startswith("~/"):
        return os.path.join(user.pw_dir, path[2:])

    if not os.path.isabs(path):
        return os.path.join(user.pw_dir, path)

    return path


def deploy_entry(
    src_root,
    dest_root,
    method,
    owner=None,
    permissions=None,
    force=False,
    dry_run=False
):
    if not os.path.isdir(src_root):
        print(f"{RED}[Error] Source directory does not exist:{RESET} {src_root}")
        return

    for root, dirs, files in os.walk(src_root):
        rel_path = os.path.relpath(root, src_root)
        target_dir = (
            dest_root if rel_path == "."
            else os.path.join(dest_root, rel_path)
        )

        if not dry_run:
            os.makedirs(target_dir, exist_ok=True)

        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(target_dir, file)

            # Handle existing destination files and symlinks.
            if os.path.lexists(dest_file):
                if not force:
                    print(
                        f"{RED}[Skipped] Destination already exists:{RESET} "
                        f"{dest_file}"
                    )
                    continue

                msg = (
                    f"{MAGENTA}[Dry-Run] Would overwrite:{RESET} "
                    f"{dest_file}"
                    if dry_run else
                    f"{RED}[Overwritten]{RESET} {dest_file}"
                )
                print(msg)

                if not dry_run:
                    if os.path.isdir(dest_file) and not os.path.islink(dest_file):
                        shutil.rmtree(dest_file)
                    else:
                        os.remove(dest_file)

            if method == "symlink":
                msg = (
                    f"{MAGENTA}[Dry-Run] Would symlink:{RESET} "
                    f"{src_file} → {dest_file}"
                    if dry_run else
                    f"{GREEN}[Symlinked]{RESET} "
                    f"{src_file} → {dest_file}"
                )
                print(msg)

                if not dry_run:
                    os.symlink(src_file, dest_file)

            elif method == "copy":
                msg = (
                    f"{MAGENTA}[Dry-Run] Would copy:{RESET} "
                    f"{src_file} → {dest_file}"
                    if dry_run else
                    f"{YELLOW}[Copied]{RESET} "
                    f"{src_file} → {dest_file}"
                )
                print(msg)

                if not dry_run:
                    shutil.copy2(src_file, dest_file)

                    if owner:
                        uid = pwd.getpwnam(owner).pw_uid
                        gid = grp.getgrnam(owner).gr_gid
                        os.chown(dest_file, uid, gid)

                    if permissions:
                        os.chmod(dest_file, int(permissions, 8))

            else:
                print(
                    f"{RED}[Error] Unknown deployment method:{RESET} "
                    f"{method}"
                )
                return


def main():
    parser = argparse.ArgumentParser(
        description="Deploy dotfiles and system configs"
    )

    parser.add_argument(
        "--config",
        default="deploy_config.toml",
        help="Path to TOML config file"
    )

    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview actions without making changes"
    )

    args = parser.parse_args()

    # Detect original user.
    original_user = get_original_user()

    print(
        f"{CYAN}Running as:{RESET} "
        f"{original_user.pw_name}"
    )

    print(
        f"{CYAN}Home directory:{RESET} "
        f"{original_user.pw_dir}"
    )

    # Resolve config path.
    # config_path = resolve_path(args.config, original_user)
    config_path = os.path.abspath(args.config)

    if not os.path.isfile(config_path):
        parser.error(f"Configuration file not found: {config_path}")

    config = toml.load(config_path)

    for entry in config.get("deploy", []):
        src = resolve_path(entry["src"], original_user)
        dest = resolve_path(entry["dest"], original_user)

        method = entry["method"]
        owner = entry.get("owner")
        permissions = entry.get("permissions")

        print(
            f"\n{CYAN}📁 Deploying "
            f"{src} → {dest}...{RESET}"
        )

        deploy_entry(
            src_root=src,
            dest_root=dest,
            method=method,
            owner=owner,
            permissions=permissions,
            force=args.force,
            dry_run=args.dry_run
        )


if __name__ == "__main__":
    main()
