from __future__ import annotations
from random import randint


class Damage:
    def __init__(self, base_damage: tuple[int, int], level: int):
        self.base_damage: tuple[int, int] =  base_damage
        self.level: int = level

    def calculate_damage(self) -> int:
        return randint(self.base_damage[0], self.base_damage[1]) + self.level

    def __str__(self) -> str:
        return f'Damage({self.base_damage[0]} - {self.base_damage[1]} + Level {self.level}'

    def __repr__(self) -> str:
        pass

    def __add__(self, other: Damage) -> Damage:
        if isinstance(other, Damage):
            new_base_damage = (
                self.base_damage[0]
                + other.base_damage[0],
                self.base_damage[1]
                + other.base_damage[1]
            )

            return Damage(new_base_damage, self.level + other.level)
        return NotImplemented