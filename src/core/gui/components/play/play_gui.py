import arcade

import config as cfg


class PlayGUI:
    def __init__(self, health):
        self.cur_health = health
        self.max_health = health

    def draw_hp(self):
        arcade.draw_line(
            300,
            10,
            1000 * (self.cur_health / self.max_health),
            10,
            arcade.color.GREEN,
            10,
        )
        arcade.draw_line(
            max(300, 1000 * (self.cur_health / self.max_health)),
            10,
            1000,
            10,
            arcade.color.RED,
            10,
        )

    def draw_menu(self):
        arcade.draw_lbwh_rectangle_filled(
            cfg.settings.screen.width - 600,
            0,
            600,
            cfg.settings.screen.height,
            arcade.color.DARK_BLUE,
        )

    """
    TODO Сделать логику отрисовки GUI во время игры.
    Тебе нужно сделать:
    2) Кликабельность платформ (core/play/components/level/какае-то_директория/platform.py ---> НЕ ГОТОВО!!!!!!!!!!!
    Чтобы когда тыкаешь на нее ЛКМ вылазила менюшка с выбором башни. Менюшку пиши тут, вызывай методом, желательно сделать проверку на деньгу
    """
