from decman import Module, File, prg

class Limine(Module):

    def __init__(self, config):
        super().__init__(name="limine", enabled=True, version="1")
        self.config = config

    def pacman_packages(self) -> list[str]:
        # Packages part of this module
        return [
            "limine",
            "limine-mkinitcpio-hook", "efibootmgr", "mkinitcpio",
            "snapper",
            "limine-snapper-sync"
        ]
    
    def files(self) -> dict[str, File]:
        return {
            "/etc/default/limine": File(source_file="./modules/bootloader/config/limine/limine", permissions=0o644),
        }
    
    def after_update(self):
        # https://wiki.cachyos.org/configuration/boot_manager_configuration/
        prg(["limine-mkinitcpio"])