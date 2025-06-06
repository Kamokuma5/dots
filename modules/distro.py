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
    "xdg-desktop-portal", "rtkit",

    # standard tools
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
]