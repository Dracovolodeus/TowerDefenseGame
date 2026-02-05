import arcade

from core.play.components.bullets.blast_bullet import BlastBullet
from core.play.components.bullets.common_bullet import CommonBullet
from core.play.components.bullets.self_guided_bullet import SelfGuidedBullet


class BulletManager:
    def __init__(self) -> None:
        self.__bullet_list = arcade.SpriteList()

    def update(self) -> None:
        self.__bullet_list.update()

    def draw(self) -> None:
        self.__bullet_list.draw()

    def add_bullet(self, bullet: CommonBullet | BlastBullet | SelfGuidedBullet) -> None:
        self.__bullet_list.append(bullet)
