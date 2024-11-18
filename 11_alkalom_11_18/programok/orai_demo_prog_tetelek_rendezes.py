t = [5, 3, 6, 3, 2, 1]


def buborek_rendezes(t):
    n = len(t)

    for i in range(n - 1, 0, -1):
        print(f'i: {i}')
        for j in range(0, i):
            # print(f'j: {j}')
            if t[j] > t[j + 1]:
                tmp = t[j + 1]
                t[j + 1] = t[j]
                t[j] = tmp

    print(t)


def rendezes_cserevel(t):
    n = len(t)

    for i in range(0, n - 1):
        print(f'i: {i}')
        for j in range(i + 1, n):
            if t[i] > t[j]:
                tmp = t[i]
                t[i] = t[j]
                t[j] = tmp
                print(f't[j]: {t[j]}')

    print(t)


def max_kivalasztas_rendezes(t):
    n = len(t)

    for i in range(n - 1, -1, -1):
        max_index = i
        for j in range(0, i):
            if t[j] > t[max_index]:
                print(f'max_index: {max_index}')
                max_index = j
        tmp = t[i]
        t[i] = t[max_index]
        t[max_index] = tmp

    print(t)


def min_kivalasztas_rendezes(t):
    n = len(t)

    for i in range(0, n - 1):
        min_index = i
        for j in range(i + 1, n):
            if t[j] < t[min_index]:
                min_index = j
        if min_index != i:
            tmp = t[i]
            t[i] = t[min_index]
            t[min_index] = tmp

    print(t)


def rendezes_beszurasssal(t):
    n = len(t)

    for i in range(0, n):
        kulcs = t[i]
        j = i - 1
        while j >= 0 and t[j] > kulcs:
            t[j + 1] = t[j]
            j -= 1
        t[j + 1] = kulcs

    print(t)


def shell_rendezes(t):
    h = [5, 3, 1]
    n = len(t)

    for k in range(0, 3):
        lepes = h[k]
        print(lepes)
        for j in range(lepes, n):
            i = j - lepes
            kulcs = t[j]
            while i >= 0 and t[i] > kulcs:
                t[i + lepes] = t[i]
                i -= lepes
            t[i + lepes] = kulcs

    print(t)


def gyors_rendezes(t):
    n = len(t)

    if n <= 1:
        return t

    kicsik = []
    egyenlo = []
    nagyok = []
    pivot = t[n-1]

    for num in t:
        if num < pivot:
            kicsik.append(num)
        if num == pivot:
            egyenlo.append(num)
        if num > pivot:
            nagyok.append(num)

    return gyors_rendezes(kicsik) + egyenlo + gyors_rendezes(nagyok)
