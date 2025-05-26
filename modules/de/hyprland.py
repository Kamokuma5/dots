from decman import Module, Directory

class Hyprland(Module):
    def __init__(self, config):
        super().__init__(name="Hyprland", enabled=True, version="1")
        self.config = config

    def pacman_packages(self) -> list[str]:
        # Packages part of this module
        return [
            "hyprland",
            "brightnessctl",
            "rofi-wayland",
            "hypridle",
            "hyprlock",
        ]
    
    def aur_packages(self) -> list[str]:
        return [
            "hyprshot",
            "ags-hyprpanel-git"
        ]
    
    def directories(self) -> dict[str, Directory]:
        return {
            f"{self.config['HOME_DIR']}/.config/hypr/": Directory("./modules/de/config/hypr/")
        }
