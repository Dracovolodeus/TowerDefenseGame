import math

import arcade

from core.play.components.enemies.base_enemy import BaseEnemy


class CommonBullet(arcade.Sprite):
    def __init__(
        self,
        position: tuple[float, float],
        angle: float,
        speed: float,
        damage: float,
        enemies_list: arcade.SpriteSequence[BaseEnemy],
        texture: arcade.Texture,
    ):
        super().__init__()
        angle_rad = math.radians(angle)
        self.texture = texture
        self.speed = speed
        self.damage = damage
        self.center_x, self.center_y = position
        self.enemies_list = enemies_list
        self.change_y = self.speed * math.cos(angle_rad)
        self.change_x = self.speed * math.sin(angle_rad)
        self.change_angle = 100

    def __check_collision(self) -> None:
        values = arcade.check_for_collision_with_list(self, self.enemies_list)
        if values:
            values[0].deal_damage(self.damage)
            self.kill()

    def update(self, delta_time: float = 1 / 60, *args, **kwargs) -> None:
        self.center_x += self.change_x * delta_time
        self.center_y += self.change_y * delta_time
        self.angle = (self.angle + self.change_angle * delta_time) % 360
        self.__check_collision()
