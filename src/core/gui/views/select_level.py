import arcade
from arcade.gui import UIAnchorLayout, UIBoxLayout, UIFlatButton, UILabel

import config as cfg
from core.gui.views.base import BaseView


class SelectLevelView(BaseView):

    def on_show_view(self) -> None:
        super().on_show_view()
        self.record_lable_1.text = f"Рекорд: {cfg.settings.save.first_level_records}"
        self.record_lable_2.text = f"Рекорд: {cfg.settings.save.third_level_records}"
        self.record_lable_3.text = f"Рекорд: {cfg.settings.save.second_level_records}"
        self.record_lable_4.text = f"Рекорд: {cfg.settings.save.fourth_level_records}"
        self.record_lable_5.text = f"Рекорд: {cfg.settings.save.fifth_level_records}"

    def setup_widgets(self) -> None:
        if self._widgets_initialized:
            return

        self._widgets_initialized = True

        self.background = self._texture_pool.get_texture(
            cfg.settings.path.select_level_menu
        )
        self.bg_x, self.bg_y = self.width // 2, self.height // 2

        anchor = UIAnchorLayout()

        box = UIBoxLayout(vertical=False, space_between=75)

        btn_level1 = UIFlatButton(width=100, height=100, text="1")
        btn_level1.on_click = lambda event: self._gui_manager.set_level_screen(1)

        btn_level2 = UIFlatButton(width=100, height=100, text="2")
        btn_level2.on_click = lambda event: self._gui_manager.set_level_screen(2)

        btn_level3 = UIFlatButton(width=100, height=100, text="3")
        btn_level3.on_click = lambda event: self._gui_manager.set_level_screen(3)

        btn_level4 = UIFlatButton(width=100, height=100, text="4")
        btn_level4.on_click = lambda event: self._gui_manager.set_level_screen(4)

        btn_level5 = UIFlatButton(width=100, height=100, text="5")
        btn_level5.on_click = lambda event: self._gui_manager.set_level_screen(5)

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

        self.record_lable_1 = UILabel(
                f"Рекорд: {cfg.settings.save.first_level_records}",
                y=cfg.settings.screen.height // 2 - 100,
                x=375
            )
        self.record_lable_2 = UILabel(
                f"Рекорд: {cfg.settings.save.third_level_records}",
                y=cfg.settings.screen.height // 2 - 100,
                x=555
            )
        self.record_lable_3 = UILabel(
                f"Рекорд: {cfg.settings.save.second_level_records}",
                y=cfg.settings.screen.height // 2 - 100,
                x=735
            )
        self.record_lable_4 = UILabel(
                f"Рекорд: {cfg.settings.save.fourth_level_records}",
                y=cfg.settings.screen.height // 2 - 100,
                x=910
            )
        self.record_lable_5 = UILabel(
                f"Рекорд: {cfg.settings.save.fifth_level_records}",
                y=cfg.settings.screen.height // 2 - 100,
                x=1090,
                width=100
            )
        self._manager.add(self.record_lable_1)
        self._manager.add(self.record_lable_2)
        self._manager.add(self.record_lable_3)
        self._manager.add(self.record_lable_4)
        self._manager.add(self.record_lable_5)

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(
            self.background,
            arcade.rect.XYWH(self.bg_x, self.bg_y, self.width, self.height),
        )
        self._manager.draw()
