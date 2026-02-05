import arcade

import config as cfg
from core.images.texture_pool import TexturePool
from core.play.components.level.map import LevelMap
from core.play.managers.enemy import EnemyManager
from core.play.managers.turret import TurretsManager


class Level(arcade.View):
    def __init__(self, texture_pool: TexturePool, level_number: int) -> None:
        super().__init__()
        self._texture_pool = texture_pool
        self.level_map = LevelMap(texture_pool, level_number)
        self.__turrets_manager = TurretsManager(texture_pool)
        self.__enemy_manager: EnemyManager = EnemyManager(
            level=self,
            texture_pool=self._texture_pool,
            route=self.level_map.get_path(),
            position=self.level_map.get_portal_position(),
        )
        self.__set_wave_gen(need_next=True)
        self.__enemy_manager.add_enemy("common", speed=125, health=1)
        self.health = cfg.settings.level.health

    def on_show_view(self) -> None: ...

    def on_hide_view(self) -> None: ...

    def on_draw(self) -> None:
        self.clear()
        self.level_map.draw_tiles()
        self.__enemy_manager.draw()
        self.__turrets_manager.draw()

    def __spawn_enemies_if_need(self, delta_time: float) -> None:
        if self.__wave_gen_alive:
            self.__wave_gen_alive = self.__wave_gen.send(delta_time)

        elif True:
            self.__set_wave_gen()

    def on_update(self, delta_time: float) -> bool | None:
        self.__spawn_enemies_if_need(delta_time)
        self.__enemy_manager.update(delta_time)
        self.__turrets_manager.update(delta_time)

    def deal_damage(self, value: int = 1) -> None:
        self.health -= value if self.health - value >= 0 else self.health
        if self.health == 0:
            print("GAME OFF")  # TODO

    def __set_wave_gen(self, need_next: bool = True) -> None:
        self.__wave_gen = self.level_map.next_wave(self.__enemy_manager.add_enemy)
        self.__wave_gen_alive = True
        if need_next:
            next(self.__wave_gen)
