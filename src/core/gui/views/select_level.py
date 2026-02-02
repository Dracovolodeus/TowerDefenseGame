import arcade
from arcade.gui import UIAnchorLayout, UIBoxLayout, UIFlatButton

from core.gui.views.base import BaseView


class SelectLevelView(BaseView):

    def setup_widgets(self) -> None:
        if self._widgets_initialized:
            return

        self._widgets_initialized = True

        anchor = UIAnchorLayout()

        box = UIBoxLayout(vertical=False, space_between=75)

        btn_level1 = UIFlatButton(width=100, height=100, text="1")
        btn_level1.on_click = lambda event: self._gui_manager.set_level_screen(1)

        btn_level2 = UIFlatButton(width=100, height=100, text="2")
        btn_level3 = UIFlatButton(width=100, height=100, text="3")
        btn_level4 = UIFlatButton(width=100, height=100, text="4")
        btn_level5 = UIFlatButton(width=100, height=100, text="5")

        box.add(btn_level1)
        box.add(btn_level2)
        box.add(btn_level3)
        box.add(btn_level4)
        box.add(btn_level5)

        anchor.add(child=box, anchor_x="center", anchor_y="center")

        back_button = UIFlatButton(x=50, y=self.height - 100, text="<")
        back_button.on_click = lambda event: self._gui_manager.set_start_menu()

        self._manager.add(anchor)
        self._manager.add(back_button)

    def on_draw(self):
        self.clear()
        self._manager.draw()
