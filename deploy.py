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

def deploy_entry(src_root, dest_root, method, owner=None, permissions=None, force=False, dry_run=False):
    for root, dirs, files in os.walk(src_root):
        rel_path = os.path.relpath(root, src_root)
        target_dir = os.path.join(dest_root, rel_path)

        if not dry_run:
            os.makedirs(target_dir, exist_ok=True)

        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(target_dir, file)

            if method == "symlink":
                if os.path.islink(dest_file) or os.path.exists(dest_file):
                    if force:
                        msg = f"{MAGENTA}[Dry-Run] Would overwrite symlink:{RESET} {src_file} → {dest_file}" if dry_run else f"{RED}[Overwritten Symlink]{RESET} {src_file} → {dest_file}"
                        print(msg)
                        if not dry_run:
                            os.remove(dest_file)
                msg = f"{MAGENTA}[Dry-Run] Would symlink:{RESET} {src_file} → {dest_file}" if dry_run else f"{GREEN}[Symlinked]{RESET} {src_file} → {dest_file}"
                print(msg)
                if not dry_run:
                    os.symlink(src_file, dest_file)

            elif method == "copy":
                if os.path.exists(dest_file):
                    if force:
                        msg = f"{MAGENTA}[Dry-Run] Would overwrite copy:{RESET} {src_file} → {dest_file}" if dry_run else f"{RED}[Overwritten Copy]{RESET} {src_file} → {dest_file}"
                        print(msg)
                        if not dry_run:
                            os.remove(dest_file)
                msg = f"{MAGENTA}[Dry-Run] Would copy:{RESET} {src_file} → {dest_file}" if dry_run else f"{YELLOW}[Copied]{RESET} {src_file} → {dest_file}"
                print(msg)
                if not dry_run:
                    shutil.copy2(src_file, dest_file)
                    if owner and permissions:
                        uid = pwd.getpwnam(owner).pw_uid
                        gid = grp.getgrnam(owner).gr_gid
                        os.chown(dest_file, uid, gid)
                        os.chmod(dest_file, int(permissions, 8))

def main():
    parser = argparse.ArgumentParser(description="Deploy dotfiles and system configs")
    parser.add_argument("--config", default="deploy_config.toml", help="Path to TOML config file")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    parser.add_argument("--dry-run", action="store_true", help="Preview actions without making changes")
    args = parser.parse_args()

    config = toml.load(args.config)

    for entry in config.get("deploy", []):
        src = entry["src"]
        dest = entry["dest"]
        method = entry["method"]
        owner = entry.get("owner")
        permissions = entry.get("permissions")

        print(f"{CYAN}📁 Deploying {src} → {dest}...{RESET}")
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
