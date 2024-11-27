# Ősosztály
class Ember:
    def __init__(self, nev, eletkor):
        self.nev = nev
        self.eletkor = eletkor

    def bemutatkozik(self):
        print(f"Név: {self.nev}, Életkor: {self.eletkor}")


# Tanár osztály (Ember leszármazott)
class Tanar(Ember):
    def __init__(self, nev, eletkor, tantargy):
        super().__init__(nev, eletkor)
        self.tantargy = tantargy
        self.osztaly = None

    def osztalyt_kap(self, osztaly):
        self.osztaly = osztaly

    def bemutatkozik(self):
        super().bemutatkozik()
        print(f"Tantárgy: {self.tantargy}")
        if self.osztaly:
            print(f"Tanít az osztályban: {self.osztaly}")


# Diák osztály (Ember leszármazott)
class Diak(Ember):
    def __init__(self, nev, eletkor):
        super().__init__(nev, eletkor)
        self.osztalyzatok = []
        self.osztaly = None

    def add_grade(self, grade):
        self.osztalyzatok.append(grade)

    def average(self):
        if len(self.osztalyzatok) == 0:
            return 0
        return sum(self.osztalyzatok) / len(self.osztalyzatok)

    def set_osztaly(self, osztaly):
        self.osztaly = osztaly

    def bemutatkozik(self):
        super().bemutatkozik()
        if self.osztaly:
            print(f"Osztály: {self.osztaly}")
        print(f"Osztályzatok: {self.osztalyzatok}")
        print(f"Átlag: {self.average():.2f}")


# Osztály osztály
class Osztaly:
    def __init__(self, nev):
        self.nev = nev
        self.diakok = []
        self.tanarok = []

    def add_diak(self, diak):
        self.diakok.append(diak)
        diak.set_osztaly(self.nev)

    def add_tanar(self, tanar):
        self.tanarok.append(tanar)
        tanar.osztalyt_kap(self.nev)

    def osztaly_info(self):
        print(f"Osztály: {self.nev}")
        print("Tanár(ok):")
        for tanar in self.tanarok:
            print(f" - {tanar.nev} (tantárgy: {tanar.tantargy})")
        print("Diák(ok):")
        for diak in self.diakok:
            print(f" - {diak.nev} ({diak.eletkor} éves), Osztályzatok: {diak.osztalyzatok}, Átlag: {diak.average():.2f}")


# Teszt program
def main():
    # Osztály létrehozása
    osztaly = Osztaly("10.A")

    # Tanár létrehozása
    tanar = Tanar("Nagy Péter", 40, "Matematika")
    osztaly.add_tanar(tanar)

    # Diákok létrehozása
    diak1 = Diak("Kovács Anna", 16)
    diak1.add_grade(5)
    diak1.add_grade(4)
    diak1.add_grade(3)
    osztaly.add_diak(diak1)

    diak2 = Diak("Szabó László", 17)
    diak2.add_grade(4)
    diak2.add_grade(5)
    osztaly.add_diak(diak2)

    # Osztály információk megjelenítése
    osztaly.osztaly_info()


if __name__ == "__main__":
    main()


