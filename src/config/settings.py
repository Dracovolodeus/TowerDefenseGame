from config.enemies import Enemies
from config.level_values import LevelValues
from config.path import Path
from config.save import Save
from config.screen import Screen
from config.text import Text


class Settings:
    def __init__(self) -> None:
        self.screen: Screen = Screen()
        self.path: Path = Path()
        self.text: Text = Text()
        self.enemies: Enemies = Enemies(self.path)
        self.save: Save = Save(self.path.save)
        self.level: LevelValues = LevelValues()
