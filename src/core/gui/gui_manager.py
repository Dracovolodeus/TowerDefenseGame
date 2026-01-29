from core.gui.views.start import StartView
from arcade import Window

from core.images.texture_pool import TexturePool


class GUIManager:
    def __init__(self, app: Window, texture_pool: TexturePool) -> None:
        self.__app = app
        self.__texture_pool = texture_pool
        self.__start_menu = StartView(self, self.__texture_pool)

    def set_start_menu(self) -> None:
        self.__app.show_view(self.__start_menu)

    def set_level_selection_menu(self) -> None:
        print("Нужно реализовать эту менюшку")  # TODO Меню выбора уровня

    def set_researches_menu(self) -> None:
        print("Нужно реализовать эту менюшку")  # TODO Меню исследований
