def beolvas(fajlnev):
    """Beolvassa a számokat a fájlból és int-té alakítja őket."""

    try:
        with open(fajlnev, "r") as f:
            pontszamok = [int(line.strip()) for line in f]
        return pontszamok
    except FileNotFoundError:
        print(f"A '{fajlnev}' fájl nem található.")
        return []
    except ValueError:
        print("A fájl nem megfelelő formátumú számokat tartalmaz.")
        return []

def beolvas_hibara(fajlnev):
    """Beolvassa a számokat a fájlbó, konvertálás int-é
    figyelmen kívül hagyva a hibás sorokat."""

    pontszamok = []
    try:
        with open(fajlnev, "r", encoding='utf-8') as f:
            while True:

                line = f.readline()
                if not line:  # Ha elértük a fájl végét
                    break

                line = line.strip()
                if line == "":  # Üres sor
                    continue

                try:
                    pont = int(line)  # Megpróbálja int-té alakítani
                    if 0 <= pont <= 10:  # Ellenőrzi, hogy a pontszám 0 és 10 között van-e
                        pontszamok.append(pont)
                except ValueError as e:
                    # print(e)
                    continue  # Ha nem sikerül int-té alakítani, átugorja a sort

    except FileNotFoundError:
        print(f"A '{fajlnev}' fájl nem található.")
    return pontszamok

def stat(pontszamok):
    """Statisztikát készít a pontszámokból."""

    statisztika = [0] * 11  # 0-tól 10-ig
    for pont in pontszamok:
        if 0 <= pont <= 10:
            statisztika[pont] += 1
    return statisztika

def stat_kiir(statisztika):
    """Kiírja a statisztikát és a sikeres ZH-kat."""

    atment = sum(count for score, count in enumerate(statisztika) if score >= 4)
    evfolyam_lett = sum(statisztika)

    for score in range(11):
        print(f"{statisztika[score]:2} db {score} pontos")

    if evfolyam_lett > 0:
        atment_szazalek = (atment / evfolyam_lett) * 100
        print(f"Átment: {atment} fő, {atment_szazalek:.2f}%")
    else:
        print("Nincsenek adatok az évfolyamról.")

def main():
    fajlnev = "pontszam_hibas.txt"
    # pontszamok = beolvas(fajlnev)
    pontszamok = beolvas_hibara(fajlnev)
    statisztika = stat(pontszamok)
    stat_kiir(statisztika)

main()