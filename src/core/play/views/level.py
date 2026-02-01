import arcade
from core.images.texture_pool import TexturePool
from core.play.map import LevelMap

class Level(arcade.View):
    def __init__(self, texture_pool: TexturePool, level_number: int) -> None:
        super().__init__()
        self._texture_pool = texture_pool
        self.level_map = LevelMap(texture_pool, level_number)

    def on_show_view(self) -> None:
        ...

    def on_hide_view(self) -> None:
        ...

    def on_draw(self) -> None:
        self.clear()
        self.level_map.draw()
