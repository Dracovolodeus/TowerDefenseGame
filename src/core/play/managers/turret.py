from typing import Literal

import config as cfg
from core.images.texture_pool import TexturePool
from core.play.components.turrets.base import Base
from core.play.components.turrets.base_turret import BaseTurret
from core.play.components.turrets.multishoot import Multishoot
from core.play.components.turrets.shotgun import Shotgun
from core.play.components.turrets.sniper import Sniper
from core.play.components.turrets.venom import Venom
from core.play.managers.bullet import BulletManager
from core.play.managers.enemy import EnemyManager


class TurretsManager:
    def __init__(
        self,
        texture_pool: TexturePool,
        enemy_manager: EnemyManager,
        bullet_manager: BulletManager,
    ) -> None:
        self.__turrets_list: list[BaseTurret] = []
        self.__texture_pool = texture_pool
        self.__enemy_manager = enemy_manager
        self.__bullet_manager = bullet_manager

    def update(self, delta_time: float) -> None:
        for turret in self.__turrets_list:
            turret.update(delta_time)

    def draw_bases(self) -> None:
        for turret in self.__turrets_list:
            turret.draw_base()

    def draw_towers(self) -> None:
        for turret in self.__turrets_list:
            turret.draw_tower()

    def add_turret(
        self,
        turret_type: Literal["base", "sniper", "multishoot", "shotgun", "venom"],
        position: tuple[int, int],
    ) -> None:
        class_dict = {
            "base": Base,
            "sniper": Sniper,
            "shotgun": Shotgun,
            "venom": Venom,
            "multishoot": Multishoot,
        }
        class_ = class_dict[turret_type]
        turret_paths = cfg.settings.path.get_turret(turret_type)
        turret = class_(
            position=position,
            texture_pool=self.__texture_pool,
            base_texture_path=turret_paths.base,
            tower_texture_path=turret_paths.tower,
            bullet_texture_path=turret_paths.bullet,
            enemy_manager=self.__enemy_manager,
            bullet_manager=self.__bullet_manager,
        )
        self.__turrets_list.append(turret)
