from abc import ABC, abstractmethod
from o_18_alkalom_12_11.hf.JarmuAlkatreszek.Motor import Motor
from o_18_alkalom_12_11.hf.JarmuAlkatreszek.Kerek import Kerekek


class Jarmu(ABC):
    def __init__(self, tipus: str, gyarto: str, evjarat: int, motor_tipus="V12", kerekek_szama=4):
        self._tipus = tipus
        self._gyarto = gyarto
        self.evjarat = evjarat
        # Kompozició: a motor és a kerekek a jármű részei
        self.motor = Motor(motor_tipus)
        self.kerekek = Kerekek(kerekek_szama)

    @property
    def tipus(self):
        return self._tipus

    @tipus.setter
    def tipus(self, new_tipus):
        self._tipus = new_tipus

    @property
    def gyarto(self):
        return self._gyarto


    def __str__(self) -> str:
        return f'{self.gyarto} - {self.tipus}'

    """def __del__(self):
        "" destuktor ""
        print("példány törölve")"""

    @abstractmethod
    def jarmu_adatok(self) -> dict:
        pass