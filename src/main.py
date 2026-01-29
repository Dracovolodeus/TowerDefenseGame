from core.game_manager import GameManager
from config import settings
import arcade


class App(arcade.Window):
    def __init__(self):
        super().__init__(
            settings.screen.width, settings.screen.height, settings.screen.title
        )
        self.game = GameManager(self)
        self.game.gui.set_start_menu()


def main():
    app = App()
    arcade.run()


if __name__ == "__main__":
    main()
