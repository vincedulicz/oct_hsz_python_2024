""" Programozási tételek I. """

def osszegzes():
    t = [3, 8, 2, 4, 5, 1, 6]

    osszeg = 0
    for num in t:
        osszeg = osszeg + num

    print("Összeg: ", osszeg)


def megszamlalas():
    t = [3, 8, 2, 4, 5, 1, 6]

    count = 0
    for num in t:
        if num > 5:
            count = count + 1

    print("5-nél nagyobb: ", count)


def eldontes():
    t = [3, 8, 2, 4, 5, 1, 6]

    n = len(t)
    ker = 5

    i = 0
    while i < n and t[i] != ker:
        i = i + 1

    if i < n:
        print("Van ilyen: ", ker)
    else:
        print("Nincs ilyen elem: ", ker)


def kivalasztas():
    t = [3, 8, 2, 4, 5, 1, 6]

    ker = 5

    i = 0
    while t[i] != ker:
        i = i + 1

    print("Hányadik helyen van: ", i + 1)


def linearis_kereses():
    t = [3, 8, 2, 4, 5, 1, 6]

    n = len(t)
    ker = 5

    i = 0
    while i < n and t[i] != ker:
        i = i + 1

    if i < n:
        print('Van ' + str(ker) + ' elem')
        print("Helye: ", i + 1)
    else:
        print('Nincs ' + str(ker) + ' elem!')


def kivalogatas():
    a = [3, 8, 2, 4, 5, 1, 6]
    b = []

    for elem in a:
        if elem < 5:
            b.append(elem)

    print(b)


def szetvalogatas():
    a = [3, 8, 2, 4, 5, 1, 6]
    b = []
    c = []

    for elem in a:
        if elem < 5:
            b.append(elem)
        else:
            c.append(elem)

    print(b)
    print(c)


def metszet():
    a = [5, 3, 6, 2, 1]
    b = [6, 2, 7, 8, 9]
    c = []
    n = len(b)

    for elem in a:
        print(elem)
        i = 0

        while i < n and elem != b[i]:
            print(f'b: {b[i]}')
            i += 1

        if i < n:
            c.append(elem)

    print(c)


def max_kivalaszas():
    t = [5, 3, 6, 2, 1]

    max_elem = t[0]
    for elem in t:
        if elem > max_elem:
            max_elem = elem

    print(max_elem)


def min_kivalaszas():
    t = [5, 3, 6, 2, 1]

    min_elem = t[0]
    for elem in t:
        if elem < min_elem:
            min_elem = elem

    print(min_elem)
