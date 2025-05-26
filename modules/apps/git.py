from decman import Module, Directory

class Git(Module):
    def __init__(self, config):
        super().__init__(name="git", enabled=True, version="1")
        self.config = config

    def pacman_packages(self) -> list[str]:
        # Packages part of this module
        return [
            "git",
            "git-delta"
        ]
    
    def directories(self) -> dict[str, Directory]:
        return {
            f"{self.config['HOME_DIR']}/.config/git/": Directory("./modules/apps/config/git/")
        }
