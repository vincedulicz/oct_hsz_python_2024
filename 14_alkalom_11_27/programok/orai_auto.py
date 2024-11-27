# 1. Osztály létrehozása
class Auto:
    # Osztályváltozó (minden példány közösen osztja)
    gyartok = ["Toyota", "BMW", "Tesla"]

    def __init__(self, marka, modell, evjarat):
        # Példányváltozók (csak az adott objektumhoz tartoznak)
        self.marka = marka
        self.modell = modell
        self.evjarat = evjarat
        self.__km_ora = 0  # Private változó (kettős aláhúzás)

    # Public metódus
    def info(self):
        return f"{self.evjarat} {self.marka} {self.modell}, {self.__km_ora} km-rel."

    # Private metódus
    def __titkos_ugras(self):
        print(f"{self.marka} gyorsan ugrik előre!")

    # Védett (protected) metódus
    def _novenyesitett_ora(self):
        self.__km_ora += 10

    # Setter metódus a private változóhoz
    def uj_km(self, km):
        if km > self.__km_ora:
            self.__km_ora = km
        else:
            print("Nem állíthatod vissza az órát!")

    # Osztálymetódus
    @classmethod
    def gyartok_listaja(cls):
        return cls.gyartok

    # Statikus metódus
    @staticmethod
    def uzemanyag_koltseg(km, liter_ar):
        return km * 0.06 * liter_ar


# 2. Példány létrehozása
auto1 = Auto("Toyota", "Corolla", 2015)

# Public metódus meghívása
print(auto1.info())

# Setter használata private változóhoz
auto1.uj_km(15000)
print(auto1.info())

# Protected metódus használata
auto1._novenyesitett_ora()
print(auto1.info())

# Private metódus direkt elérése nem lehetséges:
# auto1.__titkos_ugras()  # Ez hibát okoz!

# Osztálymetódus hívása
print("Elérhető gyártók:", Auto.gyartok_listaja())

# Statikus metódus hívása
print("Üzemanyag költség 1000 km-re:", Auto.uzemanyag_koltseg(1000, 480), "Ft")
