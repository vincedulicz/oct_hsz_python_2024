import math


def szokoz_nelkul():
    """
    Írj egy olyan programot,
    mely egy szövegből kiszedi a szóközöket!
    """

    szoveg = "H e l l o, vilag!"
    spacenelkul = ""

    for i in szoveg:
        if i != ' ':
            spacenelkul += i

    print(spacenelkul)



def palindrom():
    """
    Írj programot, amelyik egy mondatról eldönti,
    hogy palindrom-e.
    """

    szoveg = "Indul a görög aludni."

    csakbetuk = ""
    for i in szoveg:
        if i.isalnum(): # a-z 0-9
            csakbetuk += i.lower()

    """print(csakbetuk)
    print(csakbetuk[::-1])
    if csakbetuk != csakbetuk[::-1]:
        print("A megadott szöveg nem palindrom!")
    else:
        print("A megadott szöveg palindrom!")"""

    hibas = False
    index = 0
    hossz = len(csakbetuk)
    while index < hossz / 2:
        if csakbetuk[index] != csakbetuk[hossz - 1 - index]:
            hibas = True
            break
        index += 1

    if hibas:
        print("A megadott szó nem palindrom!")
    else:
        print("A megadott szó palindrom!")


def paros_e_jo():
    szam = 3
    return szam % 2 == 0 # True v False


def paros_e_rossz():
    szam = 3

    print(szam % 2 == 0)

    if szam % 2 == 0:
        print("páros")
    else:
        print("nem páros")


def alap_operatorok():
    a = 4
    b = 3

    eredmeny = "eredmény"
    eredmeny_ = "eredmény_"

    if eredmeny == eredmeny_:
        print("egyeznek a stringek")
    elif eredmeny != eredmeny_:
        print("nem egyeznek")
    else:
        print("valami más")

    if a > b:
        print("a > b")
    elif b > a:
        print("b > a")
    elif b == a:
        print("b egyenlő a")
    else:
        print("más")


def print_olvashatosaga():
    i = 0
    szo = "python"


    print("A szó " + str(i) + ". betűje: " + szo[i] + ".") # olvashatatlan


    print("A szó ", str(i), ". betűje: ", szo[i], ".", sep="") # kicsivel szebb




    formazott = f"A szó {i}. betűje: {szo[i]}"
    print(formazott)



    """
    Egy számmal megadhatjuk a kiírás szélességét
    (hány karakter széles legyen egy oszlop).
    
    A kacsacsőrökkel azt adhatjuk meg, merre igazítsa az oszlopot:
    < balra vagy > jobbra, van egyébként = is, az középre teszi.
    
    Számok esetén egy pont után megadhatjuk a tizedesjegyek számát is,
    illetve a megjelenítés módját:
    
    e = exponenciális (tudományos) alak,
    f = fix alak (mindig ugyanannyi tizedesjegy)"""

    gyumolcs = "körte"
    print(f"|{'alma':<12}|")
    print(f"|{gyumolcs:>12}|")
    print(f"|{math.pi:12.5}|")
    print(f"|{math.pi / 2.0:12.5e}|")


def osszeadas():
    """ Stringek összefűzése """

    egyik = input("Írj be valamit: ")
    masik = input("Írj be még valamit: ")

    print(egyik + masik)


def szam_osszeadas():
    """ Számok összeadása """

    egyik = int(input("Írj be valamit: "))
    masik = int(input("Írj be még valamit: "))

    print(egyik + masik)


def szakasz_hossz():
    """
    Írj egy programot, amely kér a felhasználótól egy számot,
    és kirajzol egy + és − jelekből álló szakaszt.
    Pl. ha a szám 4 akkor 4 db − legyen:

    Mekkora legyen a szakasz?
    4
    +----+
    """

    """print("Mekkora legyen a szakasz?")
    hossz = int(input())

    print("+", end="")

    i = 0
    while i < hossz:
        print("-", end="")
        i += 1

    print("+")"""


    """print("Mekkora legyen a szakasz?")
    hossz = int(input())

    print("+")

    print("-" * hossz)

    print("+")"""


    """print("Mekkora legyen a szakasz?")

    hossz = int(input())

    print("+", "-" * hossz, "+", sep="")"""


