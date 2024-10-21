"""

I. feladat

A program bekér egy szöveget és a választásod alapján
kiír ezt-azt a szövegről. Üres szövegre leáll.
Olvassunk be egy szöveget.

Kérdezzük meg a felhasználót, hogy mit szeretne:
a) Kiírjuk hány 'a' betű van a szövegben
b) Kiírjuk a szöveg hosszát
c) Kiírjuk a szöveg nagybetűs változatát

Addig ismételjük a fentebb írtakat,
amíg üres szöveget nem ad meg a felhasználó.
Mind a három feladatot (a, b, c)
saját külön függvényekkel oldjunk meg.


"""


# Egy lehetséges megoldás:

def elso_feladat():
    # Megírjuk az egyes menüpontokhoz tartozó függvényeket
    def count_char_a(input_text):
        print('A szövegben ennyi "a" betű van:', input_text.count('a'))

    def text_len(input_text):
        print('A szöveg hossza: ', len(input_text))

    def text_to_upper(input_text):
        print('A nagybetűs verzió: ', input_text.upper())

    # Tájékoztatjuk a felhasználót a program működéséről
    print('\nA program bekér egy szöveget és a választásod alapján kiír ezt-azt a szövegről. Üres szövegre leáll.')

    # Bekérünk egy szöveget:
    text = input('\nAdj meg egy tetszőleges szöveget: ')

    # Indítunk egy ciklust, amely addig tart, amíg nem üres szöveg jön be
    while text != '':
        # Kiírjuk a menüt
        print('Válassz:')
        print('a) Kiírjuk hány "a" betű van a szövegben')
        print('b) Kiírjuk a szöveg hosszát')
        print('c) Kiírjuk a szöveg nagybetűs változatát')

        # Bekérjük a választott menü betűjelét
        select = input('Válassz [a, b, c]: ').lower()

        # A választás alapján meghívjuk a megfelelő függvényt
        if select == 'a':
            count_char_a(text)
        elif select == 'b':
            text_len(text)
        elif select == 'c':
            text_to_upper(text)

        # Bekérünk egy újabb szöveget:
        text = input('\nAdj meg egy tetszőleges szöveget: ')

    # Elbúcsúzunk
    print("Viszlát!")



"""

II. Feladat

Egy kör sugarát kérjük be és kiírjuk a
kerületét cm-ben és a területét cm²-ben.
Kérjük be a felhasználótól egy kör sugarát, cm-ben értve.

Feltételezhetjük, hogy a felhasználó valóban
számot ad meg, de az lehet tört szám is.
Írj két saját függvényt a kör
adatainak a kiszámításához.

Az egyik függvény neve 'kerulet' legyen,
bemenő paramétere a kör sugara cm-ben.
A függvény számolja ki a kör kerületét és
írja is ki az eredményt a konzolra a minta szerint, cm-ben.

A másik függvény neve 'terulet' legyen,
bemenő paramétere a kör sugara cm-ben.
A függvény számolja ki a kör területét és
adja vissza az eredményt.
A szöveges, minta szerinti cm²-ben számolt
kiírást a főprogramban hajtsuk végre.
Az eredményeket mindkét esetben 2 tizedesre kerekítsük.

"""


# Egy lehetséges megoldás:

def masodik_feladat():
    from math import pi  # Beolvassuk a math modulból a pi-t

    # Definiáljuk a 'kerulet' fügvvényt
    def kerulet(r):
        # Kiszámoljuk a kör kerületét és kerekítjük két tizedesre
        ker = round(2 * r * pi, 2)
        # Kiírjuk a minta szerint az eredményt
        print(f'A kör kerülete: {ker} cm')

    # Definiáljuk a 'terulet' függvényt
    def terulet(r):
        # Kiszámoljuk a kör területét, kerekítjük két tizedesre és vissza is adjuk
        return round(r * r * pi, 2)

    # Tájékoztatjuk a felhasználót a program működéséről
    print('\nEgy kör sugarát kérjük be és kiírjuk a kerületét cm-ben és a területét cm²-ben.')

    # Bekérjük a kör sugarát
    sugar = float(input('Add meg egy kör sugarát cm-ben: '))

    # Megívjuk a 'kerulet' függvényt
    kerulet(sugar)
    # Meghívjuk a 'terulet' függvényt és kiírjuk a minta szerinti eredményt
    print(f'A kör területe: {terulet(sugar)} cm²')


