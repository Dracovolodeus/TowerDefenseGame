import math
from functools import lru_cache
from pathlib import Path
from typing import Sequence

import arcade

from core.images.texture_pool import TexturePool
from core.play.components.enemies.base_enemy import BaseEnemy
from core.play.managers.bullet import BulletManager
from core.play.managers.enemy import EnemyManager


class BaseTurret:
    def __init__(
        self,
        texture_pool: TexturePool,
        base_texture_path: Path,
        tower_texture_path: Path,
        bullet_texture_path: Path,
        position: tuple[int | float, int | float],
        enemy_manager: EnemyManager,
        bullet_manager: BulletManager,
        damage: float,
        distans: float,
        delay: float,
    ) -> None:
        self.center_x, self.center_y = position
        self._enemy_manager = enemy_manager
        self.damage = damage
        self.distans = distans
        self.delay = delay
        self._texture_pool = texture_pool
        self._bullet_manager = bullet_manager
        self.bullet_texture = self._texture_pool.get_texture(bullet_texture_path)
        self.base = arcade.Sprite(
            self._texture_pool.get_texture(base_texture_path),
            center_x=self.center_x,
            center_y=self.center_y,
        )
        self.tower = arcade.Sprite(
            self._texture_pool.get_texture(tower_texture_path),
            center_x=self.center_x,
            center_y=self.center_y,
        )
        self.base_list = arcade.SpriteList()
        self.tower_list = arcade.SpriteList()
        self.base_list.append(self.base)
        self.tower_list.append(self.tower)

    def update(self, delta_time: float) -> None: ...

    def draw_base(self) -> None:
        self.base_list.draw()

    def draw_tower(self) -> None:
        self.tower_list.draw()

    @property
    def _angle(self) -> float:
        return self.tower.angle

    @_angle.setter
    def _angle(self, angle: float) -> None:
        self.tower.angle = angle

    def _get_last_enemy(self) -> BaseEnemy | None:
        result = None
        max_path = -1
        for enemy in self._enemy_manager.get_all_enemies():
            path = enemy.get_path()
            if (
                path > max_path
                and math.sqrt(
                    abs(enemy.center_x - self.center_x) ** 2
                    + abs(enemy.center_y - self.center_y) ** 2
                )
                <= self.distans
            ):
                result, max_path = enemy, path
        return result

    def _aim_last_enemy(self) -> bool:
        enemy = self._get_last_enemy()
        if enemy is None:
            return False
        position = enemy.get_position()
        angle = math.degrees(
            math.atan2(position[1] - self.center_y, position[0] - self.center_x)
        )
        self._angle = (-angle + 90) % 360
        return True

    @lru_cache
    def _create_coordinate_circle(self, radius: float) -> list[tuple[float, float]]:
        points = []
        num_points = 360
        angle_increment = 2 * math.pi / num_points
        for i in range(num_points):
            angle = i * angle_increment
            x = int(self.center_x + radius * math.cos(angle))
            y = int(self.center_y + radius * math.sin(angle))
            points.append((x, y))
        points = points[::-1]
        return [points[(i - 90) % 360] for i in range(360)]

    def _create_bullet(self): ...

    def _shoot(self) -> None:
        if self.delay >= 1 and self._aim_last_enemy():
            self._create_bullet()
            self.delay = 0
