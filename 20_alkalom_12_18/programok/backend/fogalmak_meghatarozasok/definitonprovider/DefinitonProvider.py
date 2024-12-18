from abc import ABC, abstractmethod


class DefinitonProvider(ABC):
    """ TODO: példányváltozó létrehozása a szükséges adattagokkal """

    """ Absztrakt osztály a def. kezelésére """


    @abstractmethod
    def get_definition(self):
        pass

    @abstractmethod
    def check_answear(self, user_answear: str, correct_answear: str) -> bool:
        pass