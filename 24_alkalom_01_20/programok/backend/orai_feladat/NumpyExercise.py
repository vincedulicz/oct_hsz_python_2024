import numpy as np
import matplotlib.pyplot as plt


class NumpyFeladatok:
    @staticmethod
    def matrix_manipulacio():
        """
        A függvény egy 4x4-es véletlenszerű egész számokból készült mátrixot generál,
        és kiírja annak főátlójának összegét, valamint a transzponáltját.
        """
        matrix = np.random.randint(1, 101, size=(4, 4))  # Paraméter: size=(4, 4) - a mátrix mérete
        print("4x4-es mátrix:\n", matrix)
        print("Főátló összege:", np.trace(matrix))
        print("Mátrix transzponáltja:\n", matrix.T)

    @staticmethod
    def vektor_muveletek():
        """
        A függvény két 6 elemű véletlenszerű vektort generál, és elvégzi rajtuk
        az összeadást, kivonást, valamint az elemenkénti szorzást.
        """
        v1 = np.random.randint(0, 51, size=6)  # Paraméter: size=6 - a vektor hossza
        v2 = np.random.randint(0, 51, size=6)  # Paraméter: size=6 - a vektor hossza
        print("Vektor 1:", v1)
        print("Vektor 2:", v2)
        print("Összeg:", v1 + v2)
        print("Különbség:", v1 - v2)
        print("Elemenkénti szorzat:", v1 * v2)

    @staticmethod
    def adathalmaz_statisztika():
        """
        A függvény egy 100 elemű véletlenszerű adathalmazt generál, és kiírja
        annak átlagát, mediánját, szórását, valamint a maximumot és minimumot.
        """
        data = np.random.randint(1, 101, size=100)  # Paraméter: size=100 - az adathalmaz mérete
        print("Adathalmaz:", data)
        print("Átlag:", np.mean(data))
        print("Medián:", np.median(data))
        print("Szórás:", np.std(data))
        print("Maximum:", np.max(data))
        print("Minimum:", np.min(data))

    @staticmethod
    def maszkolas():
        """
        A függvény egy 10 elemű véletlenszerű adatokat tartalmazó tömböt generál,
        majd minden páratlan számot 0-ra módosít.
        """
        data = np.random.randint(1, 101, size=10)  # Paraméter: size=10 - a tömb hossza
        print("Eredeti tömb:", data)
        data[data % 2 != 0] = 0
        print("Maszkolt tömb (páratlanok 0):", data)

    @staticmethod
    def matrix_szorzasa():
        """
        A függvény két 3x3-as véletlenszerű mátrixot generál, majd kiszámolja
        azok szorzatát.
        """
        m1 = np.random.randint(1, 11, size=(3, 3))  # Paraméter: size=(3, 3) - a mátrix mérete
        m2 = np.random.randint(1, 11, size=(3, 3))  # Paraméter: size=(3, 3) - a mátrix mérete
        print("Mátrix 1:\n", m1)
        print("Mátrix 2:\n", m2)
        print("Mátrixszorzat:\n", np.dot(m1, m2))

    @staticmethod
    def felteteles_modositas():
        """
        A függvény egy 5x5-ös véletlenszerű mátrixot generál, majd minden olyan
        elemet, amely nagyobb, mint 50, 100-ra módosít.
        """
        matrix = np.random.randint(1, 101, size=(5, 5))  # Paraméter: size=(5, 5) - a mátrix mérete
        print("Eredeti mátrix:\n", matrix)
        matrix[matrix > 50] = 100
        print("Módosított mátrix:\n", matrix)

    @staticmethod
    def sinus_koszinus_gorbe():
        """
        A függvény egy sinus és egy koszinusz görbét ábrázol 0 és 2π között.
        """
        x = np.arange(0, 2 * np.pi, 0.1)  # Paraméter: 0 és 2π közötti értékek lépésköze 0.1
        sin_vals = np.sin(x)
        cos_vals = np.cos(x)
        plt.plot(x, sin_vals, label='Sinus')
        plt.plot(x, cos_vals, label='Koszinusz')
        plt.legend()
        plt.title("Sinus és Koszinusz görbék")
        plt.show()

    @staticmethod
    def sor_oszlop_atlag():
        """
        A függvény egy 6x6-os véletlenszerű mátrixot generál, és kiírja
        annak soronkénti és oszloponkénti átlagát.
        """
        matrix = np.random.randint(1, 101, size=(6, 6))  # Paraméter: size=(6, 6) - a mátrix mérete
        print("Mátrix:\n", matrix)
        print("Sorok átlaga:", np.mean(matrix, axis=1))
        print("Oszlopok átlaga:", np.mean(matrix, axis=0))
