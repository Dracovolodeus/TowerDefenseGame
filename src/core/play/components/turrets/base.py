from pathlib import Path
from typing import override

from core.images.texture_pool import TexturePool
from core.play.components.turrets.base_turret import BaseTurret


class Base(BaseTurret):
    type = "base"
    name = "base"

    def __init__(
        self,
        texture_pool: TexturePool,
        base_texture_path: Path,
        tower_texture_path: Path,
        bullet_texture_path: Path,
        position: tuple[int, int],
    ) -> None:
        super().__init__(
            texture_pool,
            base_texture_path,
            tower_texture_path,
            bullet_texture_path,
            position,
        )

    @override
    def update(self, delta_time: float) -> None:
        self._angle += 10 * delta_time if self._angle + 10 * delta_time < 360 else -self._angle
