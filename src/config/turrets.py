from dataclasses import dataclass, field

from config.save import Save


@dataclass
class Base:
    damage: float = 5
    delay: float = 0.4
    distans: float = 512
    bullet_speed: float = 375
    price: int = 0


@dataclass
class Sniper:
    damage: float = 10
    delay: float = 0.85
    distans: float = 2048
    bullet_speed: float = 1792
    price: int = 0


@dataclass
class Multishoot:
    damage: float = 5
    delay: float = 0.35
    distans: float = 640
    bullet_speed: float = 370
    price: int = 0


@dataclass
class Shotgun:
    damage: float = 5
    delay: float = 0.65
    distans: float = 512
    bullet_speed: float = 256
    price: int = 0
    blast_range: float = 96


@dataclass
class Venom:
    damage: float = 5
    delay: float = 0.59
    distans: float = 384
    price: int = 0
    bullet_speed: float = 80


class Turrets:
    def __init__(self, save: Save) -> None:
        self.base: Base = Base()
        self.sniper: Sniper = Sniper()
        self.multishoot: Multishoot = Multishoot()
        self.shotgun: Shotgun = Shotgun()
        self.venom: Venom = Venom()
        self.sale_coeff: float = 0.75

        self.base.delay = self.base.delay * (1 - save.turret_speed / 100)
        self.sniper.delay = self.sniper.delay * (1 - save.turret_speed / 100)
        self.multishoot.delay = self.multishoot.delay * (1 - save.turret_speed / 100)
        self.shotgun.delay = self.shotgun.delay * (1 - save.turret_speed / 100)
        self.venom.delay = self.venom.delay * (1 - save.turret_speed / 100)

        self.base.damage = self.base.damage * (1 + save.turret_damage / 100)
        self.sniper.damage = self.sniper.damage * (1 + save.turret_damage / 100)
        self.multishoot.damage = self.multishoot.damage * (1 + save.turret_damage / 100)
        self.shotgun.damage = self.shotgun.damage * (1 + save.turret_damage / 100)
        self.venom.damage = self.venom.damage * (1 + save.turret_damage / 100)

        self.base.distans = self.base.distans * (1 + save.turret_distans / 100)
        self.sniper.distans = self.sniper.distans * (1 + save.turret_distans / 100)
        self.multishoot.distans = self.multishoot.distans * (
            1 + save.turret_distans / 100
        )
        self.shotgun.distans = self.shotgun.distans * (1 + save.turret_distans / 100)
        self.venom.distans = self.venom.distans * (1 + save.turret_distans / 100)
