from arcade import Window

from core.gui.gui_manager import GUIManager
from core.images.texture_pool import TexturePool


class GameManager:
    def __init__(self, app: Window) -> None:
        texture_pool: TexturePool = TexturePool()
        self.gui = GUIManager(app, texture_pool)
