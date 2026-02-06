from pathlib import Path
from typing import override

import config as cfg
from core.images.texture_pool import TexturePool
from core.play.components.bullets.common_bullet import CommonBullet
from core.play.components.turrets.base_turret import BaseTurret
from core.play.managers.bullet import BulletManager
from core.play.managers.enemy import EnemyManager


class Sniper(BaseTurret):
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
            cfg.settings.turrets.sniper.damage,
            cfg.settings.turrets.sniper.distans,
            cfg.settings.turrets.sniper.delay,
        )
        self.__co_circle_for_shoot = self._create_coordinate_circle(25)

    def _create_bullet(self):
        try:
            self._bullet_manager.add_bullet(
                CommonBullet(
                    position=self.__co_circle_for_shoot[int(self._angle)],
                    angle=self._angle,
                    speed=cfg.settings.turrets.sniper.bullet_speed,
                    damage=self.damage,
                    enemies_list=self._enemy_manager.get_all_enemies(),
                    texture=self.bullet_texture,
                )
            )
        except:
            ...

    @override
    def update(self, delta_time: float) -> None:
        self.delay_count += delta_time
        self._shoot()
