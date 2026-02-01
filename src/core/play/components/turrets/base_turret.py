from pathlib import Path
from typing import ClassVar, Literal

import arcade

from core.images.texture_pool import TexturePool


class BaseTurret:
    type: ClassVar[Literal["base", "sniper"]]
    name: ClassVar[Literal["base", "sniper"]]

    def __init__(
        self,
        texture_pool: TexturePool,
        base_texture_path: Path,
        tower_texture_path: Path,
        bullet_texture_path: Path,
        position: tuple[int, int],
    ) -> None:
        self._texture_pool = texture_pool
        self.bullet_texture = self._texture_pool.get_texture(bullet_texture_path)
        self.base = arcade.Sprite(
            self._texture_pool.get_texture(base_texture_path),
            center_x=position[0],
            center_y=position[1],
        )
        self.tower = arcade.Sprite(
            self._texture_pool.get_texture(tower_texture_path),
            center_x=position[0],
            center_y=position[1],
        )
        self.elements_lists = arcade.SpriteList()
        self.elements_lists.append(self.base)
        self.elements_lists.append(self.tower)

    def update(self, delta_time: float) -> None: ...

    def draw(self) -> None:
        self.elements_lists.draw()

    @property
    def _angle(self) -> float:
        return self.tower.angle

    @_angle.setter
    def _angle(self, angle: float) -> None:
        self.tower.angle = angle

