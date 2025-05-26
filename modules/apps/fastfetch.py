from decman import Module, Directory

class Fastfetch(Module):
    def __init__(self, config):
        super().__init__(name="fastfetch", enabled=True, version="1")
        self.config = config

    def pacman_packages(self) -> list[str]:
        return [
            "fastfetch", "imagemagick"
        ]
    
    def directories(self) -> dict[str, Directory]:
        return {
            f"{self.config['HOME_DIR']}/.config/fastfetch/": Directory("./modules/apps/config/fastfetch/")
        }
