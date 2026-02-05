from dataclasses import dataclass


@dataclass
class LevelValues:
    health: int = 20
    wave_delta_time: int = 10 # In seconds
