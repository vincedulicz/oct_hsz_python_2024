''' Egy függvényt tesztelünk, amely két szám
közül adja vissza a nagyobb háromszorosát.
Írj függvényt "nagyobb_tripla" néven, amely
visszaadja a két szám közül a nagyobb háromszorosát.
'''
# Egy lehetséges megoldás:

# Tájékoztatjuk a felhasználót a program működéséről
print('\nEgy függvényt tesztelünk, amely két szám'
      'közül adja vissza a nagyobb háromszorosát.')

# Definiáljuk a fügvvényt
def nagyobb_tripla(x, y):
    return max(x, y) * 3

# Ez itt a tesztelés:
# Bekérjük a két számot és egyből valós
# számtípussá (float) is alakítjuk a változókat
num1 = float(input('Adj meg egy számot: '))
num2 = float(input('Adj meg még egy számot: '))

# Teszteljük a függvényt
print('A két szám közül a nagyobb háromszorosa: ', nagyobb_tripla(num1, num2))