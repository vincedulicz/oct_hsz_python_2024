from o_19_alkalom_12_16.hf.battle.Battle import Battle
from o_19_alkalom_12_16.hf.character_datamanager.CharacterDataManager import CharacterDataManager
from o_19_alkalom_12_16.hf.heroes import Hero
from o_19_alkalom_12_16.hf.heroes.Archer import Archer
from o_19_alkalom_12_16.hf.heroes.Mage import Mage
from o_19_alkalom_12_16.hf.heroes.Warrior import Warrior


def main() -> None:
    file_manager = CharacterDataManager('characters.json')

    file_manager.add_character("Thor", "Warrior", 120, 8)
    file_manager.add_character("Merlin", "Mage", 85, 5)

    characters_data = file_manager.read_data()
    heroes: list[Hero] = []

    for character in characters_data:
        if character['type'] == 'Warrior':
            heroes.append(
                Warrior(
                    character['name'],
                    character['hp'],
                    character['level'])
            )
        elif character['type'] == 'Mage':
            heroes.append(
                Mage(
                    character['name'],
                    character['hp'],
                    character['level'])
            )
        elif character['type'] == 'Archer':
            heroes.append(
                Archer(
                    character['name'],
                    character['hp'],
                    character['level'])
            )

    battle = Battle(heroes[0], heroes[1])
    battle.start_battle()


if __name__ == "__main__":
    main()
