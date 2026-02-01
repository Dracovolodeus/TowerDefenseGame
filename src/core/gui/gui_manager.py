from arcade import Window

from core.gui.views.research import ResearchView
from core.gui.views.select_level import SelectLevelView
from core.gui.views.start import StartView
from core.images.texture_pool import TexturePool
from core.play.views.level import Level


class GUIManager:
    def __init__(self, app: Window, texture_pool: TexturePool) -> None:
        self.__app = app
        self.__texture_pool = texture_pool
        self.__start_menu = StartView(self, self.__texture_pool)
        self.__research_menu = ResearchView()
        self.__select_level_menu = SelectLevelView(self, self.__texture_pool)

    def set_start_menu(self) -> None:
        self.__app.show_view(self.__start_menu)

    def set_level_selection_menu(self) -> None:
        self.__app.show_view(self.__select_level_menu)

    def set_researches_menu(self) -> None:
        self.__app.show_view(self.__research_menu)

    def set_level_screen(self, level_number: int) -> None:
        self.__app.show_view(Level(self.__texture_pool, level_number))
