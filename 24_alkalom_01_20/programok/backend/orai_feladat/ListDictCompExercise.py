class ListDictComp:
    @staticmethod
    def square_numbers():
        """
        A függvény kiszámítja az 1-től 20-ig terjedő számok négyzetét,
        és kiírja őket.
        """
        print("Négyzetek:", [x ** 2 for x in range(1, 21)])

    @staticmethod
    def even_numbers():
        """
        A függvény kiírja az 1-től 50-ig terjedő páros számokat.
        """
        print("Páros számok:", [x for x in range(1, 51) if x % 2 == 0])

    @staticmethod
    def filter_non_divisible_by_3():
        """
        A függvény kiírja az 1-től 20-ig terjedő számokat, amelyek nem oszthatók 3-mal.
        """
        print("Nem oszthatók 3-mal:", [x for x in range(1, 21) if x % 3 != 0])

    @staticmethod
    def dict_square():
        """
        A függvény egy szótárat készít az 1-től 10-ig terjedő számok négyzetével.
        """
        print("Szótár a négyzetekkel:", {x: x ** 2 for x in range(1, 11)})

    @staticmethod
    def update_dict():
        """
        A függvény létrehoz egy szótárat, majd hozzáad egy új kulcs-érték párt,
        és módosít egy meglévő értéket.
        """
        data = {"A": 10, "B": 20}
        data["C"] = 30  # új kulcs
        data["A"] = 100  # meglévő kulcs módosítása
        print("Módosított szótár:", data)

    @staticmethod
    def filter_dict():
        """
        A függvény egy szótárat készít, amely csak azokat a kulcsokat tartalmazza,
        amelyek értéke nagyobb, mint 15.
        """
        data = {"A": 10, "B": 20, "C": 30}
        szurt = {k: v for k, v in data.items() if v > 15}
        print("Szűrt szótár:", szurt)