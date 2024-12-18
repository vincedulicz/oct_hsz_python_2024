from random import choice

from o_20_alkalom_12_18.backend.fogalmak_meghatarozasok.definitonprovider.DefinitonProvider import DefinitonProvider


class DefinitonDict(DefinitonProvider):
    """ A fogalmak és meghatározások tárolása & kezelése"""

    def __init__(self, fogalmak, meghatarozasok):
        self.fogalmak = fogalmak
        self._meghatarozasok = meghatarozasok
        self._dictionary = self._create_dictionary()

    def _create_dictionary(self):
        return {meghatarozas: fogalom for fogalom, meghatarozas in zip(self.fogalmak, self._meghatarozasok)}

    def get_definition(self):
        meghatarozas = choice(list(self._dictionary.keys()))
        return meghatarozas, self._dictionary[meghatarozas]

    def check_answear(self, user_answear: str, correct_answear: str) -> bool:
        return user_answear.strip().lower() == correct_answear.strip().lower()