from pathlib import Path

from utils.json_func import JSONProcessor


class Save:
    def __init__(self, path: Path) -> None:
        self.path = path
        saves: dict = JSONProcessor.read(self.path)
        self.have_saved_game: bool = saves["have_saved_game"]

    def save(self) -> None:
        JSONProcessor.write({"have_saved_game": self.have_saved_game}, self.path)