def szakasz_hossz_koordinata():
    """
    Írj programot, amely a felhasználótól bekéri két síkbeli
    pont x és y koordinátáit, és kiírja a közéjük húzott
    egyenes szakasz hosszát (Pitagorasz tételével)!
    """

    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))

    hossz = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    print(hossz)


def is_operator():
    a = [1, 2, 3]
    b = list(a)

    print("a == b:", a == b)
    print("a is b:", a is b)  # !

    b.append(4)
    b.remove(1)

    print(a)
    print(b)


def is_operator_():
    x = [1, 2, 3]
    y = [1, 2, 3]

    print("x == y:", x == y)
    print("x is y:", x is y)  # !

    y.append(4)
    print(x)


def feladat_pontok():
    """A dolgozatok 0–10 pontosak lehetnek.
    A kérdésünk, hogy melyik pontszámból hány darab lett."""

    # bemenet: 3, 4, 5 ... 6
    # kimenet:
    #  0 p     1 db
    #  1 p     7 db
    #  2 p     3 db
    # ...
    #  9 p    34 db
    # 10 p    17 db

    # pontok beolvasása
    pontok = []
    be = input("Pont? ")

    while be != "":
        pontok.append(int(be))
        be = input("Pont? ")


    # 0–10-ig megszámoljuk mindig
    for keresett in range(0, 10 + 1):
        db = 0
        for pont in pontok:
            if pont == keresett:
                db += 1
        print(f"{keresett:2} p, {db:2}")


def piramis_golyo():
    """
    A feladat megoldásának kulcsa egy rajz készítése…
    És annak meghatározása, hogy melyik sorban hány golyó
    és hány szóköz van.
    """

    magas = int(input("Milyen magas legyen a kupac?"))

    sor = 0
    while sor < magas:
        print(f'sor: {sor}')
        # A sorok elejére kellenek szóközök
        oszlop = 0
        while oszlop < magas - sor - 1:
            # print(f'Oszlop: {oszlop}, magas-sor-1: {magas-sor-1}')
            print(" ", end="")
            oszlop += 1

        # Utána valamennyi darab o
        oszlop = 0
        while oszlop < sor * 2 + 1:
            # print(f'Oszlop: {oszlop}, sor*2+1: {sor*2+1}')
            print("o", end="")
            oszlop += 1

        print()
        sor = sor + 1


    """print("Milyen magas legyen a kupac?")
    magas = int(input())

    sor = 0
    while sor < magas:
        print(" " * (magas - sor - 1) + "o" * (sor * 2 + 1))
        sor = sor + 1"""


def tartaly_szamlalo():
    """
    Írj programot, amely segít kiszámolni a felhasználónak,
    hogy hány doboz festéket kell vennie a
    lábakon álló tartály festéséhez!
    """

    print("Tartály festése")

    magas = float(input("Milyen magas? "))
    atmero = float(input("Mennyi az átmérője? "))


    sugar = atmero / 2
    doboz = (2 * sugar ** 2 * math.pi + magas * 2 * sugar * math.pi) / 2

    print(math.ceil(doboz), "doboz festék kell.") # math.ceil
    print(doboz, "doboz festék rosszul kiírva.")


def referencia():
    "csak a hivatkozás másolódik"
    a = [1, 2, 3]
    b = a  # !

    b.append(4)
    print(a)


    """ a lista másolódik"""
    x = [1, 2, 3]
    y = list(x)  # új lista

    y.append(4)
    print(x)


def referencia_lista():
    def modify_list(lst):
        lst.append(4)
        print(f"Belső lista: {lst}")

    my_list = [1, 2, 3]
    modify_list(my_list)
    print(f"Külső lista: {my_list}")  # A lista mutálódik, mivel mutábilis


