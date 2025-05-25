from decman import Module, File

# Note: May need to run `chsh -s /usr/bin/zsh` outside of root
class Zsh(Module):

    def __init__(self, config):
        super().__init__(name="zsh", enabled=True, version="1")
        self.config = config

    def pacman_packages(self) -> list[str]:
        # Packages part of this module
        return [
            "cachyos-zsh-config",
            "vim", # dependency for cachyos-zsh-config
        ]
    
    def files(self) -> dict[str, File]:
        return {
            f"{self.config['HOME_DIR']}/.zshrc": File(source_file="./modules/dots/zsh/.zshrc"),
            f"{self.config['HOME_DIR']}/.config/zsh/.p10k.zsh": File(source_file="./modules/dots/zsh/.p10k.zsh"),
        }