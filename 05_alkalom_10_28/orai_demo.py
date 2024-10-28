# Függvény létrehozása
def koszont():
    print("Helló, üdvözöllek!")

# Függvény meghívása
koszont()




import random

mylist = ["apple", "banana", "cherry"]

print(random.choice(mylist))

"""
Visszatérési értékek

A return kulcsszóval visszaadhatunk
egy vagy több értéket a függvényből.
Ha nincs return utasítás,a függvény None-t ad vissza.
"""

def teszt_osszeadas(a):
    a = a + 1
    return a

a = 1
print(teszt_osszeadas(a))

print()

# Egy visszatérési érték
def osszeg(a, b):
    return a + b

eredmeny = osszeg(3, 4)
print(eredmeny)  # 7

# Több visszatérési érték
def muveletek(a, b):
    ossz = a + b
    kulonbseg = a - b

    return ossz, kulonbseg

ossz, kulonbseg = muveletek(10, 5)
print(ossz, kulonbseg)  # 15 5



"""
Argumentumok 

Pythonban argumentumok segítségével adunk át adatokat a függvényeknek.
Ezek lehetnek pozicionális vagy kulcsszavas argumentumok.


Pozicionális Argumentumok
A pozicionális argumentumokat a függvény meghívásakor adott sorrendjük
szerint rendeli hozzá a Python a függvény paramétereihez.

"""

def bemutatkozas(nev, kor):
    print(f"Nevem {nev}, és {kor} éves vagyok.")

# Pozicionális argumentumok használata
bemutatkozas("Anna", 25)


"""
Keyword (kulcsszavas) Argumentumok

A kulcsszavas argumentumok esetén a függvény meghívásakor megadjuk
a paraméter nevét is, így a sorrend nem számít.
"""

# Keyword argumentumok használata
bemutatkozas(kor=25, nev="Anna")
bemutatkozas(kor=66, nev="teszt elek")




"""
Alapértelmezett értékek és opcionális paraméterek

A függvényparaméterekhez alapértelmezett értéket adhatunk meg,
így azok opcionálisan átadhatók a függvény hívásakor.
"""
def koszont(nev, udvozles="Szia"):
    print(f"{udvozles}, {nev}!")

# Az "udvozles" argumentum alapértelmezett értéket kap
koszont("Péter")           # Szia, Péter!
koszont("Péter", "Helló")  # Helló, Péter!
koszont(udvozles="Sziaheló", nev="teszt elek")


"""
Összesítve:
"""

def rendeles_vegosszeg(termek, darab=1, ar=1000, kedvezmeny=0):
    return darab * ar * (1 - kedvezmeny / 100)


# Pozicionális és keyword argumentumokkal
print(rendeles_vegosszeg("Laptop", 2, kedvezmeny=10))  # 1800.0
print(rendeles_vegosszeg("Telefon", darab=3, ar=800))  # 2400.0

print()

"""
Dict
"""

TANULOK = [
    {"nev": "Teszt Elek", "osztaly": "13I", "eletkor": 19},
    {"nev": "Kiss Béla", "osztaly": "12A", "eletkor": 18},
    {"nev": "Nagy Anna", "osztaly": "11B", "eletkor": 17},
    {"nev": "Szabó Gergő", "osztaly": "10C", "eletkor": 16},
    {"nev": "Varga László", "osztaly": "9D", "eletkor": 15},
    {"nev": "Tóth Zsófia", "osztaly": "12A", "eletkor": 18}
]

# Függvény a tanuló adatainak frissítésére
def frissit_tanulo(tanulok, nev, uj_kor=None, uj_osztaly=None):
    for tanulo in tanulok:
        if tanulo["nev"] == nev:
            if uj_kor is not None:
                tanulo["eletkor"] = uj_kor
            if uj_osztaly is not None:
                tanulo["osztaly"] = uj_osztaly
            break

# Példa: Frissítsük "Kiss Béla" adatait
frissit_tanulo(TANULOK, "Kiss Béla", uj_kor=19, uj_osztaly="13A")

print("Frissített lista:", TANULOK)


# Függvény a tanuló törlésére
def torol_tanulo(tanulok, nev):
    for i, tanulo in enumerate(tanulok):
        if tanulo["nev"] == nev:
            del tanulok[i]
            return True
    return False


# Példa: Töröljük "Varga László" nevű tanulót
torol_tanulo(TANULOK, "Teszt Elek")

print("Törlés után:", TANULOK)

print(TANULOK[0].get("nev"))

print()

suti = {"nev": "dobostorta", "szeletek": 12, "elfogyott": False}

# hagyományos indexelés

print(suti["nev"])
# print(suti["laktozmentes"])   # HIBA!!! (nem létező kulcs)

# get() metódus

print(suti.get("nev"))
print(suti.get("laktozmentes"))

print()

# bejárás
for kulcs, ertek in suti.items():
    print(kulcs, "értéke:", ertek)

print()


my_dict = {
    1: "alma",
    2: "körte",
    3: "szilva",
    12: "alma",
    23: "körte",
    32: "szilva",
    41: "alma",
    42: "körte",
    34: "szilva"
}

# Hozzunk létre egy olyan dictionary-t, amely az értékek alapján csoportosítja a dictionary kulcsait!
# Tehát az elvárt output: {'alma': [1, 12, 41], 'körte': [2, 23, 42], 'szilva': [3, 32, 34]}

csoportok = {}
for kulcs, ertek in my_dict.items():
    # Ha létezik az adott csoportnak megfelelő lista, akkor csak beletesszük az új elemet.
    # Ha nincs még ilyen lista, akkor létrehozunk egy üres listát (get() metódus 2. paramétere), amibe beletesszük az elemet.
    csoportok[ertek] = csoportok.get(ertek, []) + [kulcs]

print(csoportok)


print()

def legkisebb(elso, *tobbi): # *args néven szokás
    acc = elso
    print(type(tobbi))
    for x in tobbi:
        if x < acc:
            acc = x
    return acc

print(legkisebb(3, 4, 2, -8, 6, 5, 54, 35, 5, 6, -10))

# elso  = 3
# tobbi = (4, 2, -8, 6)