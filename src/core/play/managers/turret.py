import config as cfg
from core.images.texture_pool import TexturePool
from core.play.components.turrets.base_turret import BaseTurret


class TurretsManager:
    def __init__(self, texture_pool: TexturePool) -> None:
        self.__turrets_list: list[BaseTurret] = []
        self.__texture_pool = texture_pool

    def update(self, delta_time: float) -> None:
        for turret in self.__turrets_list:
            turret.update(delta_time)

    def draw(self) -> None:
        for turret in self.__turrets_list:
            turret.draw()

    def add_turret(self, turret: type[BaseTurret], position: tuple[int, int]) -> None:
        turret_paths = cfg.settings.path.get_turret(turret.type)
        self.__turrets_list.append(
            turret(
                texture_pool=self.__texture_pool,
                base_texture_path=turret_paths.base,
                tower_texture_path=turret_paths.tower,
                bullet_texture_path=turret_paths.bullet,
                position=position,
            )
        )

    def get_all_turrets_variants(self) -> list[BaseTurret]:
        return []
