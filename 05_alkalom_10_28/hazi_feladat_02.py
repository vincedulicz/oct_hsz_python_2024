import random

# Alap adatok
TANULOK = [
    {"nev": "Teszt Elek", "osztaly": "13I", "eletkor": 19},
    {"nev": "Kiss Béla", "osztaly": "12A", "eletkor": 18},
    {"nev": "Nagy Anna", "osztaly": "11B", "eletkor": 17},
    {"nev": "Szabó Gergő", "osztaly": "10C", "eletkor": 16},
    {"nev": "Varga László", "osztaly": "9D", "eletkor": 15},
    {"nev": "Tóth Zsófia", "osztaly": "12A", "eletkor": 18}
]

OSZTALYOK = ["9A", "10B", "11C", "12D", "13I"]


# 0. Többször is kell :)
def get_tanulo_ertek_by_nev(nev):
    """ Tanuló összes adata """

    """for tanulo in TANULOK:
        if tanulo["nev"] == nev:
            return tanulo"""

    return next(tanulo for tanulo in TANULOK if tanulo["nev"] == nev)


# 1. Összes tanuló kiírása
def kiir_tanulok():
    """ Kiírja a tanulókat formázottan list comp.-al """

    print("A jelenlegi tagok:")

    for index, tanulo in enumerate(TANULOK, start=1):
        print(f"{index}. {tanulo['nev']} {tanulo['eletkor']} éves és a {tanulo['osztaly']} osztályba jár.")

    """[print(f"{index}. {tanulo['nev']} {tanulo['eletkor']} éves és a {tanulo['osztaly']} osztályba jár.")
     for index, tanulo in enumerate(TANULOK, start=1)]"""


# 2. Új tanuló hozzáadása
def uj_tanulo():
    nev = input("Add meg az új tag nevét: ")
    eletkor = int(input("Add meg az életkort: "))

    osztaly = random.choice(OSZTALYOK)  # Véletlen osztály kiválasztása

    TANULOK.append({"nev": nev, "osztaly": osztaly, "eletkor": eletkor})

    print(f"Új tag hozzáadva: {nev}, {eletkor} éves, {osztaly} osztály.")


# 3. Tanuló törlése
def tanulo_torlese():
    nev = input("Add meg a törlendő tag nevét: ")

    talalat = get_tanulo_ertek_by_nev(nev)
    print(talalat)

    if talalat:
        megerosites = input("Biztosan törölni szeretnéd? (I/N): ")
        if megerosites.lower() == "i":
            TANULOK.remove(talalat)
            print(f"{nev} törölve lett a listából.")
        else:
            print("A törlés visszavonva.")
    else:
        print("Nem található ilyen nevű tag.")


# 4. Tanuló adatainak módosítása
def tanulo_modositasa():
    nev = input("Add meg a módosítani kívánt tag nevét: ")

    talalat = get_tanulo_ertek_by_nev(nev)
    if talalat:
        kulcs = input("Melyik adatot szeretnéd módosítani? (nev, osztaly, eletkor): ")

        if kulcs in talalat:
            uj_ertek = input(f"Add meg az új értéket a(z) '{kulcs}' mezőhöz: ")

            if kulcs == "eletkor":
                uj_ertek = int(uj_ertek)  # Az életkort számmá konvertáljuk

            talalat[kulcs] = uj_ertek

            print(f"{nev} {kulcs} értéke módosítva lett: {uj_ertek}.")
        else:
            print("Érvénytelen kulcs.")
    else:
        print("Nem található ilyen nevű tag.")


# 5. Program főciklusa
def main():
    while True:
        print(
            "Az alábbi parancsokat használhatod:"
            "\nÚj tag - newmem | Törlés - delete | Módosítás - modify | Kilépés - end, Q, quit"
        )

        kiir_tanulok()

        parancs = input("Mit szeretne csinálni? ").strip().lower()
        if parancs in ["q", "end", "quit"]:
            print("A program leáll.")
            break
        elif parancs == "newmem":
            uj_tanulo()
        elif parancs == "delete":
            tanulo_torlese()
        elif parancs == "modify":
            tanulo_modositasa()
        else:
            print("Érvénytelen parancs. Próbáld újra.")


# Program futtatása
main()
