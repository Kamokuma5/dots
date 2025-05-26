import decman

# DM
decman.packages += [
    # Note: Disable current DM and run: 
    # sudo systemctl enable ly.service
    # sudo systemctl start ly.service
    "ly"
]

# CPU
decman.packages += [
    "amd-ucode"
]

# Sound
decman.packages += [
    "pipewire-alsa",
    "pipewire-pulse",
    "rtkit",
    "wireplumber",
    "pavucontrol",
    "alsa-firmware",
    "alsa-plugins",
    "alsa-utils",
    "sof-firmware"
]

# Graphics
decman.packages += [
    # iGPU
    "mesa-utils",
    "lib32-mesa",
    "vulkan-radeon",
    "lib32-vulkan-radeon",

    # dGPU
    "nvidia-prime",
    "nvidia-settings",
    "nvidia-utils", "egl-wayland",
    "lib32-nvidia-utils",
    "lib32-opencl-nvidia",
    "libva-nvidia-driver",
    "opencl-nvidia",
]

# Networking
decman.packages += [
    "ufw", "iptables-nft",
    "networkmanager",
    "iwd",
    "wpa_supplicant",
    "bluez",
    "bluez-hid2hci",
    "bluez-libs",
    "bluez-utils",
]