"""

III. feladat

Beolvasunk 5 egész számot és e
listárólírunk ki információkat.
Mindegyik alábbi feladathoz készítsünk saját függvényt.
A 2. feladattól kezdve a függvények bemenő
paramétere a lista, visszatérési értékük
pedig a kiíratandó teljes szöveges válasz a kérdésre.

1. Olvassunk be öt egész számot egy listába.
Feltételezhetjük, hogy a felhasználó
valóban csak egész számokat ad meg.

2. Írjuk ki a lista elemeit egy sorban,
kötőjellel elválasztva, abban a sorrendben,
ahogy azt a felhasználó megadta.

3. Írjuk ki a lista elemeit fordított sorrendben,
egy sorban, kötőjellel elválasztva.

4. Írjuk ki, hányadik elem a legkisebb és mennyi az.

5. Írjuk ki, hányadik elem a legnagyobb és mennyi az.

6. Írjuk ki melyik elem áll a legközelebb
a teljes lista átlagához és hogy az hányadik elem.

"""


# Egy lehetséges megoldás:

def harmadik_feladat():
    # Paraméterek
    max_count = 5  # a lista maximális mérete

    # Függvény: a számok beolvasása
    def szamok_beolvasasa(number_count):
        # Létrehozzuk a listát
        data = []
        # Elindítjuk a max_count-szor lefutó beolvasási ciklust
        for i in range(number_count):
            # Beolvasunk egy új egész számot
            new_item = int(input('Adj meg egy egész számot: '))
            # és felvesszük a listába
            data.append(new_item)
        # Visszaadjuk a listát
        return data

    # Függvény: a lista elemeinek kiírása kötőjellel
    def lista_kiirasa_kotojellel(custom_list):
        # Létrehozzuk a sztringet az első elemmel
        result = str(custom_list[0])
        # Egy ciklusban végigmegyünk a lista elemein a másodikkal kezdve
        for i in range(1, len(custom_list)):
            # és hozzávesszük a sztringhez egy kötőjellel a következő elemet
            result += f'-{custom_list[i]}'
        # Visszaadjuk a válasz sztringet
        return result

    # Függvény: a fordított lista elemeinek kiírása kötőjellel
    def forditott_lista(custom_list):
        # Készítünk egy másolatot a paraméterként jövő listából
        new_list = custom_list.copy()
        # Megfordítjuk a lista elemeinek a sorrendjét
        new_list.reverse()

        # Létrehozzuk a sztringet az első elemmel
        """result = str(new_list[0])
        # Egy ciklusban végigmegyünk a lista elemein a másodikkal kezdve
        for i in range(1, len(new_list)):
            # és hozzávesszük a sztringhez egy kötőjellel a következő elemet
            result += f'-{new_list[i]}'"""

        result = lista_kiirasa_kotojellel(new_list)

        # Visszaadjuk a válasz sztringet
        return f'A fordított sorrend: {result}'

    # Függvény: kiírjuk, hogy hányadik elem a legkisebb és mennyi az
    def legkisebb_elem_indexxel(custom_list):
        # A minimális elem indexének kezdőértéke
        min_idx = 0
        # Az aktuális index kezdőértéke
        idx = 0
        # Indítunk egy ciklust a második elemtől kezdve
        for i in custom_list[1:]:
            # Növeljük az aktuális index értékét
            idx += 1
            # Ha az aktuális elem kisebb mint az eddigi legkisebb
            if i < custom_list[min_idx]:
                # Akkor felülírjuk a legkisebb elem indexét
                min_idx = idx
        # Visszaadjuk a válasz sztringet
        return f'A legkisebb elem: {custom_list[min_idx]}, amelynek az indexe: {min_idx}'

    # Függvény: kiírjuk, hogy hányadik elem a legnagyobb és mennyi az
    def legnagyobb_elem_indexxel(custom_list):
        # A maximális elem indexének kezdőértéke
        max_idx = 0
        # Az aktuális index kezdőértéke
        idx = 0
        # Indítunk egy ciklust a második elemtől kezdve
        for i in custom_list[1:]:
            # Növeljük az aktuális index értékét
            idx += 1
            # Ha az aktuális elem nagyobb mint az eddigi legkisebb
            if i > custom_list[max_idx]:
                # Akkor felülírjuk a leganyobb elem indexét
                max_idx = idx
        # Visszaadjuk a válasz sztringet
        return f'A legnagyobb elem: {custom_list[max_idx]}, amelynek az indexe: {max_idx}'

    # Függvény: kiírjuk, melyik elem van legközelebb az átlaghoz
    def atlaghoz_legkozelebbi(custom_list):
        # A lista átlaga
        average = sum(custom_list) / len(custom_list)
        # A keresett elem indexének kezdőértéke
        avg_idx = 0
        # Az aktuális index kezdőértéke
        idx = 0
        # Indítunk egy ciklust a második elemtől kezdve
        for i in custom_list[1:]:
            # Növeljük az aktuális index értékét
            idx += 1
            # Ha az aktuális elem közelebb van az átlaghoz mint az eddig talált
            if abs(average - i) < abs(average - custom_list[avg_idx]):
                # Akkor felülírjuk a leganyobb elem indexét
                avg_idx = idx
        # Visszaadjuk a válasz sztringet
        return f'Az átlaghoz legközelebbi elem: {custom_list[avg_idx]}, amelynek az indexe: {avg_idx}'

    # Tájékoztatjuk a felhasználót, hogy hogyan működik a program
    print(f'\nBeolvasunk {max_count} egész számot és e listáról írunk ki információkat.')

    # 1. Beolvassuk a számokat egy listába
    num_list = szamok_beolvasasa(max_count)

    # 2. Kiírjuk az eredeti sorrendet
    print(lista_kiirasa_kotojellel(num_list))

    # 3. Kiírjuk a fordított sorrendet
    print(forditott_lista(num_list))

    # 4. Kiírjuk a legkisebb elemet és annak indexét
    print(legkisebb_elem_indexxel(num_list))

    # 5. Kiírjuk a leganyobb elemet és annak indexét
    print(legnagyobb_elem_indexxel(num_list))

    # 6. Kiírjuk melyik elem van legközelebb az átlaghoz
    print(atlaghoz_legkozelebbi(num_list))


