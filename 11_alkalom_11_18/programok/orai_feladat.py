import json

def elso_feladat():
    """ json mentése / betöltése fájlból """

    adat = {"név": "Anna", "kor": 25, "város": "Budapest"}

    with open("jsons/adat.json", "w", encoding="utf-8") as file:
        json.dump(adat, file, indent=4)

    with open("jsons/adat.json", "r", encoding="utf-8") as file:
        betoltott_adat = json.load(file)

    print(f'betöltött adatot: {betoltott_adat}')


def masodik_feladat():
    """ json fájl módosítása """

    with open("jsons/adat.json", "r", encoding='utf-8') as file:
        adat = json.load(file)

    adat["orszag"] = "Magyarország"

    with open("jsons/adat.json", "w", encoding='utf-8') as file:
        json.dump(adat, file, indent=4)

    print("módosított adat: ", adat)


def harmadik_feladat():
    """ számok rendezése """

    with open("jsons/szamok.json", "r") as file:
        szamok = json.load(file)

    szamok.sort()

    with open("jsons/szamok.json", "w") as file:
        json.dump(szamok, file, indent=4)

    print("rendezett számsor: ", szamok)


def negyedik_feladat():
    """" min max """

    with open("jsons/szamok.json", "r") as file:
        szamok = json.load(file)

    print("legnagyobb: ", max(szamok))
    print("legkisebb: ", min(szamok))


def otodik_feladat():
    """ összeg és átlag """

    with open("jsons/pontszamok.json", "r") as file:
        pontszamok = json.load(file)

    osszeg = sum(pontszamok)
    atlag = osszeg / len(pontszamok)

    print(f"összeg: {osszeg} | átlag: {atlag}")


import os

def hatodik_feladt():
    fajl_ut = "jsons/alap.json"

    if not os.path.exists(fajl_ut):
        alap_adat = {"msg": "alap msg"}

        with open(fajl_ut, "w") as file:
            json.dump(alap_adat, file, indent=4)
        print("Alapértelmezett fájl létre lett hozva")
    else:
        with open(fajl_ut, "r") as file:
            adat = json.load(file)
        print(adat)


def hetedik_feladat():
    """ try catch """

    try:
        with open("jsons/hibas_json.json", "r") as file:
            adat = json.load(file)
            print(adat)
    except json.JSONDecodeError as e:
        print(f'hibás adat: {e}')


def nyolcadik_feladat():
    """ eldöntés """

    with open("jsons/felhasznalok.json", "r", encoding='utf-8') as file:
        felhasznalok = json.load(file)

    szurt_adatok = [felh for felh in felhasznalok if felh["kor"] > 30]
    print(szurt_adatok)


def kilencedik_feladat():
    """ txt to json """

    with open("jsons/szavak_50.txt", "r", encoding='utf-8') as file:
        szavak = [sor.strip() for sor in file.readlines()]

    with open("jsons/szavak.json", "w", encoding='utf-8') as file:
        json.dump(szavak, file, indent=4)

    print(szavak)


def tizedik_feladat():
    """ pontszámok kiértékelése """

    fajl_ut = "jsons/pontszamok.json"

    try:
        with open(fajl_ut, "r", encoding='utf-8') as file:
            pontszamok = json.load(file)

            print("legmagasabb pontszám", max(pontszamok))
            print("legalacsonyabb p", min(pontszamok))
            print("átlag", sum(pontszamok) / len(pontszamok))
    except FileNotFoundError:
        alap_pontszamok = [0,0,0]
        with open(fajl_ut, "w") as file:
            json.dump(alap_pontszamok, file, indent=4)
            print("nem létezett a fájl, de létrehoztam: ", alap_pontszamok)

tizedik_feladat()

