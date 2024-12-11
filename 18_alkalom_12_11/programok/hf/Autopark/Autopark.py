import json
from o_18_alkalom_12_11.hf.Jarmuvek.Szemelygepkocsi import Szemelygepkocsi
from o_18_alkalom_12_11.hf.Jarmuvek.Teherauto import Teherauto
from o_18_alkalom_12_11.hf.Jarmuvek.Jarmu import Jarmu


class Autopark:
    def __init__(self):
        self.jarmuvek = []

    def jarmu_hozzadas(self, jarmu: Jarmu) -> None:
        self.jarmuvek.append(jarmu)

    def jarmu_eltavolitasa(self, jarmu: Jarmu) -> None:
        if jarmu in self.jarmuvek:
            self.jarmuvek.remove(jarmu)

    def osszes_jarmu(self) -> list[dict]:
        return [j.jarmu_adatok() for j in self.jarmuvek]

    def mentes_fajlba(self, fajlnev):
        adatok = self.osszes_jarmu()

        with open(fajlnev, 'w', encoding='utf-8') as file:
            json.dump(adatok, file, ensure_ascii=False, indent=4)

    def betoltes_fajlbol(self, fajlnev):
        try:
            with open(fajlnev, 'r', encoding='utf-8') as file:
                jarmu_lista = json.load(file)
                for j in jarmu_lista:
                    if "ajtok_szama" in j:
                        self.jarmu_hozzadas(
                            Szemelygepkocsi(
                                tipus=j["tipus"],
                                gyarto=j["gyarto"],
                                evjarat=j["evjarat"],
                                motor=j.get("motor_tipus"),
                                kerekek=j.get("kerekek_szama"),
                                ajtok_szama=j["ajtok_szama"]
                            )
                        )
                    elif "teherbiras" in j:
                        self.jarmu_hozzadas(
                            Teherauto(
                                tipus=j["tipus"],
                                gyarto=j["gyarto"],
                                evjarat=j["evjarat"],
                                motor=j.get("motor_tipus"),
                                kerekek=j.get("kerekek_szama"),
                                teherbiras=j["teherbiras"]
                            )
                        )
        except FileNotFoundError:
            print(f'A {fajlnev} nem található.')


