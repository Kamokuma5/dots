from decman import File, Module, Directory

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
    
    def files(self) -> dict[str, File]:
        with open("./modules/de/config/environment.frag", 'r', encoding="utf-8") as frag_file:
            frag = frag_file.readlines()

        # Append new lines into this file
        fname = "/etc/environment"
        with open(fname, 'r') as orig:
            content = orig.readlines()

            for line in frag:
                if line not in content:
                    content.append(line)

            with open(fname, "w", encoding="utf-8") as new:
                new.writelines(content)

        return super().files()