from config.enemies import Enemies
from config.level_values import LevelValues
from config.path import Path
from config.research_upgrade import ResearchUpgrade
from config.save import Save
from config.screen import Screen
from config.text import Text
from config.turrets import Turrets


class Settings:
    def __init__(self) -> None:
        self.screen: Screen = Screen()
        self.path: Path = Path()
        self.text: Text = Text()
        self.save: Save = Save(self.path.save)
        self.turrets: Turrets = Turrets(self.save)
        self.enemies: Enemies = Enemies(self.path)
        self.level: LevelValues = LevelValues()
        self.research_upgrade: ResearchUpgrade = ResearchUpgrade()
