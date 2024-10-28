"""
0. Csinálj egy ciklust, ami minden páros elemet megszoroz 3-al,
minden páratlant 5-el szoroz és kettővel oszt,
és minden 5. elemet hagyj ki, ami a listába nem kerül bele.

Ha lehet list comprehension-el oldd meg ezt. A lista hossza legyen 42.
0+1. List comprehension-el oldd meg a ciklusokat amennyiben ez lehetséges.
1. Tájékoztasd a felhasználót a program működéséről a mintának megfelelően!
2. Írasd ki a listát a konzolra a mintának megfelelően!
3. Kérj be a felhasználótól egy kétjegyű számot
és azt szúrd be a lista második
helyére! A felhasználó jó számot ad meg, azt nem kell ellenőrizni.
4. Írd ki a módosított listát!
5. Kérd be a felhasználótól, hogy melyik elemet akarja törölni!
A felhasználó meglévő elemet ad meg, azt nem kell ellenőrizni.
6. Töröld a kért elemet a listából és írd ki újra a listát!
7. Rendezd a listát és írd ki újra!
8. Fordítsd meg a lista elemeinek a sorrendjét és írd ki újra!


"""

def lista_letrehozasa():
    """Létrehozza a listát a megadott szabályok szerint."""

    """result = []
    for i in range(1, 43):
        if i % 5 != 0:
            if i % 2 == 0:
                result.append(i * 3)
            else:
                result.append(i * 5 / 2)"""

    return [
        (i * 3 if i % 2 == 0 else i * 5 / 2) for i in range(1, 43) if i % 5 != 0
    ]




def lista_kiirasa(lista, uzenet="Lista:"):
    """Kiírja a listát egy adott üzenettel."""
    print(f"{uzenet} {lista}")




def elem_beszurasa(lista):
    """Bekér egy kétjegyű számot a felhasználótól és beszúrja a lista második helyére."""
    szam = int(input("Adj meg egy kétjegyű számot: "))
    lista.insert(1, szam)



def elem_torlese(lista):
    """Bekér egy elemet, amit töröl a listából."""
    torlendo = int(input("Melyik elemet szeretnéd törölni? "))
    lista.remove(torlendo)



def lista_rendezese(lista):
    """Rendezi a listát növekvő sorrendben."""
    lista.sort()


def lista_megforditasa(lista):
    """Megfordítja a lista elemeinek sorrendjét."""
    lista.reverse()
    # lista.sort(reverse=True)

# Fő program
def main():
    # 1. Létrehozza a listát
    lista = lista_letrehozasa()
    lista_kiirasa(lista, "Eredeti lista")

    # 2. Elem beszúrása
    elem_beszurasa(lista)
    lista_kiirasa(lista, "Módosított lista")

    # 3. Elem törlése
    elem_torlese(lista)
    lista_kiirasa(lista, "Lista a törlés után")

    # 4. Rendezi a listát és kiírja
    lista_rendezese(lista)
    lista_kiirasa(lista, "Rendezett lista")

    # 5. Megfordítja a listát és kiírja
    lista_megforditasa(lista)
    lista_kiirasa(lista, "Fordított sorrendű lista")

# Program futtatása
main()
