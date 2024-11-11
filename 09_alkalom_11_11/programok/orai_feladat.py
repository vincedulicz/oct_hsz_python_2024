import random
from datetime import datetime, timedelta

# I. Feladat: Adott dátumhoz napok hozzáadása
def i_feladat():
    start_date = datetime(2024, 11, 11)
    days_to_add = 15

    new_date = start_date + timedelta(days=days_to_add)

    print("New date:", new_date.strftime("%Y-%m-%d"))


# II. Feladat: Véletlen szám generálása adott intervallumban
def ii_feladat():
    random_number = random.randint(1, 100)
    print("Random number:", random_number)


# III. Feladat: Véletlenszerű dátum generálása egy évben belül
def iii_feladat():
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)

    random_days = random.randint(0, (end_date - start_date).days)
    random_date = start_date + timedelta(days=random_days)

    print("Random date:", random_date.strftime("%Y-%m-%d"))


# IV. Feladat: Véletlenszerű listaelem kiválasztása
def iv_feladat():
    names = ["Alice", "Bob", "Charlie", "Diana"]
    chosen_name = random.choice(names)

    print("Chosen name:", chosen_name)


# V. Feladat: Időkülönbség kiszámítása
def v_feladat():
    date1 = datetime(2024, 11, 8)
    date2 = datetime(2025, 2, 15)
    difference = (date2 - date1).days

    print("Difference in days:", difference)


# VI. Feladat: Véletlenszerű számsorozat generálása
def vi_feladat():
    random_numbers = [random.randint(1, 50) for _ in range(10)]
    print("Random sequence:", random_numbers)


# VII. Feladat: Dátum érvényességének ellenőrzése
def vii_feladat():
    year, month, day = 2024, 2, 32
    try:
        valid_date = datetime(year, month, day)
        print("Valid date:", valid_date)
    except ValueError:
        print("Invalid date")


# VIII. Feladat: Véletlenszerű sorrend létrehozása
def viii_feladat():
    items = ["apple", "banana", "cherry", "date"]
    random.shuffle(items)

    print("Shuffled list:", items)


# IX. Feladat: Jövőbeli dátum és idő kiszámítása
def ix_feladat():
    now = datetime.now()
    future_time = now + timedelta(days=3, hours=4, minutes=30)

    print("Future time:", future_time)


# X. Feladat: Születésnap kiszámítása
def x_feladat():
    today = datetime.now()
    birthday = datetime(today.year, 12, 25)

    if birthday < today:
        birthday = birthday.replace(year=today.year + 1)
    days_left = (birthday - today).days

    print("Days until birthday:", days_left)


# XI. Feladat: Véletlenszám generálása folytonos intervallumban (uniform)
def xi_feladat():
    random_float = random.uniform(1.0, 10.0)
    print("Random float:", random_float)


# XII. Feladat: Egész véletlenszám generálása (randint)
def xii_feladat():
    random_integer = random.randint(50, 100)
    print("Random integer:", random_integer)


# XIII. Feladat: Lista elemeinek megkeverése (shuffle)
def xiii_feladat():
    items = [1, 2, 3, 4, 5]
    random.shuffle(items)

    print("Shuffled list:", items)


# XIV. Feladat: Lista egy elemének kiválasztása (choice)
def xiv_feladat():
    colors = ["red", "blue", "green", "yellow"]
    chosen_color = random.choice(colors)

    print("Chosen color:", chosen_color)


# XV. Feladat: Több elem véletlenszerű kiválasztása (sample)
def xv_feladat():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random_sample = random.sample(numbers, 3)

    print("Random sample:", random_sample)


# XVI. Feladat: Dátum formázása szöveggé (strftime)
def xvi_feladat():
    today = datetime.now()
    formatted_date = today.strftime("%Y-%m-%d")

    print("Formatted date:", formatted_date)


# XVII. Feladat: Szövegből dátum objektum készítése (strptime)
def xvii_feladat():
    date_string = "2024-11-11"
    date_object = datetime.strptime(date_string, "%Y-%m-%d")

    print("Datetime object:", date_object)


# XVIII. Feladat: Születési dátum formázása
def xviii_feladat():
    birth_date = "15/05/1990"
    formatted_date = datetime.strptime(birth_date, "%d/%m/%Y").strftime("%Y-%m-%d")

    print("Formatted birth date:", formatted_date)


# XIX. Feladat: Véletlenszerű lebegőpontos számok listája (uniform)
def xix_feladat():
    random_floats = [random.uniform(0.0, 1.0) for _ in range(5)]

    print("Random floats:", random_floats)


# XX. Feladat: Véletlenszerű csapatok generálása (sample)
def xx_feladat():
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack"]

    team1 = random.sample(names, 5)
    team2 = [name for name in names if name not in team1]

    print("Team 1:", team1)
    print("Team 2:", team2)


def main():
    i_feladat()
    ii_feladat()
    iii_feladat()
    iv_feladat()
    v_feladat()
    vi_feladat()
    vii_feladat()
    viii_feladat()
    ix_feladat()
    x_feladat()
    xi_feladat()
    xii_feladat()
    xiii_feladat()
    xiv_feladat()
    xv_feladat()
    xvi_feladat()
    xvii_feladat()
    xviii_feladat()
    xix_feladat()
    xx_feladat()


# main()
