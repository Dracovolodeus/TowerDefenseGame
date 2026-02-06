from pathlib import Path

from utils.json_func import JSONProcessor


class Save:
    def __init__(self, path: Path) -> None:
        self.path = path
        save: dict = JSONProcessor.read(self.path)
        self.money = save["money"]
        self.have_saved_game: bool = save["have_saved_game"]
        self.first_level_records: int = save["first_level_records"]
        self.second_level_records: int = save["second_level_records"]
        self.third_level_records: int = save["third_level_records"]
        self.fourth_level_records: int = save["fourth_level_records"]
        self.fifth_level_records: int = save["fifth_level_records"]

        self.turret_speed: int = save["turret_speed"]
        self.turret_damage: int = save["turret_damage"]
        self.turret_distans: int = save["turret_distans"]

    def save(self) -> None:
        JSONProcessor.write(
            {
                "money": self.money,
                "have_saved_game": self.have_saved_game,
                "first_level_records": self.first_level_records,
                "second_level_records": self.second_level_records,
                "third_level_records": self.third_level_records,
                "fourth_level_records": self.fourth_level_records,
                "fifth_level_records": self.fifth_level_records,
                "turret_speed": self.turret_speed,
                "turret_damage": self.turret_damage,
                "turret_distans": self.turret_distans,
            },
            self.path,
        )
