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

        # UI
        self.__ui = self.__images / "ui"
        self.damage = self.__ui / "damage.png"
        self.length = self.__ui / "length.png"
        self.speed = self.__ui / "speed.png"

        # Turrets
        self.__turrets = self.__images / "turrets"

        # Backgrounds
        self.__backgrounds = self.__images / "backgrounds"
        self.start_menu = self.__backgrounds / "start_menu.png"
        self.research_menu = self.__backgrounds / "research_menu.png"
        self.select_level_menu = self.__backgrounds / "select_level_menu.png"
        self.tower_menu = self.__backgrounds / "towers_choose_back.png"

        # Tiles
        self.__tiles = self.__images / "tiles"
        self.road = self.__tiles / "road.png"
        self.platform = self.__tiles / "platform.png"
        self.portal = self.__tiles / "portal.png"
        self.base = self.__tiles / "base.png"

        # Enemies
        self.__enemies = self.__images / "enemies"
        self.common = self.__enemies / "common.png"
        self.powerful = self.__enemies / "powerful.png"
        self.regenerating = self.__enemies / "regenerating.png"
        self.fast = self.__enemies / "fast.png"
        self.boss = self.__enemies / "boss.png"

        # Maps
        self.__maps = self.__assets / "maps"

    def get_turret(
        self, turtype: Literal["base", "sniper", "multishoot", "shotgun", "venom"]
    ) -> Turret:
        return Turret(
            base=self.__turrets / turtype / "base.png",
            bullet=self.__turrets / turtype / "bullet.png",
            tower=self.__turrets / turtype / "tower.png",
        )

    def get_level(self, level_number: int) -> PathLibPath:
        return self.__maps / f"{level_number}.json"
