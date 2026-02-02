from dataclasses import dataclass


@dataclass
class EnemyInfo:
    type: str
    frequency: int
    health: float
    gain_speed_step: float | None
    gain_speed_value: float | None
    gain_speed_count: float | None
    gain_health_step: float | None
    gain_health_value: float | None
    gain_health_count: float | None
