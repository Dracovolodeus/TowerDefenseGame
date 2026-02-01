import arcade
from arcade.color import GRAY_BLUE, GRAY
from arcade.csscolor import DARK_GRAY
from arcade.gui import (
    UIManager, UIBoxLayout, UIAnchorLayout, UILabel, UIFlatButton
)


class Level1(arcade.View):
    def __init__(self):
        super().__init__()

        # Будет сделано когда будет json файлик

        self.anchor_layout = UIAnchorLayout()
        self.box = UIBoxLayout(vertical=False, space_between=50)
        self.ui_manager = UIManager()

    def on_show_view(self):
        self.ui_manager.enable()

    def on_hide_view(self):
        self.ui_manager.disable()

    def on_draw(self):
        self.clear()
        self.ui_manager.draw()
