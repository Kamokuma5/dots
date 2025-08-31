#!/bin/bash

SYMLINK_NAME="amd-igpu"

# === Check if symlink was created ===
if [ -e "/dev/dri/$SYMLINK_NAME" ]; then
    echo "Using symlinked iGPU: /dev/dri/$SYMLINK_NAME"
    export AQ_DRM_DEVICES="/dev/dri/$SYMLINK_NAME"
else
    echo "Symlink not found. Falling back to available DRM device..."

    # Find first available card
    FALLBACK_CARD=$(ls /dev/dri/ | grep '^card' | head -n 1)
    if [ -n "$FALLBACK_CARD" ]; then
        echo "Fallback to /dev/dri/$FALLBACK_CARD"
        export AQ_DRM_DEVICES="/dev/dri/$FALLBACK_CARD"
    else
        echo "No DRM device found. Hyprland may fail to start."
    fi
fi

# === Optional: Enable verbose logging ===
export HYPRLAND_LOG_WLR=1

# === Launch Hyprland ===
exec Hyprland
