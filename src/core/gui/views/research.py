import arcade
from arcade.gui import (
    UIManager, UIBoxLayout, UIAnchorLayout
)

from core.gui.components.ResearchButton import ResearchButton

"""Я когда зашел в репо я чет, скажем 'удивился', как на самом деле пишутся игры,
 а не эти ТУПЫЕ ЗАДАЧИ КОТОРЫЕ У МЕНЯ НЕ ПРОХОДЯТ"""



class ResearchView(arcade.View):
    def __init__(self):
        super().__init__()

        self.anchor_layout = UIAnchorLayout()
        self.ui_manager = UIManager()

    def on_show_view(self):
        self.ui_manager.enable()
        box = UIBoxLayout(spacing=15)

        box.add(
            ResearchButton(
                research_id="research_1",
                text="Исследование I",
                width=260
            )
        )

        box.add(
            ResearchButton(
                research_id="research_2",
                text="Исследование II",
                width=260
            )
        )

        box.add(
            ResearchButton(
                research_id="research_3",
                text="Исследование III",
                width=260
            )
        )

        self.anchor_layout.add(box)

        self.ui_manager.add(self.anchor_layout)

    def on_hide_view(self):
        self.ui_manager.disable()

    def on_draw(self):
        self.clear()
        self.ui_manager.draw()
