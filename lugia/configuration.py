import decman

USERNAME = 'duck'
config = {
    "USERNAME" : f'{USERNAME}',
    "HOME_DIR" : f'/home/{USERNAME}',
}

from modules.limine import Limine
from modules.asus import Asus
import lugia.hardware
import modules.distro
import modules.fonts
import modules.kde

from modules.hyprland import Hyprland
from modules.zsh import Zsh
from modules.git import Git
decman.modules += [
    Limine(config),
    Asus(config),
    Hyprland(config),
    Zsh(config),
    Git(config),
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
    
    "xdg-desktop-portal", "rtkit",


    "alacritty",
    "foot",
    "neovim",
    "eza",
    "dust",
    "zoxide",
    "fzf",
    "zellij",
    "tmux",
    "fastfetch",
    "yazi",
    "tree",
    "bat",
    "powertop",
]

decman.aur_packages += [
    "lazydocker",
    
    "vesktop-bin",
    "visual-studio-code-bin",
    "zen-browser-bin",
    "microsoft-edge-stable-bin",
]