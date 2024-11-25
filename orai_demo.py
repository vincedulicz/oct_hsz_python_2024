import sys


def csv_orai():
    import csv

    with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Név', 'Kor', 'Város'])
        writer.writerows([['Anna', 25, 'Budapest'], ['Béla', 30, 'Szeged'], ['Csilla', 27, 'Debrecen']])

    with open('output.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

    with open('output_dict.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Név', 'Kor', 'Város']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()  # fejléc kiírása
        writer.writerow({'Név': 'Anna', 'Kor': 25, 'Város': 'Budapest'})

    with open('output_dict.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(type(row))
            print(row)
            print(f'név: {row["Név"]}, kor: {row["Kor"]}')


object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.my_dict = {}

    def __str__(self):
        return f'{self.name} {self.age}'

    def udvozles(self):
        print("üdv by " + self.name)



person = Person("Teszt Elek", 35)
print(person.name)

person_ = Person("Teszt Béla", 25)
print(person_.name)

print(f'person {person} : person_ {person_}')

person.udvozles()

class LAMPA:
    piros = 1
    sarga = 2
    sargazold = 3
    zold = 4


#print(LAMPA.piros)

global tesztelek

class Menu:
    kilepes = 0
    stat = 1
    kiiras = 2
    beolvas = 3

def stat():
    pass

while True:
    choice = input()
    if Menu.kiiras == choice:
        pass
    if Menu.stat == choice:
        stat()