""" I. feladat """

'''
Egy függvényt tesztelünk, amely két szám
szorzatát adjavissza eredményül.
Írj egy függvényt "szorzat" néven, amely két számot vár
paraméterül és visszaadja a szorzatukat.
Ha nem számot adnak meg, fusson hibára!
'''

# Egy lehetséges megoldás:

# Tájékoztatjuk a felhasználót a program működéséről
print('Egy függvényt tesztelünk, amely két'
      'szám szorzatát adja vissza eredményül.')

# Definiáljuk a fügvvényt
def szorzat(x, y):
    return x * y

# Ez itt a tesztelés:
# Bekérjük a két számot és egyből valós
# számtípussá (float) is alakítjuk a változókat
num1 = float(input('Adj meg egy számot: '))
num2 = float(input('Adj meg még egy számot: '))

# Teszteljük a függvényt
print('A két szám szorzata: ', szorzat(num1, num2))
