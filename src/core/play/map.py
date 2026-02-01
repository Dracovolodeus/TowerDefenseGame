import arcade
from utils.json_func import JSONProcessor
import config as cfg


class LevelMap:
    def __init__(self, texture_pool, level_number: int):
        level: dict = JSONProcessor.read(cfg.settings.path.get_level(level_number))
        self._texture_pool = texture_pool

        self.complexity = level['complexity']
        self.path = level['path']
        self.enemies = level['enemies']
        self.map_: list[list[int]] = level['map'][::-1]
        self.map_size = [len(self.map_[0]), len(self.map_)]
        self.elements = []
        y = 0
        for i in self.map_:
            x = 0
            for j in i:
                match j:
                    case 1: # Дорога
                        self.elements.append(
                                {
                                    "texture": self._texture_pool.get_texture(
                                        cfg.settings.path.road
                                        ),
                                    "rect": arcade.rect.XYWH(x, y, 128, 128),
                                    }
                                )
                    case 2: # Платформа
                        self.elements.append(
                                {
                                    "texture": self._texture_pool.get_texture(
                                        cfg.settings.path.platform
                                        ),
                                    "rect": arcade.rect.XYWH(x, y, 128, 128),
                                    }
                                )
                    case 3: # Портал
                        self.elements.append(
                                {
                                    "texture": self._texture_pool.get_texture(
                                        cfg.settings.path.portal
                                        ),
                                    "rect": arcade.rect.XYWH(x, y, 128, 128),
                                    }
                                )
                    case 4: # База
                        self.elements.append(
                                {
                                    "texture": self._texture_pool.get_texture(
                                        cfg.settings.path.base
                                        ),
                                    "rect": arcade.rect.XYWH(x, y, 128, 128),
                                    }
                                )
                x += 128
            y += 128

    def draw(self):
        for el in self.elements:
            arcade.draw_texture_rect(**el)
