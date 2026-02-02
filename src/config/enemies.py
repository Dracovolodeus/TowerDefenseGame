from dataclasses import dataclass
from pathlib import Path

from config.path import Path as ConfigPath


@dataclass
class Common:
    texture_path: Path
    speed: float = 50


@dataclass
class Powerful:
    texture_path: Path
    speed: float = 50


@dataclass
class Regenerating:
    texture_path: Path
    speed: float = 50


@dataclass
class Fast:
    texture_path: Path
    speed: float = 50
    dodge_probability: float = 0.05


@dataclass
class Boss:
    texture_path: Path
    speed: float = 50
    impenetrability_probability: float = 0.1
    part_penetration_probability: float = 0.25


class Enemies:
    def __init__(self, path: ConfigPath) -> None:
        self.path = path
        self.restart()

    def restart(self) -> None:
        self.common = Common(self.path.common)
        self.powerful = Powerful(self.path.powerful)
        self.fast = Fast(self.path.fast)
        self.regenerating = Regenerating(self.path.regenerating)
        self.boss = Boss(self.path.boss)
