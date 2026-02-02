import arcade

class PlayGUI:
    def __init__(self, health):
        self.cur_health = health
        self.max_health = health


    def draw_hp(self):
        arcade.draw_line(300, 10, 1000 * (self.cur_health / self.max_health), 10, arcade.color.GREEN, 10)
        arcade.draw_line(1000 * (self.cur_health / self.max_health), 10, 1000, 10, arcade.color.RED, 10)
    """
    TODO Сделать логику отрисовки GUI во время игры.
    Тебе нужно сделать:
    1) Отрисовку ХП (из self.health в Level) ---> ГОТОВО!!!!!!!!!!!
    2) Кликабельность платформ (core/play/components/level/какае-то_директория/platform.py ---> НЕ ГОТОВО!!!!!!!!!!!
    Чтобы когда тыкаешь на нее ЛКМ вылазила менюшка с выбором башни. Менюшку пиши тут, вызывай методом, желательно сделать проверку на деньгу
    """
