from o_19_alkalom_12_16.hf.damage.Damage import Damage
from o_19_alkalom_12_16.hf.heroes.Hero import Hero


class Warrior(Hero):
    def __init__(self, name: str, hp: int, level: int):
        super().__init__(name, hp, level)
        self.damage = Damage((10, 20), self.level)

    def attack(self) -> int:
        damage = self.damage.calculate_damage()
        print(f'{self.name} attacks with a sword, dealing {damage} damage!')
        return damage