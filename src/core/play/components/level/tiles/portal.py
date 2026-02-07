import arcade

import config as cfg
from core.images.texture_pool import TexturePool


class Portal(arcade.Sprite):
    def __init__(self, texture_pool: TexturePool, position: tuple[int, int]) -> None:
        super().__init__()
        self.__texture_pool = texture_pool
        self.__texture_list = [
            self.__texture_pool.get_texture(cfg.settings.path.portal_0),
            self.__texture_pool.get_texture(cfg.settings.path.portal_1),
            self.__texture_pool.get_texture(cfg.settings.path.portal_2),
            self.__texture_pool.get_texture(cfg.settings.path.portal_3),
            self.__texture_pool.get_texture(cfg.settings.path.portal_2),
            self.__texture_pool.get_texture(cfg.settings.path.portal_1),
        ]
        self.texture = self.__texture_list[0]
        self.position = (
            position[0] - self.texture.width / 2,
            position[1] - self.texture.height / 2,
        )
        self.__animation_delta = 0
        self.__animation_index = 0

    def __animation(self, delta_time: float) -> None:
        self.__animation_delta += delta_time
        if self.__animation_delta >= 0.05:
            self.__animation_delta = 0
            self.__animation_index += 1
            if self.__animation_index == len(self.__texture_list):
                self.__animation_index = 0
            self.texture = self.__texture_list[self.__animation_index]

    def update(self, delta_time: float = 1 / 60, *args, **kwargs) -> None:
        self.__animation(delta_time)
        return super().update(delta_time, *args, **kwargs)
