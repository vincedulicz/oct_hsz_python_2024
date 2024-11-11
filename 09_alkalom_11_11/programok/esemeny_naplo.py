"""

Események naplózása fájlba

Feladat

Készíts egy programot, amely:

Egy szöveges fájlban ("naplo.txt") tárolja különböző események naplóit.
Minden eseményt véletlenszerű időközönként generál
(pl. különböző napokon és időpontokon).

Minden bejegyzést magyar nyelvű dátummal és
időbélyeggel rögzít (pl. „2024. október 25. péntek, 14:23” formátumban).

Az események típusa véletlenszerűen legyen kiválasztva egy listából.
Új futáskor hozzáfűzi az új eseményeket a meglévő fájlhoz.

Ellenőrzi, hogy a fájl mérete ne haladja meg az 5 KB-ot;
ha igen, akkor új fájlt hoz létre (pl. "naplo_2.txt").

"""
import locale, os, random, datetime

locale.setlocale(locale.LC_TIME, 'hu_HU.UTF-8')

EVENTS = ["Felhasználói bejelentkezés",
          "Adatfeltöltés",
          "Jelszó módosítás",
          "Kilépés",
          "Hozzáférés megtagadva"
          ]


def get_log_filename(base_name="naplo", max_size=5 * 1024):
    """ Fájlnév beállítása és méretellenőrzés """

    filename = f'{base_name}.txt'
    counter = 1

    while os.path.exists(filename) and os.path.getsize(filename) > max_size:
        counter += 1
        filename = f'{base_name}_{counter}.txt'

    return filename


def random_past_datetime():
    """ Véletlenszerű időpont generálása """

    days_ago = random.randint(0, 30)
    hours_ago = random.randint(0, 23)
    minutes_ago = random.randint(0, 59)

    event_time = datetime.datetime.now() \
                 - datetime.timedelta\
                     (days=days_ago,
                      hours=hours_ago,
                      minutes=minutes_ago
                      )

    return event_time


def create_log_entry():
    """ Napló esemény létrehozása """

    event_time = random_past_datetime()
    event = random.choice(EVENTS)
    formatted_time = event_time.strftime("%Y. %b %D. %a, %H:%M")

    return f'{formatted_time} - {event}'


def write_log_events(num_entries=10):
    """ Esemény fájlba írása """

    filename = get_log_filename()
    with open(filename, "a", encoding='UTF-8') as file:
        for _ in range(num_entries):
            entry = create_log_entry()
            file.write(entry + "\n")
            print(f'Naplózott esemény: {entry}')


def main():
    write_log_events(1000)


main()




