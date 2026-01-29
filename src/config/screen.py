from dataclasses import dataclass


@dataclass
class Screen:
    width: int = 1500
    height: int = 875
    title: str = "TWGame"
