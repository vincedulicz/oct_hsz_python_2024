""" I. feladat """

def szokoev(ev):
    return ev % 400 == 0 or (ev % 4 == 0 and ev % 100 != 0)


def evnapja(ev, honap, nap):
    honapok = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # hónapok összege
    napszam = 0
    i = 0
    while i < honap - 1:
        napszam += honapok[i]
        i += 1
    # +1, ha szökőév és február eltelt
    if szokoev(ev) and honap > 2:
        napszam += 1
    # az adott hónap napja
    napszam += nap

    return napszam


def main():
    ev = int(input("Kerem az évet: "))
    honap = int(input("Kerem a hónapot: "))
    nap = int(input("Kerem a napot: "))

    n = evnapja(ev, honap, nap)
    print(f"{ev}.{honap}.{nap}. az év {n}. napja")


# main()



""" II. feladat """

def szoveget_elemez(szoveg):
    eredmeny = {"betu": 0, "szamjegy": 0, "egyeb": 0}   # Kitöltjük kezdőértékekkel az eredmény dictionary-t

    for karakter in szoveg:                 # Bejárjuk a paraméterben kapott szöveg karaktereit
        if karakter.isalpha():              # Minden betű esetén növeljük a "betu" kulcshoz tartozó értéket
            eredmeny["betu"] += 1
        elif karakter.isdigit():            # Minden számjegy esetén növeljük a "szamjegy" kulcshoz tartozó értéket
            eredmeny["szamjegy"] += 1
        else:                               # Egyéb karakterek esetén az "egyeb" kulcshoz tartozó értéket növeljük
            eredmeny["egyeb"] += 1

    return eredmeny

# print(szoveget_elemez("te8d7fdfkd!!!kdlg@VVV"))


""" III. feladat """

def kurzuskodot_csoportosit(kurzuskodok):
    if kurzuskodok == "":                   # Ha a paraméter az üres string, akkor egy üres dictionary-vel térünk vissza
        return {}

    kurzuskod_lista = kurzuskodok.split(";")    # A pontosvesszővel elválasztott kurzuskódokat eltároljuk egy listában
    eredmeny = {"infos": [], "matekos": [], "szabval": []}  # Kitöltjük kezdőértékekkel az eredmény dictionary-t

    for kurzuskod in kurzuskod_lista:       # Minden kurzuskódot a megfelelő kulcshoz tartozó listába szúrunk be
        if kurzuskod.startswith("I"):       # Az `I` betűvel kezdődő kurzuskódok az infós tárgyakhoz tartoznak
            eredmeny["infos"].append(kurzuskod)
        elif kurzuskod.startswith("M"):     # Az `M` betűvel kezdődő kurzuskódok a matekos tárgyakhoz tartoznak
            eredmeny["matekos"].append(kurzuskod)
        elif kurzuskod.startswith("X"):     # Az `X` betűvel kezdődő kurzuskódok a szabválokhoz tartoznak
            eredmeny["szabval"].append(kurzuskod)

    return eredmeny

# print(kurzuskodot_csoportosit("IB370G;MBNXK114E;MBNXK114G;XA0021-GTK-MM1;IB370E"))



""" IV. feladat """

def statisztika(fajlok):
    eredmeny = {}                       # A kiterjesztéseket nem tudjuk előre, így egy üres dictionary-ből indulunk ki

    for fajl in fajlok:                 # Bejárjuk a paraméterben kapott listában szereplő fájlokat
        kit = fajl.split(".")[-1]       # A kiterjesztés a legutolsó pont után lévő string
        kit = kit.lower()               # A kis- és nagybetűket nem különböztetjük meg a kiterjesztések esetén

        if kit not in eredmeny:         # Ha az adott kiterjesztés még nem szerepel kulcsként a dictionary-ben...
            eredmeny[kit] = 1           # ...beszúrjuk 1-es kezdőértékkel (hiszen most látjuk először)
        else:                           # Ha pedig már szerepel a kiterjesztés a dictionary kulcsai között...
            eredmeny[kit] += 1          # ...megnöveljük a hozzá tartozó előfordulási értéket 1-gyel

    return eredmeny


print(statisztika(['feladat.py', 'Bolygo.java', 'HELLOFRIENDS.MP4', 'TEST.PY', 'biro.gib.maxpont.py', 'russian-driving-fails.mp4']))