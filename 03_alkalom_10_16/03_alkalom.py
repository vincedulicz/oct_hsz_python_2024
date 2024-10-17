### Python kurzus 3. alkalom - 2024.10.16 ###

"""
I.

Egy szám osztói

Írj programot, mely bekér egy pozitív egész számot,
majd kiszámolja és kiírja annak osztóit!
Az osztók egy sorban, pontosvesszővel
elválasztva jelenjenek meg!


A program várt működése pl. a következő:

Írj be egy pozitív egész számot: 15

15 osztói:
1; 3; 5; 15

"""

"""

Megoldási terv

bekérjük a számot, típusnak megfelelően konvertáljuk
osztó változó amiben gyűjtük őket
minden n számra (ciklusléptető) 2- től a megadott szám feléig
vizsgáljuk, hogy n osztója-e.
ha igen akkor n hozzá fűzésre kerül az osztó változóhoz
eredmény kiírása

"""


def szam_osztoi():
    szam = int(input("Írjá be egy egész számot: "))
    osztok = "1"

    n = 2
    while n <= szam // 2: # egészosztás
        if szam % n == 0:
            osztok += "; " + str(n)
        n += 1

    osztok += "; " + str(szam)

    print(str(szam) + " osztói:")
    print(osztok)




"""
II.

Tökéletes számok


Egy pozitív egész számot tökéletesnek nevezünk,
ha a szám megegyezik az önmagánál kisebb osztóinak összegével.

Pl. a 6 tökéletes szám, mert az
önmagánál kisebb osztói az 1, 2, 3, és ezek összege pont 6.

Az előző feladat mintájára, írj programot,
mely bekér egy pozitív egész számot, majd megállapítja,
hogy az tökéletes szám-e vagy nem!

A program várt működése pl. a következő:

Írj be egy pozitív egész számot: 6
Tökéletes szám!

Írj be egy pozitív egész számot: 12
Nem tökéletes szám.

"""

""" 

Megoldási terv:

számbekérése, típuskonverzió, osztók összegére egy változó
ez lehet 1 hiszen minden számnam osztója
ehhez adjuk a további osztókat
minden számra 2-től nézzük a megadott szám feléig, osztója-e
vagy sem, ha igen hozzá adjuk a számot az osztók összegéhez
ellenőrzés az osztók összege megegyezik-e a számmal

"""



def tokeletes_szam():
    szam = int(input("Írj be egy számot egészet: "))
    osztok_osszege = 1

    n = 2
    while n <= szam // 2:
        if szam % n == 0:
            osztok_osszege += n
        n += 1

    if osztok_osszege == szam:
        print("Tökéletes szám")
    else:
        print("nem az")


def tokeletes_szam_felso_hatar():
    felso_hatar = int(input("Tökéletes szám felső határa: "))

    elso_tokeletes_szam = 6
    while elso_tokeletes_szam <= felso_hatar:
        osztok_osszege = 1

        n = 2
        while n <= elso_tokeletes_szam // 2:
            if elso_tokeletes_szam % n == 0:
                osztok_osszege += n
            n += 1

        if osztok_osszege == elso_tokeletes_szam:
            print(elso_tokeletes_szam)

        elso_tokeletes_szam += 1











"""

III. Tökéletes szám keresés megadott felső határig

Megoldás:

Programtörzs ciklusba ágyazva, 6-tól a felső határig

"""

def tokeletes_szam_felso_hatarral():
    pass


# a tökéletes számok elég ritkák, közel 50-et ismerünk
#  2**(p−1)(2p−1), ahol 2**(p-1) és p is prím






""" String műveletek IV. """
# len lower upper find count replace strip stb...


szoveg = "füst Fölt SZALO NA toaaaa rmF gval"
# print(len(szoveg))

# print(f'0. index {szoveg[0]}')
# print(f'2. index {szoveg[2]}')

# print(f'utolsó karaktere: {szoveg[-2]}')

# print(f'második karakter: {szoveg[::2]}')

# print(f'fordított: {szoveg[::-1]}')

# szoveg[0] = "k" # nem fog működni
# print(szoveg.replace("ö", "á"))

"""if "q" not in szoveg:
    print("nincs q")
else:
    print("van q")"""

