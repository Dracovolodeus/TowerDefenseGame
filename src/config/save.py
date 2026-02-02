from pathlib import Path

from utils.json_func import JSONProcessor


class Save:
    def __init__(self, path: Path) -> None:
        self.path = path
        save: dict = JSONProcessor.read(self.path)
        self.have_saved_game: bool = save["have_saved_game"]
        self.first_level_records = save["first_level_records"]
        self.second_level_records = save["second_level_records"]
        self.third_level_records = save["third_level_records"]
        self.fourth_level_records = save["fourth_level_records"]
        self.fifth_level_records = save["fifth_level_records"]

    def save(self) -> None:
        JSONProcessor.write(
            {
                "have_saved_game": self.have_saved_game,
                "first_level_records": self.first_level_records,
                "second_level_records": self.second_level_records,
                "third_level_records": self.third_level_records,
                "fourth_level_records": self.fourth_level_records,
                "fifth_level_records": self.fifth_level_records,
            },
            self.path,
        )