# alter megoldás:
# 1. Beolvasunk 5 egész számot a felhasználótól

# map(function, iterable)

""" példa 

numbers = [1, 2, 3, 4, 5]
def double(x):
    return x * 2

result = map(double, numbers)
print(list(result))  # Eredmény: [2, 4, 6, 8, 10] """



def beolvas():
    lista = []
    for i in range(5):
        szam = int(input(f"Kérem adja meg a(z) {i+1}. számot: "))
        lista.append(szam)
    return lista

# 2. Kiírjuk a lista elemeit kötőjellel elválasztva
def eredeti_lista(lista):
    return '-'.join(map(str, lista)) # join - str összefésülés

# 3. Kiírjuk a lista elemeit fordított sorrendben
def forditott_lista(lista):
    return '-'.join(map(str, lista[::-1]))

# 4. A legkisebb elem helye és értéke
def legkisebb_elem(lista):
    legkisebb = min(lista)
    index = lista.index(legkisebb)
    return f"A legkisebb elem a(z) {index}. helyen van, értéke: {legkisebb}"

# 5. A legnagyobb elem helye és értéke
def legnagyobb_elem(lista):
    legnagyobb = max(lista)
    index = lista.index(legnagyobb)
    return f"A legnagyobb elem a(z) {index}. helyen van, értéke: {legnagyobb}"

# 6. A lista átlagához legközelebb álló elem és annak helye
def legkozelebbi_atlaghoz(lista):
    atlag = sum(lista) / len(lista)
    legkozelebbi = min(lista, key=lambda x: abs(x - atlag))
    index = lista.index(legkozelebbi)
    return f"A legközelebb álló elem az átlaghoz a(z) {index}. helyen van, értéke: {legkozelebbi}"

# A program fő része
"""if __name__ == "__main__":
    lista = beolvas()
    print("A megadott lista elemei:", eredeti_lista(lista))
    print("A lista elemei fordított sorrendben:", forditott_lista(lista))
    print(legkisebb_elem(lista))
    print(legnagyobb_elem(lista))
    print(legkozelebbi_atlaghoz(lista))"""



"""

IV. Feladat

Egy pozitív egész számot alakítunk bináris számmá.
Olvassunk be egy pozitív egész számot
és írjuk ki a bináris alakját.

A beépített bin() függvényt nem használhatod!

Ehhez készítsünk egy dec_bin() függvényt,
amelynek van egy bemenő paramétere és
sztringesen adja vissza a bináris értékét.

A felhasználó biztosan egész számot ad meg,
azt nem kell ellenőrizni.

A program kommunikációját a
mintának megfelelően alakítsd.

"""


