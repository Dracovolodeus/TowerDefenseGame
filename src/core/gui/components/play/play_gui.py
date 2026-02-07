import arcade
from arcade.gui import UIAnchorLayout, UIBoxLayout, UIFlatButton, UILabel, UIManager

import config as cfg
from core.gui.components.play.tower_button import TowerButton


class PlayGUI:
    def __init__(self, health, on_skip, gui_manager):
        self.cur_health = health
        self.max_health = health

        self.on_skip = on_skip

        self.is_paused = False

        self.turret_placed = None
        self.curr_position = (0, 0)

        self.backgroundPath = cfg.settings.path.tower_menu

        self._money = 225
        self._wave = 0

        self.manager = UIManager()
        self.menu_manager = UIManager()
        self.loose_manager = UIManager()

        self.menu_manager.enable()
        self.manager.enable()

        base_turret = cfg.settings.path.get_turret("base")
        sniper_turret = cfg.settings.path.get_turret("sniper")
        multishoot_turret = cfg.settings.path.get_turret("multishoot")
        shotgun_turret = cfg.settings.path.get_turret("shotgun")
        venom_turret = cfg.settings.path.get_turret("venom")

        self.base_price = cfg.settings.turrets.base.price
        self.sniper_price = cfg.settings.turrets.sniper.price
        self.multishoot_price = cfg.settings.turrets.multishoot.price
        self.shotgun_price = cfg.settings.turrets.shotgun.price
        self.venom_price = cfg.settings.turrets.venom.price

        self.skip_wave_button = arcade.gui.UIFlatButton(
            text="Пропустить кд волны",
            width=175,
            height=50,
            x=cfg.settings.screen.width - 250,
            y=25,
        )
        self.skip_wave_button.on_click = self.on_skip

        box = UIBoxLayout(
            vertical=True,
            x=cfg.settings.screen.width - 500,
            y=0,
            width=500,
            height=cfg.settings.screen.height,
            space_between=8,
        )

        box.add(
            UILabel(
                text=f"Обычная (Цена: {self.base_price})", font_size=16
            ).with_padding(top=128)
        )
        box.add(
            TowerButton(
                base_texture_path=base_turret.base,
                tower_texture_path=base_turret.tower,
                turret_name="base",
                on_select=self.select_turret,
            )
        )

        box.add(UILabel(text=f"Снайпер (Цена: {self.sniper_price})", font_size=16))

        box.add(
            TowerButton(
                base_texture_path=sniper_turret.base,
                tower_texture_path=sniper_turret.tower,
                turret_name="sniper",
                on_select=self.select_turret,
            )
        )

        box.add(
            UILabel(text=f"Мультистрел (Цена: {self.multishoot_price})", font_size=16)
        )

        box.add(
            TowerButton(
                base_texture_path=multishoot_turret.base,
                tower_texture_path=multishoot_turret.tower,
                turret_name="multishoot",
                on_select=self.select_turret,
            )
        )

        box.add(UILabel(text=f"Дробовик (Цена: {self.shotgun_price})", font_size=16))

        box.add(
            TowerButton(
                base_texture_path=shotgun_turret.base,
                tower_texture_path=shotgun_turret.tower,
                turret_name="shotgun",
                on_select=self.select_turret,
            )
        )

        box.add(UILabel(text=f"Веном (Цена: {self.venom_price})", font_size=20))

        box.add(
            TowerButton(
                base_texture_path=venom_turret.base,
                tower_texture_path=venom_turret.tower,
                turret_name="venom",
                on_select=self.select_turret,
            )
        )

        button = UIFlatButton(
            x=25, y=cfg.settings.screen.height - 75, width=50, height=50, text="||"
        )
        button.on_click = self.toogle_pause

        self.text_money = UILabel(f"Деньги: {self._money}", x=25, y=25)
        self.wave_text = UILabel(f"Волна: {self._wave}", x=175, y=25)

        self.loose_anchor = UIAnchorLayout()
        loose_box = UIBoxLayout(vertical=True)
        loose_box.add(UILabel(f"Вы дошли до {self._wave} волны", font_size=36))
        self.result_money_label = UILabel(f"Вы заработали {0} монет", font_size=36)
        loose_box.add(self.result_money_label)
        self.loose_button = UIFlatButton(text="Выйти в выбор уровней", width=300, height=100)

        self.loose_button.on_click = lambda event: gui_manager.set_level_selection_menu()
        self.loose_button.disabled = True

        loose_box.add(self.loose_button)

        self.loose_anchor.add(loose_box)
        self.loose_manager.add(self.loose_anchor)

        self.manager.add(button)
        self.manager.add(self.text_money)
        self.manager.add(self.wave_text)
        self.manager.add(self.skip_wave_button)

        self.menu_manager.add(box)

    def select_turret(self, turret_name: str):
        self.turret_placed = turret_name

    def set_result_money(self, value: int) -> None:
        self.result_money_label.text = f"Вы заработали {value} монет"

    def draw_hp(self):
        arcade.draw_line(
            300,
            10,
            max(300, 1000 * (self.cur_health / self.max_health)),
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

    def toogle_pause(self, event=None):
        self.is_paused = not self.is_paused

    def change_money(self, value):  # value может быть отрицательным и положительным
        self._money += value
        self.text_money.text = f"Деньги: {self._money}"

    def can_be_buyed(self, name):
        price_dict = {
            "base": self.base_price,
            "sniper": self.sniper_price,
            "shotgun": self.shotgun_price,
            "venom": self.venom_price,
            "multishoot": self.multishoot_price,
        }
        if self._money >= price_dict[name]:
            self.change_money(-price_dict[name])
            return True
        else:
            return False

    def sell_turret(self, name):
        price_for_sale_dict = {
            "base": round(self.base_price * cfg.settings.turrets.sale_coeff),
            "sniper": round(self.sniper_price * cfg.settings.turrets.sale_coeff),
            "shotgun": round(self.shotgun_price * cfg.settings.turrets.sale_coeff),
            "venom": round(self.venom_price * cfg.settings.turrets.sale_coeff),
            "multishoot": round(
                self.multishoot_price * cfg.settings.turrets.sale_coeff
            ),
        }
        self.change_money(price_for_sale_dict[name])

    def set_wave(self, wave):
        self._wave = wave
        self.wave_text.text = f"Волна: {self._wave}"