def argumentumok():
    def print_numbers(*args):
        for num in args:
            print(num)

    print_numbers(1, 2, 3, 4, 5, 6, 7, 8)  # Tetszőleges számú argumentum adható át



def fuggveny_parameterrel(nev, kor):
    nev = nev.split(" ")
    kor += 15

    return nev, kor
    # return f'Név: {nev}, kor: {kor}'


"""nev = input()
kor = int(input())
print(fuggveny_parameterrel(nev, kor))"""


def argumentumok_kwargs():
    def print_info(**kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")

    print_info(name="Teszt Elek", age=28, city="Budapest", mail="mail@example.com")


def szorzas():
    def multiply(a, b):
        return a * b

    print(multiply(3, 4))


def tobb_ertek_visszaadasa():
    def arithmetic_operations(a, b):
        return a + b, a - b, a * b, a / b

    sum_val, diff, product, quotient = arithmetic_operations(10, 5)
    print(f"Összeg: {sum_val}, Különbség: {diff}, Szorzat: {product}, Hányados: {quotient}")



def kiiratas():
    hero = {
        "name": "Batman",
        "gender": "Male",
        "race": "Human",
        "height": [
            "6'2",
            "188 cm"
        ],
        "weight": [
            "210 lb",
            "95 kg"
        ],
        "eye-color": "blue2",
        "hair-color": "black"
    }


    szoveg = f"A hős haja {hero['hair-color']} színű."
    print(szoveg)

    szoveg = f"A hős neve {hero['name']}, a szeme színe" \
             f"{' nem ' if hero.get('eye-color') != 'blue' else ''} kék"
    print(szoveg)

# kiiratas()

# tobb_ertek_visszaadasa()

# szorzas()

# argumentumok_kwargs()
# argumentumok()

# referencia_lista()
# referencia()

# print_olvashatosaga()
# alap_operatorok()

# paros_e_rossz()
# paros_e_jo()

# osszeadas()
# szam_osszeadas()

# palindrom()

# szakasz_hossz()
# feladat_pontok()

# piramis_golyo()

# tartaly_szamlalo()

# szakasz_hossz_koordinata()


""" Házi feladat, időmérés """
def feladat_ido():
    from datetime import datetime

    def megfelelo_perc_masodperc():
        """ kiegészítés a házifeladathoz """

        # if-else minta óra perc másodpercre
        hour = None
        if hour == True:
            pass
            # törzs:-> hour min_hour > 23
        else:
            pass
            # törzs:-> hor min_sec > 59
        # end if-else

        a_min = int(input("Perc: "))
        while True:
            if a_min < 0 or a_min > 59:
                a_min = int(input("Kérjük megfelelő számot adjon meg (0-59): "))
            else:
                return a_min

    print("Kérem adja meg az első időpontot:")

    a_hour = int(input("Óra: "))

    # kiegészíteni a megfelelő függvény hívásra
    min_, sec_, hour_ = None
    a_min = megfelelo_perc_masodperc(min_)
    a_sec = megfelelo_perc_masodperc(sec_)
    a_hour = megfelelo_perc_masodperc(hour_)

    first_time = str(f'{a_hour}:{a_min}:{a_sec}')
    print(f'Az első időpont: {first_time}')

    print("Kérem adja meg a második időpontot:")

    b_hour = int(input("Óra: "))
    b_min = megfelelo_perc_masodperc()
    b_sec = megfelelo_perc_masodperc()

    second_time = str(f'{b_hour}:{b_min}:{b_sec}')
    print(f'A második időpont: {second_time}')

    time_format = "%H:%M:%S"

    start = datetime.strptime(first_time, time_format)
    end = datetime.strptime(second_time, time_format)

    difference = end - start
    seconds = int(difference.total_seconds())

    print(f'A különbség másodpercben: {seconds}')
