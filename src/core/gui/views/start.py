import arcade
from arcade.gui import UIFlatButton

import config as cfg
from core.gui.views.base import BaseView


class StartView(BaseView):

    def setup_widgets(self) -> None:
        if not self._widgets_initialized:
            self._widgets_initialized = True

            self.background = self._texture_pool.get_texture(
                cfg.settings.path.start_menu
            )
            self.bg_x, self.bg_y = self.width // 2, self.height // 2

            btn_continue = UIFlatButton(
                x=1210, y=500, width=250, height=65, text=cfg.settings.text.continue_
            )
            btn_level_selection = UIFlatButton(
                x=1210, y=430, width=250, height=65, text=cfg.settings.text.start
            )
            btn_researches = UIFlatButton(
                x=1210, y=360, width=250, height=65, text=cfg.settings.text.researches
            )
            btn_level_selection.on_click = (
                lambda event: self._gui_manager.set_level_selection_menu()
            )
            btn_researches.on_click = (
                lambda event: self._gui_manager.set_researches_menu()
            )
            btn_continue.disabled = not cfg.settings.save.have_saved_game
            self._manager.add(btn_level_selection)
            self._manager.add(btn_continue)
            self._manager.add(btn_researches)

    def on_draw(self) -> None:
        self.clear()
        arcade.draw_texture_rect(
            self.background,
            arcade.rect.XYWH(self.bg_x, self.bg_y, self.width, self.height),
        )
        self._manager.draw()
