import decman

USERNAME = 'duck'
config = {
    "USERNAME" : f'{USERNAME}',
    "HOME_DIR" : f'/home/{USERNAME}',
}

import lugia.hardware
from lugia.asus import Asus

from modules.bootloader.limine import Limine
import modules.distro
import modules.de.kde

from modules.de.hyprland import Hyprland
from modules.apps.foot import Foot
from modules.apps.zsh import Zsh
from modules.apps.git import Git
from modules.apps.fastfetch import Fastfetch

decman.modules += [
    Limine(config),
    Asus(config),
    Hyprland(config),
    Foot(config),
    Zsh(config),
    Git(config),
    Fastfetch(config),
]

# Apps
decman.packages += [
    # CLI
    "decman",
    "btop",

    # GUI
    "firefox",
    "ark",
    "btrfs-assistant",
    "octopi",

    "alacritty",
    "neovim",
    "eza",
    "dust",
    "zoxide",
    "fzf",
    "zellij",
    "tmux",
    "yazi",
    "tree",
    "bat",
    "powertop",
    "mullvad-vpn",

    # fonts
    "ttf-cascadia-code-nerd",
]

decman.aur_packages += [
    "lazydocker",

    "vesktop-bin",
    "visual-studio-code-bin",
    "zen-browser-bin",
    "microsoft-edge-stable-bin",
]