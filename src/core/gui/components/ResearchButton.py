import copy

import arcade
from arcade.color import GRAY_BLUE, LIGHT_GRAY
from arcade.gui import UIBoxLayout, UIFlatButton, UIImage, UILabel, UIOnClickEvent


class ResearchButton(UIFlatButton):
    def __init__(self, research_id, icon_texture, text="", **kwargs):
        super().__init__(text="", **kwargs)

        self.research_id = research_id

        content_layout = UIBoxLayout(vertical=False, align="center", space_between=8)

        self.icon = UIImage(texture=icon_texture, width=48, height=48)
        content_layout.add(self.icon.with_padding(left=12))

        self.text_label = UILabel(
            text=text,
            font_size=kwargs.get("font_size", 14),
            text_color=arcade.color.WHITE,
            multiline=False,
        )
        content_layout.add(self.text_label.with_padding(right=12))

        self.add(content_layout.with_padding(top=8, bottom=8))
