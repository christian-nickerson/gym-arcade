from subprocess import call
from pathlib import Path
import retro


class ArcadeConsole:

    """Console for running games. Requires controllers to play."""

    def __init__(self, rom_directory: str) -> None:
        """ArcadeConsole initialiser.

        :param rom_directory: directory to import ROM files from
        """
        self._import_roms(Path(rom_directory))

    @staticmethod
    def _import_roms(rom_directory: Path) -> None:
        """Import all ROMs from a designated directory. Must be supported by Gym Retro.

        :param rom_directory: directory to import ROM files from
        """
        call(["python", "-m", "retro.import", rom_directory])
