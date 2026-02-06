import arcade
from arcade.gui import UIManager, UIAnchorLayout, UIBoxLayout, UILabel
import config as cfg
from core.gui.components.play.tower_button import TowerButton


class PlayGUI:
    def __init__(self, health):
        self.cur_health = health
        self.max_health = health

        self.turret_placed = None
        self.curr_position = (0, 0)

        self.backgroundPath = cfg.settings.path.tower_menu

        self.manager = UIManager()
        self.manager.enable()

        base_turret = cfg.settings.path.get_turret("base")
        sniper_turret = cfg.settings.path.get_turret("sniper")
        multishoot_turret = cfg.settings.path.get_turret("multishoot")
        shotgun_turret = cfg.settings.path.get_turret("shotgun")
        venom_turret = cfg.settings.path.get_turret("venom")

        box = UIBoxLayout(
            vertical=True,
            x=cfg.settings.screen.width - 500,
            y=0,
            width=500,
            height=cfg.settings.screen.height,
            space_between=8
        )



        box.add(UILabel(text="Обычная", font_size=16).with_padding(top=128))

        box.add(TowerButton(
            base_texture_path=base_turret.base,
            tower_texture_path=base_turret.tower,
            turret_name="base",
            on_select=self.select_turret
        ))

        box.add(UILabel(text="Снайпер", font_size=16))

        box.add(TowerButton(
            base_texture_path=sniper_turret.base,
            tower_texture_path=sniper_turret.tower,
            turret_name="sniper",
            on_select=self.select_turret
        ))

        box.add(UILabel(text="Мульти выстрел", font_size=16))

        box.add(TowerButton(
            base_texture_path=multishoot_turret.base,
            tower_texture_path=multishoot_turret.tower,
            turret_name="multishoot",
            on_select=self.select_turret
        ))

        box.add(UILabel(text="Дробовик", font_size=16))

        box.add(TowerButton(
            base_texture_path=shotgun_turret.base,
            tower_texture_path=shotgun_turret.tower,
            turret_name="shotgun",
            on_select=self.select_turret
        ))

        box.add(UILabel(text="Веном", font_size=20))

        box.add(TowerButton(
            base_texture_path=venom_turret.base,
            tower_texture_path=venom_turret.tower,
            turret_name="venom",
            on_select=self.select_turret
        ))

        self.manager.add(box)

    def select_turret(self, turret_name: str):
        self.turret_placed = turret_name

    def draw_hp(self):
        arcade.draw_line(
            300, 10,
            1000 * (self.cur_health / self.max_health),
            10,
            arcade.color.GREEN,
            10,
        )
        arcade.draw_line(
            max(300, 1000 * (self.cur_health / self.max_health)),
            10,
            1000,
            10,
            arcade.color.RED,
            10,
        )

    def draw_menu(self):
        arcade.draw_lbwh_rectangle_filled(
            cfg.settings.screen.width - 600,
            0,
            600,
            cfg.settings.screen.height,
            arcade.color.DARK_BLUE,
        )

    """
    TODO Сделать логику отрисовки GUI во время игры.
    Тебе нужно сделать:
    2) Кликабельность платформ (core/play/components/level/какае-то_директория/platform.py ---> НЕ ГОТОВО!!!!!!!!!!!
    Чтобы когда тыкаешь на нее ЛКМ вылазила менюшка с выбором башни. Менюшку пиши тут, вызывай методом, желательно сделать проверку на деньгу
    """
