from o_19_alkalom_12_16.hf.heroes.Hero import Hero


class Battle:
    def __init__(self, hero: Hero, hero_other: Hero):
        if isinstance(hero, Hero) and isinstance(hero_other, Hero):
            self.hero: Hero = hero
            self.hero_other: Hero = hero_other
        else:
            raise NotImplementedError(f'Wrong type: {Hero} only')

    def start_battle(self):
        print(f'Battlen between {self.hero.name} and {self.hero_other.name}')

        while self.hero.is_alive() and self.hero_other.is_alive():
            self.hero_other.take_damage(
                self.hero.attack()
            )

            if self.hero_other.is_alive():
                self.hero.take_damage(
                    self.hero_other.attack()
                )

        if self.hero.is_alive():
            print(f'{self.hero.name} wins!')
        else:
            print(f'{self.hero_other.name} wins!')