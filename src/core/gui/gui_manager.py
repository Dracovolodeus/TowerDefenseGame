from core.gui.views.level1 import Level1
from core.gui.views.select_level import SelectLevelView
from core.gui.views.start import StartView
from arcade import Window

from core.images.texture_pool import TexturePool

from core.gui.views.research import ResearchView


class GUIManager:
    def __init__(self, app: Window, texture_pool: TexturePool) -> None:
        self.__app = app
        self.__texture_pool = texture_pool
        self.__start_menu = StartView(self, self.__texture_pool)
        self.__research_menu = ResearchView()
        self.__select_level_menu = SelectLevelView(self, self.__texture_pool)
        self.__level1_screen = Level1()

    def set_start_menu(self) -> None:
        self.__app.show_view(self.__start_menu)

    def set_level_selection_menu(self) -> None:
        self.__app.show_view(self.__select_level_menu)

    def set_researches_menu(self) -> None:
        self.__app.show_view(self.__research_menu)

    def set_level1_screen(self) -> None:
        self.__app.show_view(self.__level1_screen)
