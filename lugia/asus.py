from decman import Module, Directory, File

class Asus(Module):

    def __init__(self, config):
        super().__init__(name="ASUS", enabled=True, version="1")
        self.config = config

    def pacman_packages(self) -> list[str]:
        return [
            "asusctl",
            "power-profiles-daemon",
            "rog-control-center",
            "supergfxctl",
            "switcheroo-control"
        ]
    
    def files(self) -> dict[str, File]:
        return {
            "/etc/supergfxd.conf": File(source_file="./lugia/config/asus/supergfxd.conf"),
        }
    
    def directories(self) -> dict[str, Directory]:
        return {
            "/etc/asusd": Directory("./lugia/config/asus/asusd/")
        }