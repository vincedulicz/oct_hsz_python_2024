import numpy as np
import pandas as pd
from datetime import datetime


class PandasFeladatok:
    @staticmethod
    def dataframe_letrehozasa():
        """
        A függvény egy DataFrame-et hoz létre, amely tartalmazza a személyek
        nevét, életkorát és pontszámát. Majd kiszámolja az átlagpontszámot és
        kiszűri a jobb pontszámú adatokat.
        """
        df = pd.DataFrame({"Név": ["Anna", "Béla", "Cecil"], "Életkor": [25, 30, 22], "Pontszám": [85, 92, 78]})
        print("DataFrame:\n", df)
        atlag_pontszam = df["Pontszám"].mean()
        print("Átlagpontszám:", atlag_pontszam)
        szurt = df[df["Pontszám"] > atlag_pontszam]
        print("Átlagnál jobb pontszámok:\n", szurt)

    @staticmethod
    def csv_beolvasas():
        """
        A függvény egy DataFrame-t hoz létre a megadott adatokból és kiírja
        a sorok számát, a pontszámok oszlopának maximumát, minimumát és átlagát.
        """
        df = pd.DataFrame({
            "Név": ["Anna", "Béla", "Cecil"],
            "Kor": [25, 30, 22],
            "Pontszám": [85, 92, 78]
        })
        print("DataFrame:\n", df)
        print("Sorok száma:", len(df))
        print("Pontszám oszlop max:", df["Pontszám"].max())
        print("Pontszám oszlop min:", df["Pontszám"].min())
        print("Pontszám oszlop átlag:", df["Pontszám"].mean())

    @staticmethod
    def csoportositas():
        """
        A függvény egy DataFrame-ben lévő adatokat csoportosítja a kategóriák
        szerint, majd kiszámítja az átlagokat.
        """
        df = pd.DataFrame({
            "Kategória": ["A", "A", "B", "B"],
            "Érték": [10, 20, 30, 40]
        })
        print("Csoportosított átlagok:\n", df.groupby("Kategória").mean())

    @staticmethod
    def hianyzo_kezeles():
        """
        A függvény egy DataFrame-ben lévő hiányzó adatokat kitölti az oszlopok
        átlagával.
        """
        df = pd.DataFrame({"A": [1, 2, None], "B": [None, 5, 6]})
        print("Eredeti DataFrame:\n", df)
        df_filled = df.fillna(df.mean())
        print("Hiányzó értékek kitöltve:\n", df_filled)

    @staticmethod
    def idosor_elemzes():
        """
        A függvény egy idősort generál, ahol a dátumok és az értékek szerepelnek,
        és kiszámolja a mozgó átlagot 3 elemre.
        """
        dates = pd.date_range(start=datetime.today(), periods=10)  # Paraméter: periods=10 - 10 dátum generálása
        values = np.random.randint(1, 101, size=10)
        df = pd.DataFrame({"Dátum": dates, "Érték": values})
        df["Mozgó átlag"] = df["Érték"].rolling(window=3).mean()
        print("Idősor mozgó átlaggal:\n", df)

    @staticmethod
    def felteteles_szures():
        """
        A függvény egy DataFrame-ben kiszűri azokat az adatokat, ahol az "A" oszlop
        értéke nagyobb, mint 15.
        """
        df = pd.DataFrame({"A": [10, 20, 30], "B": [5, 15, 25]})
        szurt = df[df["A"] > 15]
        print("Szűrt DataFrame:\n", szurt)

    @staticmethod
    def adatok_modositasa():
        """
        A függvény egy DataFrame-ben lévő adatokat kétszerez.
        """
        df = pd.DataFrame({"Érték": [10, 20, 30]})
        print("Eredeti DataFrame:\n", df)
        df["Érték"] *= 2
        print("Módosított DataFrame:\n", df)

    @staticmethod
    def adatok_rendezese():
        """
        A függvény egy DataFrame-ben lévő adatokat csökkenő sorrendbe rendezi
        az "Érték" oszlop alapján.
        """
        df = pd.DataFrame({"Érték": [30, 10, 20]})
        print("Rendezett DataFrame:\n", df.sort_values(by="Érték", ascending=False))
