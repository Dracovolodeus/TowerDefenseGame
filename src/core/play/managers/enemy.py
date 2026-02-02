from typing import Literal

import arcade

import config as cfg
from core.images.texture_pool import TexturePool
from core.play.components.enemies.boss import BossEnemy
from core.play.components.enemies.common import CommonEnemy
from core.play.components.enemies.fast import FastEnemy
from core.play.components.enemies.powerful import PowerfulEnemy
from core.play.components.enemies.regenerating import RegeneratingEnemy
from core.play.views.level import Level


class EnemyManager:
    def __init__(
        self,
        level: Level,
        texture_pool: TexturePool,
        route: list[tuple[int, int]],
        position: tuple[int, int],
    ) -> None:
        self.__route = route
        self.__level = level
        self.__position = position
        self.__texture_pool = texture_pool
        self.__enemies_list = arcade.SpriteList()

    def update(self) -> None:
        self.__enemies_list.update()

    def draw(self) -> None:
        self.__enemies_list.draw()

    def add_enemy(
        self, enemy_type: Literal["common", "powerfull", "fast", "regenerating", "boss"]
    ) -> None:
        match enemy_type:
            case "common":
                enemy = CommonEnemy(
                    speed=cfg.settings.enemies.common.speed,
                    health=cfg.settings.enemies.common.health,
                    texture_pool=self.__texture_pool,
                    texture_path=cfg.settings.enemies.common.texture_path,
                    deal_damage_game=self.__level.deal_damage,
                    position=self.__position,
                    route=self.__route,
                )
            case "powerfull":
                ...
            case "fast":
                ...
            case "regenerating":
                ...
            case "boss":
                ...
