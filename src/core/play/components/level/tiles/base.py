import arcade

import config as cfg
from core.images.texture_pool import TexturePool


class Base(arcade.Sprite):
    def __init__(self, texture_pool: TexturePool, position: tuple[int, int]) -> None:
        super().__init__()
        self.__texture_pool = texture_pool
        self.texture = self.__texture_pool.get_texture(cfg.settings.path.base)
        self.position = (
            position[0] - self.texture.width / 2,
            position[1] - self.texture.height / 2,
        )
