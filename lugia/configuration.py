import decman

USERNAME = 'duck'
config = {
    "USERNAME" : f'{USERNAME}',
    "HOME_DIR" : f'/home/{USERNAME}',
}

from modules.limine import Limine
import lugia.hardware
import modules.distro
import modules.fonts
import modules.kde

from modules.hyprland import Hyprland
from modules.zsh import Zsh
from modules.git import Git
decman.modules += [
    Limine(config),
    Hyprland(config),
    Git(config),
    Zsh(config),
]

# Apps
decman.packages += [
    # System Dependencies
    "perl",
    "cryptsetup",
    "device-mapper",
    "diffutils",
    "e2fsprogs", "lvm2",
    "rsync",
    "ripgrep",
    "mdadm",
    "upower", 
    "xf86-input-libinput",

    # CLI
    "decman",
    "neovim",
    "btop",
    "wget",
    "which",
    "sudo",
    "openssh",
    "btrfs-progs",
    "hwinfo",
    "inetutils",
    "unzip",
    "unrar",
    "chwd",
    "chrony",
    "bind",
    "ethtool",
    "python", "python-defusedxml","python-packaging",

    # GUI
    "firefox",
    "ark",
    "btrfs-assistant",
    "octopi",
    "alacritty",

    "xdg-desktop-portal", "rtkit"
]

decman.aur_packages += [
    "visual-studio-code-bin",
]