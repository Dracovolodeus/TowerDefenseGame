from collections.abc import Generator
from typing import Callable

import arcade

import config as cfg
from core.images.texture_pool import TexturePool
from core.play.components.enemies.enemy_info import EnemyInfo
from core.play.components.level.tiles import Base, Platform, Portal, Road
from utils.json_func import JSONProcessor


class LevelMap:
    def __init__(self, texture_pool: TexturePool, level_number: int):
        level: dict = JSONProcessor.read(cfg.settings.path.get_level(level_number))
        self.__wave_schemas: dict[str, dict[str, str | int | float]] = level["waves"][
            "schemas"
        ]
        self.__wave_path: dict[str, str] = level["waves"]["path"]
        self.__path: list[tuple[int, int]] = level["path"]
        self.__texture_pool = texture_pool
        self.__wave_count: int = 0
        self.__current_wave_index: str = "start"
        self.__enemies_info: list[EnemyInfo] = []
        self.__tiles = arcade.SpriteList()
        self.__set_next_wave_scheme()
        self.__setup(level["map"], level["enemies"])

    def draw_tiles(self) -> None:
        self.__tiles.draw()

    def get_path(self) -> list[tuple[int, int]]:
        return self.__path

    def get_portal_position(self) -> tuple[float | int, float | int]:
        return self.__portal.center_x, self.__portal.center_y

    def get_current_wave(self) -> int:
        return self.__wave_count

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
                        )
                        break
                while density_count < density:
                    delta_time = yield True
                    if not (delta_time is None):
                        density_count += delta_time
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
                        self.__tiles.append(Platform(self.__texture_pool, (x, y)))
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
                    frequency=enemy["frequency"],
                    health=enemy["start"]["health"],
                    speed=speed_dict.get(type_, 0),
                    gain_speed_step=speed.get("step"),
                    gain_speed_value=speed.get("value"),
                    gain_speed_count=speed.get("count"),
                    gain_health_step=health.get("step"),
                    gain_health_value=health.get("value"),
                    gain_health_count=health.get("count"),
                )
            )

    def __set_next_wave_scheme(self) -> None:
        self.__current_wave_index = self.__wave_path[self.__current_wave_index]
        self.__current_wave_scheme = self.__wave_schemas[
            self.__wave_path[self.__current_wave_index]
        ]

    def __update_enemies_power(self) -> None: ... #TODO
