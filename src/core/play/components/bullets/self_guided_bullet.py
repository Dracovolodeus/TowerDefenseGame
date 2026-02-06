import math
import config as cfg

import arcade

from core.play.components.enemies.base_enemy import BaseEnemy


class SelfGuidedBullet(arcade.Sprite):
    def __init__(
        self,
        position: tuple[float, float],
        target: BaseEnemy,
        speed: float,
        damage: float,
        texture: arcade.Texture,
    ):
        super().__init__()
        self.texture = texture
        self.speed = speed
        self.damage = damage
        self.center_x, self.center_y = position
        self.target = target
        self.__path = 0

    def __check_collision(self) -> None:
        if arcade.check_for_collision(self, self.target):
            self.target.deal_damage(self.damage)
            self.kill()

    def update(self, delta_time: float = 1 / 60, *args, **kwargs) -> None:
        target_position = self.target.get_position()
        angle = math.degrees(
            math.atan2(
                target_position[1] - self.center_y, target_position[0] - self.center_x
            )
        )
        angle_rad = math.radians(angle)
        self.center_x += self.speed * math.cos(angle_rad) * delta_time
        self.center_y += self.speed * math.sin(angle_rad) * delta_time
        self.__path += self.speed
        if self.__path > math.sqrt(cfg.settings.screen.width ** 2 + cfg.settings.screen.height ** 2) * 1.5:
            self.kill()
        self.angle = angle
        self.__check_collision()
