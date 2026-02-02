import arcade
from arcade.gui import UIAnchorLayout, UIBoxLayout, UILabel, UIManager, UIFlatButton

import config as cfg
from core.gui.components.ResearchButton import ResearchButton
from core.gui.views.base import BaseView


class ResearchView(BaseView):
    def setup_widgets(self) -> None:
        if self._widgets_initialized:
            return

        self._widgets_initialized = True

        anchor_layout =  UIAnchorLayout()

        attack_box = UIBoxLayout(spacing=15, space_between=30)
        speed_box = UIBoxLayout(spacing=15, space_between=30)
        length_box = UIBoxLayout(spacing=15, space_between=30)

        attack_texture = arcade.load_texture(cfg.settings.path.damage)
        length_texture = arcade.load_texture(cfg.settings.path.length)
        speed_texture = arcade.load_texture(cfg.settings.path.speed)

        attack_box.add(
            ResearchButton(
                research_id="research_1",
                text="Урон +10%",
                width=260,
                icon_texture=attack_texture,
            )
        )

        attack_box.add(
            ResearchButton(
                research_id="research_2",
                text="Урон +10%",
                width=260,
                icon_texture=attack_texture,
            )
        )

        attack_box.add(
            ResearchButton(
                research_id="research_3",
                text="Урон +10%",
                width=260,
                icon_texture=attack_texture,
            )
        )

        attack_box.add(UILabel("Улучшить Урон", font_size=18))

        speed_box.add(
            ResearchButton(
                research_id="research_1",
                text="Скорострельность +10%",
                width=260,
                icon_texture=speed_texture,
            )
        )

        speed_box.add(
            ResearchButton(
                research_id="research_2",
                text="Скорострельность +10%",
                width=260,
                icon_texture=speed_texture,
            )
        )

        speed_box.add(
            ResearchButton(
                research_id="research_3",
                text="Скорострельность +10%",
                width=260,
                icon_texture=speed_texture,
            )
        )

        speed_box.add(UILabel("Улучшить Скорострельность", font_size=18))

        length_box.add(
            ResearchButton(
                research_id="research_1",
                text="Длина стрельбы +10%",
                width=260,
                icon_texture=length_texture,
            )
        )

        length_box.add(
            ResearchButton(
                research_id="research_2",
                text="Длина стрельбы +10%",
                width=260,
                icon_texture=length_texture,
            )
        )

        length_box.add(
            ResearchButton(
                research_id="research_3",
                text="Длина стрельбы +10%",
                width=260,
                icon_texture=length_texture,
            )
        )

        length_box.add(UILabel("Улучшить Дальность Стрельбы", font_size=18))

        back_button = UIFlatButton(x=50, y=self.height - 100, text="<")
        back_button.on_click = lambda event: self._gui_manager.set_start_menu()
        box = UIBoxLayout(vertical=False, space_between=100)

        box.add(attack_box)
        box.add(length_box)
        box.add(speed_box)

        anchor_layout.add(box)
        self._manager.add(back_button)

        self._manager.add(anchor_layout)

    def on_draw(self):
        self.clear()
        self._manager.draw()