# Egy lehetséges megoldás:

# Létrehozzuk a függvényt

def negyedik_feladat():
    def dec_bin(dec):
        # Létrehozzuk a bináris számot tároló változót
        bin = ''

        # Amíg a szám el nem fogy, azaz nulla nem lesz
        while dec > 0:
            # A kettes osztás maradékát előre írjuk
            bin = str(dec % 2) + bin
            # A számot csökkentjük a maradék nélküli kettes osztásra
            dec = dec // 2
        return bin

    # Tájékoztatjuk a felhasználót, hogy hogyan működik a program
    print('\nEgy pozitív egész számot alakítunk bináris számmá.\n')

    # Beolvassuk a számot és egész szám típusúvá is alakítjuk egyből
    szam = int(input('Adj meg egy pozitív egész számot: '))

    print(f'{szam} binárisan: {dec_bin(szam)}')



"""

V. feladat

Összegeket kerekítünk.
Kérj be a felhasználótól egy összeget.
Biztosak lehetünk benne, hogy pozitív
egész számot ad meg, azt nem kell ellenőrizni.

Az összeget kerekítsd lefelé százasokra és írd ki,
majd ugyanezt százasra felfelé kerekítéssel is tedd meg.

Ha a megadott összeg százzal osztható,
akkor a két érték természetesen azonos.
A kerekítésekhez írj saját függvényeket kerek_fel()
és kerek_le() néven.

Mindkét függvénynek egy bemenő paramtere van,
egy egész szám, és a visszatérési érték
a kerekített érték.
A program kommunikációját a mintának
megfelelően szövegezd.

"""


def otodik_feladat():
    # Egy lehetséges megoldás:

    # Létrehozzuk a lefelé kerekítő függvényt
    def kerek_le(x):
        # Kiszámoljuk és vissza is adjuk a százasra lefelé kerekített értéket
        return 100 * (x // 100)

    # Létrehozzuk a felfelé kerekítő függvényt
    def kerek_fel(x):
        # Kiszámoljuk a százasokra felfelé kerekítést
        # Ha a százzal osztásnak van maradéka
        if x % 100 > 0:
            # akkor a lefelé kerekítés plusz száz az eredmény
            return kerek_le(x) + 100
        else:
            # különben azonos a lefelé kerekítéssel
            return kerek_le(x)

    # Tájékoztatjuk a felhasználót, hogy hogyan működik a program
    print('Összegeket kerekítünk.\n')

    # Bekérjük az összeget és egyből számmá is alakítjuk
    osszeg = int(input('Adj meg egy összeget: '))

    # Kiírjuk az eredményt
    print('A százasokra lefelé kerekített értéke:', kerek_le(osszeg))

    # Kiírjuk az eredményt
    print('A százasokra felfelé kerekített értéke:', kerek_fel(osszeg))



"""

VI. feladat

A program induláskor kérjen be egy nevet
és egy születési évszámot, majd írja ki
hány keresztneve van az illetőnek,
és 2030-ban hányadik születésnapja lesz.

A kor meghatározásához hozz létre egy függvényt,
kor2030 néven, ami a paraméterként kapott
évszám alapján kiszámolja a 2030-ban betöltött kort!

A függvény csak adja visszatérési értékül
a számítás eredményét, de a képernyőre ne írja ki!

Amíg a felhasználó kéri, kérje a következő nevet.

A program kommunikációját a mintának
megfelelően szövegezd.

Abban biztosak lehetünk, hogy a felhasználó
egy-egy szóközzel választja csak el a
szavakat és a születési évszámot.

"""


def hatodik_feladat():
    # Egy lehetséges megoldás:

    def kor2030(ev):
        return 2030 - ev

    folytat = 'i'
    while folytat == 'i':
        adat = input('\nAdjon meg egy nevet és egy születési évet: ').split()
        print(f'\nAz adott személynek {len(adat) - 2} keresztneve van: ', end="")
        print(*adat[1:-1], sep=" és ", end=".\n")
        print(f'2030-ban a {kor2030(int(adat[-1]))}. születésnapja lesz.')

        folytat = input('\nSzeretne újabb számítást végezni (i/n)? ').lower()
        while folytat not in ['i', 'n']:
            folytat = input('\nSzeretne újabb számítást végezni (i/n)? ').lower()

hatodik_feladat()
