from typing import Literal

import config as cfg


class ResearchController:

    @staticmethod
    def bye_upgrade(type_: Literal["damage", "distans", "delay"]) -> bool:
        match type_:
            case "damage":
                if (
                    cfg.settings.save.money
                    >= cfg.settings.research_upgrade.damage_price
                ):
                    cfg.settings.save.money -= (
                        cfg.settings.research_upgrade.damage_price
                    )
                    cfg.settings.save.turret_damage += 1
                    cfg.settings.save.save()
                    return True
            case "distans":
                if (
                    cfg.settings.save.money
                    >= cfg.settings.research_upgrade.distans_price
                ):
                    cfg.settings.save.money -= (
                        cfg.settings.research_upgrade.distans_price
                    )
                    cfg.settings.save.turret_distans += 1
                    cfg.settings.save.save()
                    return True
            case "delay":
                if cfg.settings.save.money >= cfg.settings.research_upgrade.speed_price:
                    cfg.settings.save.money -= cfg.settings.research_upgrade.speed_price
                    cfg.settings.save.turret_speed += 1
                    cfg.settings.save.save()
                    return True
        return False

    @staticmethod
    def button_is_active(
        type_: Literal[
            "damage_1",
            "damage_2",
            "damage_3",
            "distans_1",
            "distans_2",
            "distans_3",
            "delay_1",
            "delay_2",
            "delay_3",
        ],
    ) -> bool:
        match type_:
            case "damage_1":
                return cfg.settings.save.turret_damage >= 1
            case "damage_2":
                return cfg.settings.save.turret_damage >= 2
            case "damage_3":
                return cfg.settings.save.turret_damage >= 3
            case "distans_1":
                return cfg.settings.save.turret_distans >= 1
            case "distans_2":
                return cfg.settings.save.turret_distans >= 2
            case "distans_3":
                return cfg.settings.save.turret_distans >= 3
            case "delay_1":
                return cfg.settings.save.turret_speed >= 1
            case "delay_2":
                return cfg.settings.save.turret_speed >= 2
            case "delay_3":
                return cfg.settings.save.turret_speed >= 3
