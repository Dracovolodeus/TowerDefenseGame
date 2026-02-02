import arcade

import config as cfg
from core.play.components.enemies.wenemy_info import EnemyInfo
from core.play.components.level.tiles import Base, Platform, Portal, Road
from utils.json_func import JSONProcessor


class LevelMap:
    def __init__(self, texture_pool, level_number: int):
        level: dict = JSONProcessor.read(cfg.settings.path.get_level(level_number))
        self.__tiles = arcade.SpriteList()
        self.__base_tile = arcade.SpriteList()
        self.__texture_pool = texture_pool
        self.__path = level["path"]
        self.__enemies_info: list[EnemyInfo] = []
        self.__setup(level["map"], level["enemies"])

    def draw_tiles(self) -> None:
        self.__tiles.draw()

    def draw_base(self) -> None:
        self.__base_tile.draw()

    def get_enemies_info(self) -> list[EnemyInfo]:
        return self.__enemies_info

    def get_path(self) -> list[tuple[int, int]]:
        return self.__path

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
                        self.__tiles.append(Portal(self.__texture_pool, (x, y)))
                    case 4:  # База
                        self.__base_tile.append(Base(self.__texture_pool, (x, y)))
                x += 128
            y -= 128

    def __setup_enemies_settings(self, enemies: list[dict]) -> None:
        for enemy in enemies:
            gain = enemy.get("gain", {})
            speed = gain.get("speed", {})
            health = gain.get("health", {})
            self.__enemies_info.append(EnemyInfo(
                type=enemy["type"],
                frequency=enemy["frequency"],
                health=enemy["start"]["health"],
                gain_speed_step=speed.get("step"),
                gain_speed_value=speed.get("value"),
                gain_speed_count=speed.get("count"),
                gain_health_step=health.get("step"),
                gain_health_value=health.get("value"),
                gain_health_count=health.get("count"),
                )
                                       )

