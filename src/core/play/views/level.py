import arcade

import config as cfg
from core.gui.components.play.play_gui import PlayGUI
from core.gui.views.base import BaseView
from core.images.texture_pool import TexturePool
from core.play.components.level.map import LevelMap
from core.play.managers.bullet import BulletManager
from core.play.managers.enemy import EnemyManager
from core.play.managers.turret import TurretsManager


class Level(BaseView):
    def __init__(self, gui_manager, texture_pool: TexturePool, level_number: int):
        super().__init__(gui_manager, texture_pool)
        self.show_menu = False
        self.level_map = LevelMap(texture_pool, level_number)

        self.__bullet_manager = BulletManager()
        self.__enemy_manager = EnemyManager(
            level=self,
            texture_pool=texture_pool,
            route=self.level_map.get_path(),
            position=self.level_map.get_portal_position(),
        )
        self.__turrets_manager = TurretsManager(
            texture_pool, enemy_manager=self.__enemy_manager, bullet_manager=self.__bullet_manager
        )

        self.__wave_time_counter = 0
        self.__wave_gen_alive = False
        self.__wave_delta_time = self.level_map.get_wave_delta()
        self.health = cfg.settings.level.health
        self.turrets_positions = {}
        self.current_wave = 0
        self.__research_money = 0

        self.level_gui = PlayGUI(cfg.settings.level.health, self.skip_wave_cooldown, gui_manager)

    def setup_widgets(self) -> None:
        if not self._widgets_initialized:
            self._widgets_initialized = True
            self._manager.add(self.level_gui.manager)
            self._manager.add(self.level_gui.menu_manager)
            self._manager.add(self.level_gui.loose_manager)

    def on_show_view(self):
        self.setup_widgets()
        self._manager.enable()

    def on_hide_view(self):
        self._manager.disable()

    def on_mouse_press(
        self, x: int, y: int, button: int, modifiers: int
    ) -> bool | None:
        if self.level_gui.manager.on_mouse_press(x, y, button, modifiers):
            return

        if button == arcade.MOUSE_BUTTON_LEFT:
            pressed_tile = arcade.get_sprites_at_point(
                (x, y), self.level_map.get_platform_tiles()
            )
            if pressed_tile:
                self.level_gui.curr_position = (
                    pressed_tile[0].center_x,
                    pressed_tile[0].center_y,
                )
                self.show_menu = True
            else:
                self.show_menu = False
        if button == arcade.MOUSE_BUTTON_RIGHT:
            pressed_tile = arcade.get_sprites_at_point(
                (x, y), self.level_map.get_platform_tiles()
            )
            if (
                pressed_tile
                and (pressed_tile[0].center_x, pressed_tile[0].center_y)
                in self.turrets_positions
            ):
                position = (pressed_tile[0].center_x, pressed_tile[0].center_y)
                self.sell_tower(position),
                del self.turrets_positions[position]

    def on_draw(self) -> None:
        self.clear()
        self.level_map.draw()
        self.__enemy_manager.draw()
        self.__turrets_manager.draw_bases()
        self.__bullet_manager.draw()
        self.__turrets_manager.draw_towers()
        self.level_gui.draw_hp()
        self.level_gui.manager.draw()
        if self.show_menu and not self.level_gui.is_paused:
            arcade.draw_texture_rect(
                arcade.load_texture(self.level_gui.backgroundPath),
                arcade.XYWH(
                    cfg.settings.screen.width - 250,
                    cfg.settings.screen.height // 2,
                    500,
                    cfg.settings.screen.height,
                ),
            )
            self.level_gui.menu_manager.draw()
        if self.level_gui.is_paused:
            arcade.draw_lbwh_rectangle_filled(
                0,
                0,
                cfg.settings.screen.width,
                cfg.settings.screen.height,
                (0, 0, 0, 128),
            )
        if self.level_gui.loose_manager._enabled:
            self.level_gui.loose_manager.draw()

    def __spawn_enemies_if_need(self, delta_time: float) -> None:
        if self.__wave_gen_alive:
            self.__wave_gen_alive = self.__wave_gen.send(delta_time)
        elif self.__wave_time_counter >= self.__wave_delta_time:
            self.__set_wave_gen()
        else:
            self.__wave_time_counter += delta_time

    def on_update(self, delta_time: float) -> bool | None:
        if not self.level_gui.is_paused and self.health != 0:
            self.__spawn_enemies_if_need(delta_time)
            self.__enemy_manager.update(delta_time)
            self.__bullet_manager.update()
            self.__turrets_manager.update(delta_time)

            if (
                self.level_gui.turret_placed is not None
                and self.level_gui.curr_position not in self.turrets_positions
            ):
                self.add_turret(
                    self.level_gui.turret_placed, self.level_gui.curr_position
                )
                self.turrets_positions[self.level_gui.curr_position] = (
                    self.level_gui.turret_placed
                )
            self.level_gui.turret_placed = None

    def deal_damage(self, value: int = 1) -> None:
        self.health -= value if self.health - value >= 0 else self.health
        self.level_gui.cur_health = self.health
        if self.health == 0:
            self.level_gui.manager.disable()
            self.level_gui.loose_manager.enable()
            self.level_gui.is_paused = True
            cfg.settings.save.money += self.__research_money
            cfg.settings.save.save()

    def __set_wave_gen(self, need_next: bool = True) -> None:
        self.current_wave += 1
        self.level_gui.set_wave(self.current_wave)
        self.__wave_gen = self.level_map.next_wave(self.__enemy_manager.add_enemy)
        self.__wave_gen_alive = True
        self.__wave_time_counter = 0
        if need_next:
            next(self.__wave_gen)

    def add_turret(self, name, position):
        if self.level_gui.can_be_buyed(name):
            self.__turrets_manager.add_turret(name, position)

    def sell_tower(self, position):
        self.__turrets_manager.delete_turrets(position)
        self.level_gui.sell_turret(self.turrets_positions[position])

    def skip_wave_cooldown(self, event=None):
        if not self.__wave_gen_alive:
            self.__set_wave_gen()
