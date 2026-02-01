from arcade import View
from arcade.gui import UIManager

from core.images.texture_pool import TexturePool


class BaseView(View):
    def __init__(self, gui_manager, texture_pool: TexturePool):
        super().__init__()
        self._manager = UIManager()
        self._gui_manager = gui_manager
        self._texture_pool = texture_pool
        self._widgets_initialized = False

    def on_show_view(self):
        self.setup_widgets()
        self._manager.enable()

    def on_hide_view(self):
        self._manager.disable()

    def setup_widgets(self) -> None: ...
