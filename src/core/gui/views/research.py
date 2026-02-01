import arcade
from arcade.gui import UIAnchorLayout, UIBoxLayout, UILabel, UIManager

import config as cfg
from core.gui.components.ResearchButton import ResearchButton


class ResearchView(arcade.View):
    def __init__(self):
        super().__init__()

        self.anchor_layout = UIAnchorLayout()
        self.box = UIBoxLayout(vertical=False, space_between=100)
        self.ui_manager = UIManager()

    def on_show_view(self):
        self.ui_manager.enable()
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

        self.box.add(attack_box)
        self.box.add(length_box)
        self.box.add(speed_box)

        self.anchor_layout.add(self.box)

        self.ui_manager.add(self.anchor_layout)

    def on_hide_view(self):
        self.ui_manager.disable()

    def on_draw(self):
        self.clear()
        self.ui_manager.draw()
