import arcade

from core.images.texture_pool import TexturePool
from core.play.components.level.map import LevelMap
from core.play.components.turrets.base import Base
from core.play.managers.turret import TurretsManager


class Level(arcade.View):
    def __init__(self, texture_pool: TexturePool, level_number: int) -> None:
        super().__init__()
        self._texture_pool = texture_pool
        self.level_map = LevelMap(texture_pool, level_number)
        self.health = 10
        self.__turrets_manager = TurretsManager(texture_pool)
        self.__turrets_manager.add_turret(Base, (100, 100))

    def on_show_view(self) -> None: ...

    def on_hide_view(self) -> None: ...

    def on_draw(self) -> None:
        self.clear()
        self.level_map.draw_tiles()
        self.__turrets_manager.draw()
        self.level_map.draw_base()

    def on_update(self, delta_time: float) -> bool | None:
        self.__turrets_manager.update(delta_time)

    def deal_damage(self, value: int = 1) -> None:
        self.health -= value if self.health - value >= 0 else self.health
        if self.health == 0:
            print("GAME OFF")  # TODO
