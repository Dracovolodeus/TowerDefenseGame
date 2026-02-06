from typing import Literal

import arcade
from arcade.gui import UIAnchorLayout, UIBoxLayout, UIFlatButton, UILabel

import config as cfg
from core.gui.components.ResearchButton import ResearchButton
from core.gui.views.base import BaseView
from core.images.texture_pool import TexturePool
from core.research.controller import ResearchController


class ResearchView(BaseView):
    def __init__(self, gui_manager, texture_pool: TexturePool):
        super().__init__(gui_manager, texture_pool)
        self.research_controller = ResearchController()

    def setup_widgets(self) -> None:
        if self._widgets_initialized:
            return

        self._widgets_initialized = True

        self.background = self._texture_pool.get_texture(
            cfg.settings.path.research_menu
        )
        self.bg_x, self.bg_y = self.width // 2, self.height // 2

        anchor_layout = UIAnchorLayout()

        attack_box = UIBoxLayout(spacing=15, space_between=30)
        speed_box = UIBoxLayout(spacing=15, space_between=30)
        length_box = UIBoxLayout(spacing=15, space_between=30)

        attack_texture = self._texture_pool.get_texture(cfg.settings.path.damage)
        length_texture = self._texture_pool.get_texture(cfg.settings.path.length)
        speed_texture = self._texture_pool.get_texture(cfg.settings.path.speed)

        self.__btns = {
            "attack": [
                ResearchButton(
                    research_id=f"damage_{i}",
                    text="Урон +10%",
                    width=260,
                    icon_texture=attack_texture,
                )
                for i in range(1, 4)
            ],
            "length": [
                ResearchButton(
                    research_id=f"distans_{i}",
                    text="Дистанция стрельбы +10%",
                    width=260,
                    icon_texture=length_texture,
                )
                for i in range(1, 4)
            ],
            "speed": [
                ResearchButton(
                    research_id=f"delay_{i}",
                    text="Скорострельность +10%",
                    width=260,
                    icon_texture=speed_texture,
                )
                for i in range(1, 4)
            ],
        }

        for btn in self.__btns["attack"]:
            btn.on_click = lambda event: self.__bye_upgrade("damage")
            attack_box.add(btn)
        for btn in self.__btns["length"]:
            btn.on_click = lambda event: self.__bye_upgrade("distans")
            length_box.add(btn)
        for btn in self.__btns["speed"]:
            btn.on_click = lambda event: self.__bye_upgrade("delay")
            speed_box.add(btn)

        attack_box.add(UILabel("Улучшить Урон:", font_size=18))
        speed_box.add(UILabel("Улучшить Скорострельность:", font_size=18))
        length_box.add(UILabel("Улучшить Дальность Стрельбы:", font_size=18))

        back_button = UIFlatButton(x=50, y=self.height - 100, text="<")
        back_button.on_click = lambda event: self._gui_manager.set_start_menu()
        box = UIBoxLayout(vertical=False, space_between=100)

        box.add(attack_box)
        box.add(length_box)
        box.add(speed_box)

        self.money_label = UILabel(
            f"Количество монет: {cfg.settings.save.money}",
            font_size=16,
            x=cfg.settings.screen.width - 300,
            y=cfg.settings.screen.height - 75,
        )

        self._manager.add(self.money_label)

        anchor_layout.add(box)
        self._manager.add(back_button)
        self._manager.add(anchor_layout)
        self.__set_active_buttons()

    def on_draw(self) -> None:
        self.clear()
        arcade.draw_texture_rect(
            self.background,
            arcade.rect.XYWH(self.bg_x, self.bg_y, self.width, self.height),
        )
        self._manager.draw()

    def __set_active_buttons(self) -> None:
        for btn in self.__btns["attack"] + self.__btns["length"] + self.__btns["speed"]:
            btn.disabled = self.research_controller.button_is_active(btn.research_id)

    def __bye_upgrade(self, type_: Literal["damage", "distans", "delay"]) -> None:
        if self.research_controller.bye_upgrade(type_):
            self.__set_active_buttons()
            self.money_label.text = f"Количество монет: {cfg.settings.save.money}"
