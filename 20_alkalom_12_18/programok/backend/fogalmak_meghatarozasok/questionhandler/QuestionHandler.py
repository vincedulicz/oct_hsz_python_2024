from o_20_alkalom_12_18.backend.fogalmak_meghatarozasok.definitonprovider.DefinitonProvider import DefinitonProvider


class QuestionHandler:
    """ A kérdések kezelésért felelős osztály """

    def __init__(self, definiton_provider: DefinitonProvider):
        self.definiton_provider = definiton_provider

    def ask_question(self):
        meghatarozas, correct_fogalom = self.definiton_provider.get_definition()
        print(f'\n(END/Q/QUIT) Meghatározás: {meghatarozas}')
        valasz = input("Melyik fogalom társul ehhez? : ").strip()

        return valasz, correct_fogalom