
try:
    szam = int(input('Adj meg egy számot: '))
    print(f'A szám négyzete: {szam ** 2}')
except Exception as e:
    print(e)
    print('Nem szám')


try:
    oszto = int(input('Mennyivel osszam el a 10-et'))
    print(f'Az eredmény: {10 / oszto}')
except ZeroDivisionError as e:
    print(f'Hiba: {e}')
    print("0-val nem lehet osztani")
except ValueError as e:
    print(f'Hiba: {e}')
    print("ez nem szám")
finally:
    print("na ez mindig lefut")


print("progi vége")


try:
    oszto = int(input("mennyivel osszam a 10-et?"))
    print(f'eredmeny: {10/oszto}')
except (ZeroDivisionError, ValueError) as e:
    print(f'hiba: {e}')
finally:
    print("proginak vége")



forrasfajl = open('autok_listaja.txt')
# print(type(forrasfajl))

# fájl objektum bejárása
for sor in forrasfajl:
    print(sor)


# print(forrasfajl.readline()) # 1-es sorok

# print(forrasfajl.readlines()) # listával tér vissza, összes elemmel együtt

# print(forrasfajl.read()) # teljes fájltartalom

forrasfajl.close() # bezárás



autok = []

with open('autok_listaja.txt', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(',')
        auto = {'rendszam': adatok[0], 'tipus': adatok[1], 'kor': int(adatok[2])}
        autok.append(auto)

print(f'{autok=}')




# megnyitási módok:

# r:  olvasás
# w:  írás, fájlt hoz létre v felülírja
# x:  írás, fájlt hoz létre DE ha van ilyen akkor hibát dob
# a:  létező fájl végére hozzűfűzni, ha nem létezik akkor létrehozza
# a+: hozzáfűzés és olvasás


with open('kimenet.txt', 'w', encoding='utf-8') as celfajl:
    print("Ez kerül a fájlba...", file=celfajl)


with open('kimenet.txt', 'w', encoding='utf-8') as celfajl:
    # str-et írunk
    celfajl.write('alma, körte, mézesdió\n')

    # lista elemei
    celfajl.writelines(['alma\n', 'körte\n', 'mézesdió\n'])



with open('gyumolcsok.txt', 'r', encoding='utf-8') as forrasfajl, \
        open('gyumolcsok_masolat.txt', 'w', encoding='utf-8') as celfajl:
    for sor in forrasfajl:
        print(sor.strip(), file=celfajl)




import json

with open('diakok.json', 'r', encoding='utf-8') as diak_adatok:
    adatok = json.load(diak_adatok)

print(type(adatok))

for diak in adatok['diakok']:
    print(diak.get('név'))
    print(diak)

    if not diak.get('kollegista'):
        print('mér')
    else:
        print('az')




