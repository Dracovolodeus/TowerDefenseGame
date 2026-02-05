from dataclasses import dataclass


@dataclass
class EnemyInfo:
    type: str
    health: int | float
    speed: int | float
    gain_speed_step: float | int | None
    gain_speed_value: float | int | None
    gain_speed_count: float | int | None
    gain_health_step: float | int | None
    gain_health_value: float | int | None
    gain_health_count: float | int | None
