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
        self.root = PathLibPath(".")

        self.program_data = PathLibPath("../.program_data")
        self.save = self.program_data / "save.json"

        self.__assets = self.root / "assets"
        self.__images = self.__assets / "images"
        self.__turrets = self.__images / "turrets"
        self.__backagraunds = self.__images / "backgrounds"
        self.start_menu = self.__backagraunds / "start_menu.png"

    def get_turret(self, turtype: Literal["base", "sniper"]) -> Turret:
        return Turret(
            base=self.__turrets / turtype / "base.png",
            bullet=self.__turrets / turtype / "bullet.png",
            tower=self.__turrets / turtype / "tower.png",
        )
