from pathlib import Path
from typing import Callable

from core.images.texture_pool import TexturePool
from core.play.components.enemies.base_enemy import BaseEnemy


class CommonEnemy(BaseEnemy):
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
        super().__init__(
            speed, health, texture_pool, texture_path, deal_damage_game, position, route
        )

    def update(self, delta_time: float = 1 / 60, *args, **kwargs) -> None:
        self._move(delta_time)
