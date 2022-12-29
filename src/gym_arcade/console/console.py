import time
from pathlib import Path
from subprocess import call

import retro


class ArcadeConsole:

    """Console for running games. Requires controllers to play."""

    def __init__(self, game_name: str, rom_directory: Path) -> None:
        """ArcadeConsole initialiser.

        :param game_name: name of game to start console with.
        :param rom_directory: directory to import ROM files from.
        """
        self._import_roms(Path(rom_directory))
        self.env = retro.make(game=game_name)
        self.env.reset()

    @staticmethod
    def _import_roms(rom_directory: Path) -> None:
        """Import all ROMs from a designated directory. Must be supported by Gym Retro.

        :param rom_directory: directory to import ROM files from
        """
        call(["python", "-m", "retro.import", rom_directory])

    def run(self, no_of_games: int = 1) -> None:
        """Run game.

        :param no_of_games: number of games to play.
        """
        done = False
        for game in range(no_of_games):
            while not done:
                if done:
                    obs = self.env.reset()
                self.env.render()
                action = self.env.action_space.sample()
                obs, reward, done, info = self.env.step(action)
                time.sleep(0.01)
        self.env.close()


if __name__ == "__main__":

    from pathlib import Path

    rom_path = Path("roms")

    console = ArcadeConsole("StreetFighterIISpecialChampionEdition-Genesis", rom_path)
    console.run()
