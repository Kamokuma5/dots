import os
import shutil
import argparse
import pwd
import getpass
from pathlib import Path

# ANSI color codes
class Color:
    RESET = "\033[0m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    GRAY = "\033[90m"

def correct_ownership_and_permissions(path, uid, gid, mode=None):
    if path.exists() and not path.is_symlink():
        # os.chown(path, uid, gid)
        if mode is not None:
            path.chmod(mode)

def symlink_tree(src_dir, dest_dir, force=False, dry_run=False, label="Symlinked", uid=None, gid=None):
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            src_path = Path(root) / file
            relative_path = src_path.relative_to(src_dir)
            dest_path = dest_dir / relative_path

            dest_path.parent.mkdir(parents=True, exist_ok=True)

            if dest_path.exists() or dest_path.is_symlink():
                if force:
                    if dry_run:
                        print(f"{Color.YELLOW}[Dry Run]{Color.RESET} Would overwrite symlink: {src_path} → {dest_path}")
                    else:
                        dest_path.unlink()
                        print(f"{Color.RED}[Overwritten Symlink]{Color.RESET} {src_path} → {dest_path}")
                else:
                    print(f"{Color.GRAY}[Skipped Symlink]{Color.RESET} {dest_path} already exists")
                    continue

            if dry_run:
                print(f"{Color.YELLOW}[Dry Run]{Color.RESET} Would symlink: {src_path} → {dest_path}")
            else:
                os.symlink(src_path.resolve(), dest_path)
                print(f"{Color.GREEN}[{label}]{Color.RESET} {src_path} → {dest_path}")
                # Ownership not applied to symlinks

def copy_etc(src_dir, dest_dir, force=False, dry_run=False, uid=None, gid=None):
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            src_path = Path(root) / file
            relative_path = src_path.relative_to(src_dir)
            dest_path = dest_dir / relative_path

            dest_path.parent.mkdir(parents=True, exist_ok=True)

            if dest_path.exists():
                if force:
                    if dry_run:
                        print(f"{Color.YELLOW}[Dry Run]{Color.RESET} Would overwrite copy: {src_path} → {dest_path}")
                    else:
                        if dest_path.is_file():
                            dest_path.unlink()
                        print(f"{Color.RED}[Overwritten Copy]{Color.RESET} {src_path} → {dest_path}")
                else:
                    print(f"{Color.GRAY}[Skipped Copy]{Color.RESET} {dest_path} already exists")
                    continue

            if dry_run:
                print(f"{Color.YELLOW}[Dry Run]{Color.RESET} Would copy: {src_path} → {dest_path}")
            else:
                shutil.copy2(src_path, dest_path)
                print(f"{Color.CYAN}[Copied]{Color.RESET} {src_path} → {dest_path}")
                correct_ownership_and_permissions(dest_path, uid, gid, mode=0o644)

def copy_usr(src_dir, dest_dir, force=False, dry_run=False, uid=None, gid=None):
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            src_path = Path(root) / file
            relative_path = src_path.relative_to(src_dir)
            dest_path = dest_dir / relative_path

            dest_path.parent.mkdir(parents=True, exist_ok=True)

            if dest_path.exists():
                if force:
                    if dry_run:
                        print(f"{Color.YELLOW}[Dry Run]{Color.RESET} Would overwrite copy: {src_path} → {dest_path}")
                    else:
                        if dest_path.is_file():
                            dest_path.unlink()
                        print(f"{Color.RED}[Overwritten Copy]{Color.RESET} {src_path} → {dest_path}")
                else:
                    print(f"{Color.GRAY}[Skipped Copy]{Color.RESET} {dest_path} already exists")
                    continue

            if dry_run:
                print(f"{Color.YELLOW}[Dry Run]{Color.RESET} Would copy: {src_path} → {dest_path}")
            else:
                shutil.copy2(src_path, dest_path)
                print(f"{Color.CYAN}[Copied]{Color.RESET} {src_path} → {dest_path}")
                # correct_ownership_and_permissions(dest_path, uid, gid, mode=0o644)

def main():
    parser = argparse.ArgumentParser(description="Deploy dotfiles with symlinks and copies.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    parser.add_argument("--dry-run", action="store_true", help="Preview actions without making changes")
    args = parser.parse_args()

    base_dir = Path(__file__).resolve().parent
    config_src = base_dir / ".config"
    home_src = base_dir / "home"
    etc_src = base_dir / "etc"
    usr_src = base_dir / "usr"

    # Get user from sudo context
    user = os.getenv('SUDO_USER', getpass.getuser())        
    pw_record = pwd.getpwnam(user)
    home_dir = pw_record.pw_dir
    uid = pw_record.pw_uid
    gid = pw_record.pw_gid

    config_dest = Path(home_dir) / ".config"
    home_dest = Path(home_dir)
    etc_dest = Path("/etc")
    usr_dest = Path("/usr")

    print(f"{Color.CYAN}🔗 Deploying .config files...{Color.RESET}")
    symlink_tree(config_src, config_dest, force=args.force, dry_run=args.dry_run, label=".config", uid=uid, gid=gid)

    print(f"{Color.CYAN}🏠 Deploying home files...{Color.RESET}")
    symlink_tree(home_src, home_dest, force=args.force, dry_run=args.dry_run, label="home", uid=uid, gid=gid)

    print(f"{Color.CYAN}📁 Deploying etc files...{Color.RESET}")
    copy_etc(etc_src, etc_dest, force=args.force, dry_run=args.dry_run, uid=uid, gid=gid)

    print(f"{Color.CYAN}📁 Deploying usr files...{Color.RESET}")
    copy_usr(usr_src, usr_dest, force=args.force, dry_run=args.dry_run, uid=uid, gid=gid)

if __name__ == "__main__":
    main()
