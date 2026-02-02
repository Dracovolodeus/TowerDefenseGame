from dataclasses import dataclass


@dataclass
class Screen:
    width: int = 1536
    height: int = 896
    title: str = "TWGame"
