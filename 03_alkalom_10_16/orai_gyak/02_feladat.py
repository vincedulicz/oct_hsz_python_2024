''' Egy függvényt tesztelünk,
amely két szám közül adja vissza a kisebb dupláját.
Írj egy függvényt "kisebb_dupla" néven,
amely két számot kap paraméterül és visszaadja
a kisebb szám dupláját.
'''
# Egy lehetséges megoldás:

# Tájékoztatjuk a felhasználót a program működéséről
print('Egy függvényt tesztelünk, amely két szám'
      'közül adja vissza a kisebb dupláját.')

# Definiáljuk a fügvvényt
def kisebb_dupla(x, y):
    print(min(x, y))
    return min(x, y) * 2

# Ez itt a tesztelés:
# Bekérjük a két számot és egyből valós
# számtípussá (float) is alakítjuk a változókat
num1 = float(input('Adj meg egy számot: '))
num2 = float(input('Adj meg még egy számot: '))

# Teszteljük a függvényt
print('A két szám közül a kisebb duplája: ', kisebb_dupla(num1, num2))