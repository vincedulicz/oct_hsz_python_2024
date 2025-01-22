class SuperSong(object):
    """ Super song I """
    def __init__(self):
        self._singsongsung: str = "https://youtu.be/qJW8gYZsroM?si=w3gX8F85Rl6Xa76a"

    def __str__(self):
        return f'Hm: {self.singsongsung}'

    @property
    def singsongsung(self):
        return self._singsongsung

    @singsongsung.setter
    def singsongsung(self, new_singsongsung):
        self._singsongsung = new_singsongsung


def main():
    hehe = SuperSong()
    print(hehe)


if __name__ == "__main__":
    main()
