from abc import ABC, abstractmethod
from o_19_alkalom_12_16.hf.damage.Damage import Damage


class Hero(ABC):
    def __init__(self, name: str, hp: int, level: int):
        self.name: str = name
        self._hp: int = hp
        self.level: int = level
        self._damage: Damage = None

    @abstractmethod
    def attack(self) -> int:
        pass

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f'{self.name} has {self.hp} HP left\n')

    def is_alive(self) -> bool:
        return self.hp > 0

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = max(0, value)

    @property
    def damage(self) -> Damage:
        return self._damage

    @damage.setter
    def damage(self, value: Damage) -> None:
        self._damage = value

    def __str__(self) -> str:
        return f'{self.name} - HP: {self.hp}, level: {self.level}'

    def __repr__(self) -> str:
        return f'Hero(name={self.name}, hp={self.hp}, Level: {self.level})'
