from collections.abc import Generator
import random
from typing import Callable

import arcade

import config as cfg
from core.images.texture_pool import TexturePool
from core.play.components.enemies.enemy_info import EnemyInfo
from core.play.components.level.tiles import Base, Platform, Portal, Road
from utils.json_func import JSONProcessor


class LevelMap:
    def __init__(self, texture_pool: TexturePool, level_number: int, add_level_money: Callable, add_research_money: Callable):
        level: dict = JSONProcessor.read(cfg.settings.path.get_level(level_number))
        self.__wave_schemas: dict[str, dict[str, str | int | float]] = level["waves"][
            "schemas"
        ]
        self.__add_level_money, self.__add_research_money = add_level_money, add_research_money
        self.__money_percent, self.__research_money_percent, = level["money_percent"], level["research_money_percent"]
        self.__money_add_wave, self.__research_add_wave = level["money_add_wave"], level["research_add_wave"]
        self.__wave_path: dict[str, str] = level["waves"]["path"]
        self.__path: list[tuple[int, int]] = level["path"]
        self.__texture_pool = texture_pool
        self.__wave_count: int = 0
        self.__current_wave_index: str = "start"
        self.__enemies_info: list[EnemyInfo] = []
        self.__tiles = arcade.SpriteList()
        self.__platform_tiles = arcade.SpriteList()
        self.__set_next_wave_scheme()
        self.__wave_delta_time = level["delay"]
        self.__setup(level["map"], level["enemies"])

    def draw(self) -> None:
        self.__tiles.draw()
        self.__platform_tiles.draw()

    def get_path(self) -> list[tuple[int, int]]:
        return self.__path

    def get_wave_delta(self) -> float:
        return self.__wave_delta_time

    def get_portal_position(self) -> tuple[float | int, float | int]:
        return self.__portal.center_x, self.__portal.center_y

    def get_current_wave(self) -> int:
        return self.__wave_count

    def get_platform_tiles(self):
        return self.__platform_tiles

    def next_wave(self, add_enemy: Callable) -> Generator[bool, float | None, None]:
        self.__wave_count += 1
        self.__set_next_wave_scheme()
        self.__update_enemies_power()
        for key in sorted(self.__current_wave_scheme):
            value = self.__current_wave_scheme[key]
            enemy_type = value["enemy_type"]
            density: float = value["density"] * 3
            for _ in range(value["enemy_quantity"]):
                density_count = 0
                for enemy in self.__enemies_info:
                    if enemy_type == enemy.type:
                        add_enemy(
                            enemy_type=enemy.type,
                            speed=enemy.speed,
                            health=enemy.health,
                            death_func=self.__enemy_death_func
                        )
                        break
                while density_count < density:
                    delta_time = yield True
                    if not (delta_time is None):
                        density_count += delta_time
        self.__add_level_money(self.__money_add_wave)
        self.__add_research_money(self.__research_add_wave)
        yield False

    def __setup(self, map_: list[list[int]], enemies: list[dict]) -> None:
        self.__setup_map(map_)
        self.__setup_enemies_settings(enemies)

    def __setup_map(self, map_: list[list[int]]) -> None:
        y = cfg.settings.screen.height
        for i in map_:
            x = 128
            for j in i:
                match j:
                    case 1:  # Дорога
                        self.__tiles.append(Road(self.__texture_pool, (x, y)))
                    case 2:  # Платформа
                        self.__platform_tiles.append(
                            Platform(self.__texture_pool, (x, y))
                        )
                    case 3:  # Портал
                        self.__portal = Portal(self.__texture_pool, (x, y))
                        self.__tiles.append(self.__portal)
                    case 4:  # База
                        self.__tiles.append(Base(self.__texture_pool, (x, y)))
                x += 128
            y -= 128

    def __setup_enemies_settings(self, enemies: list[dict]) -> None:
        for enemy in enemies:
            type_ = enemy["type"]
            gain = enemy.get("gain", {})
            speed = gain.get("speed", {})
            health = gain.get("health", {})
            speed_dict = {
                "common": cfg.settings.enemies.common.speed,
                "powerful": cfg.settings.enemies.powerful.speed,
                "fast": cfg.settings.enemies.fast.speed,
                "regenerating": cfg.settings.enemies.regenerating.speed,
                "boss": cfg.settings.enemies.boss.speed,
            }
            self.__enemies_info.append(
                EnemyInfo(
                    type=type_,
                    health=enemy["start"]["health"],
                    speed=speed_dict.get(type_, 0),
                    gain_speed_step=speed.get("step"),
                    gain_speed_value=speed.get("value"),
                    gain_speed_count=speed["count"],
                    gain_health_step=health.get("step"),
                    gain_health_value=health.get("value"),
                    gain_health_count=health["count"],
                )
            )

    def __set_next_wave_scheme(self) -> None:
        self.__current_wave_index = self.__wave_path[self.__current_wave_index]
        self.__current_wave_scheme = self.__wave_schemas[
            self.__wave_path[self.__current_wave_index]
        ]

    def __update_enemies_power(self) -> None:
        for enemy_info in self.__enemies_info:
            # Health
            if (
                not (enemy_info.gain_health_step is None)
                and not (enemy_info.gain_health_count is None)
                and not (enemy_info.gain_health_value is None)
                and self.__wave_count % enemy_info.gain_health_step == 0
                and (
                    self.__wave_count // enemy_info.gain_health_step
                    <= enemy_info.gain_health_count
                    or enemy_info.gain_health_count == -1
                )
            ):
                enemy_info.health += enemy_info.gain_health_value

            # Speed
            if (
                not (enemy_info.gain_speed_step is None)
                and not (enemy_info.gain_speed_count is None)
                and not (enemy_info.gain_speed_value is None)
                and self.__wave_count % enemy_info.gain_speed_step == 0
                and (
                    self.__wave_count // enemy_info.gain_speed_step
                    <= enemy_info.gain_speed_count
                    or enemy_info.gain_speed_count == -1
                )
            ):
                enemy_info.speed += enemy_info.gain_speed_value

    def __enemy_death_func(self) -> None:
        if random.random() >= self.__money_percent:
            self.__add_level_money(1)
        if random.random() >= self.__research_money_percent:
            self.__add_research_money(1)

