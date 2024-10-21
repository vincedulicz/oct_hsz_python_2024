# 1. feladat

def elso_feladat():
    db = [0] * 10

    print("Számok 1 és 10 között, üres sor = vége: ")
    sor = input()
    while sor != "":
        szam = int(sor)
        db[szam - 1] += 1
        sor = input()

    szam = 1
    while szam <= 10:
        print("{}: {} db".format(szam, db[szam - 1]))
        szam += 1


# 2. feladat

def masodik_feladat():
    ev = int(input(f'Év: '))

    def szokoev_alter(ev):
        return ev % 400 == 0 or (ev % 4 == 0 and ev % 100 != 0)


    def szokoev(ev):
        if ev % 400 == 0:
            return True
        if ev % 4 == 0 and ev % 100 != 0:
            return True
        return False

    print(szokoev(ev))
    print(szokoev_alter(ev))


# 3. feladat
def atlag(szamok):
    return sum(szamok) / len(szamok)


def kisebbek_szurese(szamok, minel):
    szurt = []
    for x in szamok:
        if x < minel:
            szurt.append(x)
    return szurt


def atlagnal_kisebbek(szamok):
    return kisebbek_szurese(szamok, atlag(szamok))


def main_harmadik():
    szamok = [24, 31, 22, 43, 10, 84, 38, 44, 84, 56, 67, 51, 56, 84, 31, 65, 69, 83, 39]
    print(atlagnal_kisebbek(szamok))


# main_harmadik()


# 4. feladat
def cserel(szo, hol, mire):
    if hol < 0 or hol >= len(szo):
        raise ValueError("Érvénytelen pozíció: " + str(hol))
    return szo[0:hol] + mire + szo[hol + 1:]


def negyedik_feladat():
    uj = cserel("répa", 1, "i")
    print(uj)

    try:
        uj = cserel("teszt", -1, "X")
        print(uj)
    except ValueError as e:
        print(e)
