from pathlib import Path
from typing import Callable

import arcade

from core.images.texture_pool import TexturePool


class BaseEnemy(arcade.Sprite):
    def __init__(
        self,
        speed: float,
        health: float,
        texture_pool: TexturePool,
        texture_path: Path,
        deal_damage_game: Callable,
        position: tuple[int, int],
        route: list[tuple[int, int]],
    ) -> None:
        super().__init__()
        self._speed = speed
        self.health = health
        self._texture_pool = texture_pool
        self._route = route
        self.deal_damage_game = deal_damage_game
        self.center_x, self.center_y = position
        self._path = 0
        self._segment_progress = 0
        self.texture = self._texture_pool.get_texture(texture_path)

    def deal_damage(self, value: float | int) -> None:
        self.health -= value if self.health - value >= 0 else self.health
        if self.health == 0:
            self.kill()

    def _move(self, delta_time: float) -> None:
        if not self._route:
            self.deal_damage_game()
            self.kill()
            return
        change = self._speed * delta_time
        change_type = self._route[0][1]

        if self._route[0][0] - self._segment_progress <= change:
            change = self._route[0][0] - self._segment_progress
            self._segment_progress = 0
            del self._route[0]
        else:
            self._segment_progress += change

        match change_type:
            case 1:
                self.angle = 90
                self.forward(change)
            case -1:
                self.angle = 270
                self.forward(change)
            case 2:
                self.angle = 0
                self.forward(change)
            case -2:
                self.angle = 180
                self.forward(change)
        self._path += change
