from typing import Callable

import arcade
from arcade.gui import UIFlatButton, UIImage, UIOnClickEvent


class TowerButton(UIFlatButton):
    def __init__(
        self,
        *,
        base_texture_path: str,
        tower_texture_path: str,
        size=80,
        turret_name: str,
        on_select: Callable[[str], None],
        **kwargs,
    ):
        super().__init__(width=size, height=size, **kwargs)

        self.turret_name = turret_name
        self.on_select = on_select

        base_texture = arcade.load_texture(base_texture_path)
        tower_texture = arcade.load_texture(tower_texture_path)

        self.base_image = UIImage(
            texture=base_texture,
            width=size,
            height=size,
        )

        scale = size / max(tower_texture.width, tower_texture.height)

        self.tower_image = UIImage(
            texture=tower_texture,
            width=int(tower_texture.width * scale),
            height=int(tower_texture.height * scale),
        )

        self.add(self.base_image)
        self.add(self.tower_image)

    def on_click(self, event: UIOnClickEvent):
        self.on_select(self.turret_name)
