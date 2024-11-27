class A:
    def __init__(self):
        self.nev = "A"
        self._protected_tag = 0

    def _protected_method(self):
        return 0

    def __privat_methods(self):
        return "very private method"

    def kiir(self):
        return f"Ez a(z) {self.nev} osztály."

    @staticmethod
    def display():
        print("cool")

a = A()
print(a.kiir())
print(A.kiir(a))

A.display()

class B(A):
    def __init__(self):
        super().__init__()
        self.nev = "B"
        self._protected_tag = 1



class C(A):
    def __init__(self):
        super().__init__()
        self.nev = "C"

a = A()
b = B()

b._protected_method()

c = C()

print(f'a: {a.kiir()} b: {b.kiir()} c: {c.kiir()}')

# D osztály egyszerre örököl B és C osztályból
class D(B, C):
    def __init__(self):
        super().__init__()

"""
D -> B -> C -> A
"""



# Példányosítás
d = D()
print(d.kiir())  # Melyik osztály metódusa fut le?
print(D.mro())   # MRO-t megvizsgáljuk
