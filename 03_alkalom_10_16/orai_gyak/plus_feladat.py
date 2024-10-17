""" Egy függvényt tesztelünk, amely bekér egy sztringet
szóközökkel (min 1) és a bekért sztringből kiveszi a szóközöket."""


# Egy lehetséges megoldás
def szokoz_nelkul(szoveg):
    space_nelkul = ""

    for i in szoveg:
        if i != ' ':
            space_nelkul += i

    return space_nelkul


szoveg = input("Ez a függvény kiveszi a space karaktereket: ")

space_nelkul = szokoz_nelkul(szoveg)
print(f'A megoldás {space_nelkul}')
