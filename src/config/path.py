from dataclasses import dataclass
from pathlib import Path as PathLibPath
from typing import Literal


@dataclass
class Turret:
    base: PathLibPath
    bullet: PathLibPath
    tower: PathLibPath


class Path:
    def __init__(self) -> None:

        # Base
        self.program_data = PathLibPath("../.program_data")
        self.save = self.program_data / "save.json"

        # Assets
        self.root = PathLibPath(".")
        self.__assets = self.root / "assets"

        # Images
        self.__images = self.__assets / "images"
        self.__turrets = self.__images / "turrets"

        # Backgrounds
        self.__backagraunds = self.__images / "backgrounds"
        self.start_menu = self.__backagraunds / "start_menu.png"

        # Tiles
        self.__tiles = self.__images / "tiles"
        self.road = self.__tiles / "road.png"
        self.platform = self.__tiles / "platform.png"
        self.portal = self.__tiles / "portal.png"
        self.base = self.__tiles / "base.png"

        # Maps
        self.__maps = self.__assets / "maps"

    def get_turret(self, turtype: Literal["base", "sniper"]) -> Turret:
        return Turret(
            base=self.__turrets / turtype / "base.png",
            bullet=self.__turrets / turtype / "bullet.png",
            tower=self.__turrets / turtype / "tower.png",
        )

    def get_level(self, level_number: int) -> PathLibPath:
        return self.__maps / f"{level_number}.json"

