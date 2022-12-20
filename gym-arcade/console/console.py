from subprocess import call
from pathlib import Path
import retro
import time


class ArcadeConsole:

    """Console for running games. Requires controllers to play."""

    def __init__(self, game_name: str, rom_directory: str = None) -> None:
        """ArcadeConsole initialiser.

        :param game_name: name of game to start console with.
        :param rom_directory: directory to import ROM files from, defaults to None.
        """
        if not rom_directory:
            self._import_roms(Path(rom_directory))
        self.env = retro.make(game=game_name)
        self.env.reset()

    @staticmethod
    def _import_roms(rom_directory: Path) -> None:
        """Import all ROMs from a designated directory. Must be supported by Gym Retro.

        :param rom_directory: directory to import ROM files from
        """
        call(["python", "-m", "retro.import", rom_directory])
