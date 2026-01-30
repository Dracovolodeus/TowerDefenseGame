import arcade
from arcade.gui import (
    UIFlatButton, UIImage
)
from pymunk.examples.arrows import height


class ResearchButton(UIFlatButton):
    def __init__(self, research_id, icon_texture, **kwargs):
        super().__init__(**kwargs)
        self.research_id = research_id
        self.icon_texture = icon_texture

        self.icon = UIImage(
            texture=self.icon_texture,
            width=48, height=48
        )

        self.add(self.icon)

    def on_click(self, event):
        # TODO Надо сделать логику исследования
        print("Сделай логику исследования😡")
        ...