from decman import Module, Directory

class Foot(Module):
    def __init__(self, config):
        super().__init__(name="foot", enabled=True, version="1")
        self.config = config

    def pacman_packages(self) -> list[str]:
        return [
            "foot",
        ]
    
    def directories(self) -> dict[str, Directory]:
        return {
            f"{self.config['HOME_DIR']}/.config/foot/": Directory("./modules/apps/config/foot/")
        }
