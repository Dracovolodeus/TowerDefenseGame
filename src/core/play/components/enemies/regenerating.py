from pathlib import Path
from typing import Callable

from core.images.texture_pool import TexturePool
from core.play.components.enemies.base_enemy import BaseEnemy


class RegeneratingEnemy(BaseEnemy):
    def __init__(
        self,
        speed: float,
        health: float,
        texture_pool: TexturePool,
        texture_path: Path,
        deal_damage_game: Callable,
        position: tuple[int, int],
        route: list[tuple[int, int]],
        death_func: Callable,
    ) -> None:
        super().__init__(
            speed,
            health,
            texture_pool,
            texture_path,
            deal_damage_game,
            death_func,
            position,
            route,
        )
        self.max_health = health

    def regeneration(self, delta_time: float) -> None:
        new_health = self.health + 10 * delta_time
        if new_health <= self.max_health:
            self.health = new_health

    def update(self, delta_time: float = 1 / 60, *args, **kwargs) -> None:
        self.regeneration(delta_time)
        self._move(delta_time)
