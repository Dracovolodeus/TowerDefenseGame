from typing import Literal

import arcade

import config as cfg
from core.images.texture_pool import TexturePool
from core.play.components.enemies.base_enemy import BaseEnemy
from core.play.components.enemies.boss import BossEnemy
from core.play.components.enemies.common import CommonEnemy
from core.play.components.enemies.fast import FastEnemy
from core.play.components.enemies.powerful import PowerfulEnemy
from core.play.components.enemies.regenerating import RegeneratingEnemy


class EnemyManager:
    def __init__(
        self,
        level,
        texture_pool: TexturePool,
        route: list[tuple[int, int]],
        position: tuple[int | float, int | float],
    ) -> None:
        self.__route = route
        self.__level = level
        self.__position = position
        self.__texture_pool = texture_pool
        self.__enemies_list = arcade.SpriteList()

    def update(self, delta_time: float) -> None:
        self.__enemies_list.update()

    def draw(self) -> None:
        self.__enemies_list.draw()

    def add_enemy(
        self,
        enemy_type: Literal["common", "powerful", "fast", "regenerating", "boss"],
        speed: float,
        health: float,
    ) -> None:
        match enemy_type:
            case "common":
                enemy = CommonEnemy(
                    speed=speed,
                    health=health,
                    texture_pool=self.__texture_pool,
                    texture_path=cfg.settings.enemies.common.texture_path,
                    deal_damage_game=self.__level.deal_damage,
                    position=self.__position,
                    route=self.__route.copy(),
                )
            case "powerful":
                enemy = CommonEnemy(
                    speed=speed,
                    health=health,
                    texture_pool=self.__texture_pool,
                    texture_path=cfg.settings.enemies.powerful.texture_path,
                    deal_damage_game=self.__level.deal_damage,
                    position=self.__position,
                    route=self.__route.copy(),
                )
            case "fast":
                enemy = CommonEnemy(
                    speed=speed,
                    health=health,
                    texture_pool=self.__texture_pool,
                    texture_path=cfg.settings.enemies.fast.texture_path,
                    deal_damage_game=self.__level.deal_damage,
                    position=self.__position,
                    route=self.__route.copy(),
                )
            case "regenerating":
                enemy = CommonEnemy(
                    speed=speed,
                    health=health,
                    texture_pool=self.__texture_pool,
                    texture_path=cfg.settings.enemies.regenerating.texture_path,
                    deal_damage_game=self.__level.deal_damage,
                    position=self.__position,
                    route=self.__route.copy(),
                )
            case "boss":
                enemy = CommonEnemy(
                    speed=speed,
                    health=health,
                    texture_pool=self.__texture_pool,
                    texture_path=cfg.settings.enemies.boss.texture_path,
                    deal_damage_game=self.__level.deal_damage,
                    position=self.__position,
                    route=self.__route.copy(),
                )
        self.__enemies_list.append(enemy)

    def get_all_enemies(self) -> arcade.SpriteList[BaseEnemy]:
        return self.__enemies_list
