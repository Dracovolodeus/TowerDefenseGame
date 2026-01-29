import json
from pathlib import Path


class JSONProcessor:
    @staticmethod
    def write(data: list | dict, path: Path) -> None:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, sort_keys=True)

    @staticmethod
    def read(path: Path) -> dict | list:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
