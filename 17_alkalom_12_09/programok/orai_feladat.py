import json
import re
from abc import ABC, abstractmethod


class Allat(ABC):
    def __init__(self, nev, faj, kor):
        self.nev = nev
        self.faj = faj
        self.kor = kor

    @abstractmethod
    def hangot_ad(self):
        pass

    @abstractmethod
    def allat_adatok(self):
        pass

    def __str__(self):
        return f'{self.faj} - {self.nev}'


class Emlos(Allat):
    def __init__(self, nev, kor, szoros_fajta):
        super().__init__(nev, "Emlős", kor)
        self.szoros_fajta = szoros_fajta

    def __str__(self):
        return f'emlős: {self.nev}'

    def hangot_ad(self):
        return f'{self.nev} emlős hangot ad: ugat'

    def allat_adatok(self):
        return {
            "nev": self.nev,
            "faj": self.faj,
            "kor": self.kor,
            "szoros_fajta": self.szoros_fajta
        }


class Madar(Allat):
    def __init__(self, nev, kor, repul_kepes):
        super().__init__(nev, "Madár", kor)
        self.repul_kepes = repul_kepes

    def hangot_ad(self):
        return f'{self.nev} madár károg'

    def allat_adatok(self):
        return {
            "nev": self.nev,
            "faj": self.faj,
            "kor": self.kor,
            "repul_kepes": self.repul_kepes
        }


class Hullo(Allat):
    def __init__(self, nev, kor, merges):
        super().__init__(nev, "Hüllő", kor)
        self.merges = merges

    def hangot_ad(self):
        return f'{self.nev} hüllő sziszeg'

    def allat_adatok(self):
        return {
            "nev": self.nev,
            "faj": self.faj,
            "kor": self.kor,
            "merges": self.merges
            }


class Allatkert:
    def __init__(self):
        self._allatok = []

    @property
    def allatok(self):
        return self._allatok

    def __iadd__(self, allat):
        self.allatok.append(allat)
        return self

    def allat_eltavolitas(self, allat):
        if allat in self.allatok:
            self.allatok.remove(allat)

    def osszes_allat(self):
        return [allat.allat_adatok() for allat in self.allatok]

    def mentes_fajlba(self, fajlnev):
        adatok = self.json_beolvasasa(fajlnev)
        adatok.extend(self.osszes_allat())

        with open(fajlnev, 'w', encoding='utf-8') as file:
            json.dump(adatok, file, ensure_ascii=False, indent=4)

    def betoltes_fajlbol(self, fajlnev):
        json_adatok = self.json_beolvasasa(fajlnev)

        try:
            for adat in json_adatok:
                if adat["faj"] == "Emlős":
                    self.allatok.append(
                        Emlos(adat["nev"],
                              adat["kor"],
                              adat["szoros_fajta"]))
                elif adat["faj"] == "Madár":
                    self.allatok.append(
                        Madar(adat["nev"],
                              adat["kor"],
                              adat["repul_kepes"]))
                elif adat["faj"] == "Hüllő":
                    self.allatok.append(
                        Hullo(adat["nev"],
                              adat["kor"],
                              adat["merges"]))
        except FileNotFoundError:
            print(f'A {fajlnev} nem található')
        except Exception as e:
            print(f'Hiba: {e}')


    @staticmethod
    def json_beolvasasa(fajlnev):
        try:
            with open(fajlnev, 'r', encoding='utf-8') as file:
                adatok = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f'Hiba: {e}')
            return []

        return adatok


class AllatAdatProcess:
    def __init__(self, allatkert: Allatkert):
        self.allatok = allatkert.allatok

    def kor_alapjan_szures(self, minimalis_kor):
        return [allat for allat in self.allatok if allat.kor >= minimalis_kor]

    def van_e_fajta(self, fajta) -> bool:
        return any(allat.faj == fajta for allat in self.allatok)

    def nevek_keresese(self, minta):
        return [allat.nev for allat in self.allatok if re.search(minta, allat.nev)]

    def faj_keresese(self, minta):
        return [allat.faj for allat in self.allatok if re.search(minta, allat.faj)]

    def osszesitett_kor(self):
        return sum(allat.kor for allat in self.allatok)

    def keres_nev_szerint(self, nev):
        for allat in self.allatok:
            if allat.nev == nev:
                return allat
        return None

    def nevek_betuvel_kezdodnek(self, kezdo_betu):
        return [allat.nev for allat in self.allatok if allat.nev.startswith(kezdo_betu)]

    def faj_szerinti_csoporitas(self):
        csoportok = {}

        for allat in self.allatok:
            if allat.faj not in csoportok:
                csoportok[allat.faj] = []
            csoportok[allat.faj].append(allat.nev)

        return csoportok


if __name__ == "__main__":
    allatkert = Allatkert()

    # állatok hozzáadni

    allatkert += Emlos("cirmos", 2, "rövidszüre")
    allatkert += Madar("harkály", 7, True)
    allatkert += Hullo("kígyó", 6, True)
    allatkert += Emlos("Bodri", 5, "HOSSZÚszürő")
    allatkert += Madar("pingvin", 3, False)

    fajlnev = "allatkert.json"
    allatkert.mentes_fajlba(fajlnev)

    allatkert.betoltes_fajlbol(fajlnev)

    aap = AllatAdatProcess(allatkert)

    print("Állatok az állatkertben:")
    for allat in allatkert.allatok:
        print(allat)


    print("\n3 évnél idősebb állatok:")
    szurt_allatok = aap.kor_alapjan_szures(3)
    for allat in szurt_allatok:
        print(allat)


    if aap.van_e_fajta("Madár"):
        print("van")
    else:
        print("nincs")


    print("Állatok név keresése:")
    c_betu_allatok = aap.nevek_keresese(r"^B")

    for allat in c_betu_allatok:
        print(allat)

