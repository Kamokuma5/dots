import decman

decman.packages += [
    # Arch Linux
    "base",
    "base-devel", "texinfo",
    "paru", "pacman-contrib", "rebuild-detector", "reflector",

    # CachyOS
    "cachyos-keyring",
    "linux-cachyos", "wireless-regdb",
    "linux-cachyos-headers",
    "linux-cachyos-nvidia-open",
    "linux-firmware",

    "plymouth",
    "plymouth-kcm",
    "cachyos-plymouth-theme",

    "cachyos-kde-settings",

    "cachyos-hooks",
    "cachyos-settings",
    "cachyos-snapper-support",

    "cachyos-mirrorlist",
    "cachyos-rate-mirrors",
    "cachyos-v3-mirrorlist",
    "cachyos-v4-mirrorlist",
    
    # GUI Apps
    "cachyos-hello",
    "cachyos-kernel-manager",
    "cachyos-packageinstaller",
]