"""print(f'kezdő: {szoveg.startswith("")} végző: {szoveg.endswith("")}')

if szoveg.startswith("6"):
    print("számmal kezdődik")
else:
    print("nem")"""

"""print(szoveg.lower())
print(szoveg.upper())
print(szoveg.count("a"))"""

"""splittelt_szoveg = szoveg.split(" ")
print(splittelt_szoveg)
"""

# pi = 3.141592653
# print('a pi értéke {} az annyi {} <- ebbe'.format(pi, pi-1))
# print(f'szöveg {pi} ez meg másik {szoveg} ... {5}')


szoveg = "Hello"
# print(szoveg)
# print(szoveg.swapcase())

# lista = list(enumerate(szoveg))
# print(lista)

# for char in szoveg:
#   print(char)

"""elotag = "Törp"

utotagok_listaja = ["erős", "költő", "morgó", "oltő"]

for utotag in utotagok_listaja:
    print(elotag + utotag)"""


"""nevek = ["erős", "költő", "morgó", "oltő"]

print(nevek[2:4])"""

"""
szoveg = "szöveg"
print(szoveg.find("veg"))"""


"""a = 5
b = 4

print(f'a: {a} ; b: {b}')

tmp = a
a = b
b = tmp

print(f'a: {a} ; b: {b}')

a = 5
b = 4

a, b = b, a

print(f'a: {a} ; b: {b}')"""







""" 
V.

Prímszám 

Egy pozitív egész számot prímszámnak nevezünk,
ha a számnak csak 1 és önmaga az osztója.

Az 1 definíció szerint nem prím. A legkisebb prímszám
így a 2, hiszen csak 1-gyel és önmagával osztható.

Írj programot, mely bekér egy pozitív egész számot,
majd megállapítja, hogy az prímszám-e vagy sem!

A program várt működése pl. a következő:

Írj be egy pozitív egész számot: 6
Nem prím.

Írj be egy pozitív egész számot: 13
Prím.

"""

""" 

Megoldás: 

Számbekérése, ha 1 nem megyünk tovább, egyébként igen..
Boolean változó -> prím vagy nem prím tárolására
ciklus ellenőrzéssel minden számra 2 és a vizsgálandó
szám gyöke között, osztja vagy sem. Ha van osztó akkor nem prím

sqrt math könyvtárból a gyök kiszámításához

"""


def primkereso():
    from math import sqrt

    szam = int(input("szám: "))

    if szam == 1:
        print("def szerint ez nem prím")
    else:
        prim = True

        n = 2
        while n <= sqrt(szam):
            if szam % n == 0:
                prim = False

            n += 1

        if prim:
            print("prím")
        else:
            print("nem prím")


primkereso()










""" 
VII.

Prímszámok keresése megadott felső határig

Írj programot, mely egy megadott felső határig
az összes számot megvizsgálja, és kiírja a prímszámokat!
A program várt működése pl. a következő:

Prímszám keresésének felső határa: 100

Ezeket a prímszámokat találtam:
2; 3; 5; 7; 11; 13; 17; 19; 23;
29; 31; 37; 41; 43; 47; 53; 59;
61; 67; 71; 73; 79; 83; 89; 97;


"""

"""

Megoldási terv:

Előző program törzse már tudja a várt működést
Ciklusba ágyazva megkaphatjuk 2-től a felső határig

"""




def primszam_kereso_felso_hatarig():
    pass













"""

VII. Pitagoraszi számhármasok

A Pitagorasz-tétel azt mondja ki, hogy bármely
derékszögű háromszög leghosszabb oldalának
(átfogójának) négyzete megegyezik a másik két oldal
(a befogók) négyzetének összegével.

Röviden: a**2 + b**2 = c**2

Írj programot, mely bekéri egy háromszög három
oldalának hosszát, majd megállapítja,
hogy a háromszög derékszögű-e!

A program várt működése
pl. a következő:

1. oldal: 5           | 1. oldal: 3
2. oldal: 4           | 2. oldal: 6
3. oldal: 3           | 3. oldal: 7

Derékszögű 3szög      | Nem derékszögáő 3szög

"""

"""

Megoldási terv:

3szám bekérése, konvertálás,
3. oldal legyen a legnagyobb (szám csere, tétel miatt)
tétel ellenőrzés
kiírás

"""


def pitagoraszi_szamharmas():
    pass

