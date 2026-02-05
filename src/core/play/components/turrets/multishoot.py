from pathlib import Path
from typing import override

import config as cfg
from core.images.texture_pool import TexturePool
from core.play.components.bullets.common_bullet import CommonBullet
from core.play.components.turrets.base_turret import BaseTurret
from core.play.managers.bullet import BulletManager
from core.play.managers.enemy import EnemyManager


class Multishoot(BaseTurret):
    def __init__(
        self,
        texture_pool: TexturePool,
        base_texture_path: Path,
        tower_texture_path: Path,
        bullet_texture_path: Path,
        position: tuple[int, int],
        enemy_manager: EnemyManager,
        bullet_manager: BulletManager,
    ) -> None:
        super().__init__(
            texture_pool,
            base_texture_path,
            tower_texture_path,
            bullet_texture_path,
            position,
            enemy_manager,
            bullet_manager,
            cfg.settings.turrets.multishoot.damage,
            cfg.settings.turrets.multishoot.distans,
            cfg.settings.turrets.multishoot.delay,
        )
        self.__co_circle_for_shoot = self._create_coordinate_circle(25)

    def _create_bullet(self):
        self.__co_circle_for_shoot[int(self._angle)]
        for pos, angle in (
            (self.__co_circle_for_shoot[int(self._angle) - 10], self._angle - 10),
            (self.__co_circle_for_shoot[int(self._angle) - 5], self._angle - 5),
            (self.__co_circle_for_shoot[int(self._angle)], self._angle),
            (self.__co_circle_for_shoot[int(self._angle) + 5], self._angle + 5),
            (self.__co_circle_for_shoot[int(self._angle) + 10], self._angle + 10),
        ):
            self._bullet_manager.add_bullet(
                CommonBullet(
                    position=pos,
                    angle=angle,
                    speed=cfg.settings.turrets.multishoot.bullet_speed,
                    damage=self.damage,
                    enemies_list=self._enemy_manager.get_all_enemies(),
                    texture=self.bullet_texture,
                )
            )

    @override
    def update(self, delta_time: float) -> None:
        self.delay += delta_time
        self._shoot()
