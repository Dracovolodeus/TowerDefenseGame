import random
from pathlib import Path
from typing import Callable

import config as cfg
from core.images.texture_pool import TexturePool
from core.play.components.enemies.base_enemy import BaseEnemy


class BossEnemy(BaseEnemy):
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

    def deal_damage(self, value: float | int) -> None:
        if random.random() >= cfg.settings.enemies.boss_impenetrability_probability:
            super().deal_damage(value)
        elif random.random() >= cfg.settings.enemies.boss_part_penetration_probability:
            super().deal_damage(value / 5)

    def update(self, delta_time: float = 1 / 60, *args, **kwargs) -> None:
        self._move(delta_time)
