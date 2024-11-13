

def collatz_iter(start):
    if start <= 0:
        raise ValueError("A kezdőérték nem lehet 0")

    steps = 0
    current = start
    sequence = [current]

    while current != 1:
        if current % 2 == 0:
            current //= 2
        else:
            current = 3 * current + 1
        sequence.append(current)
        steps += 1

    return sequence, steps


def collatz_recursive(start, steps=0):
    if start <= 0:
        raise ValueError("a kezdő nem lehet 0")

    print(start, end=" ")

    if start == 1:
        return steps

    if start % 2 == 0:
        return collatz_recursive(start // 2, steps + 1)
    else:
        return collatz_recursive(3 * start + 1, steps + 1)


def main():
    start_value = int(input("kezdő: "))
    print(collatz_recursive(start_value))
    print(collatz_iter(start_value))

main()