def generate_mirror_numbers_iter(n):
    if n <= 0:
        return []

    start = 10 ** (n - 1)
    end = 10 ** n
    mirror_numbers = []

    for number in range(start, end):
        str_number = str(number)
        if str_number == str_number[::-1]:
            mirror_numbers.append(str_number)

    return mirror_numbers


def write_mirror_numbers_to_file_iter(n):
    mirror_numbers = generate_mirror_numbers_iter(n)

    with open("tukor_paros.txt", "w") as even_file, open("tukor_paratlan.txt", "w") as odd_file:
        for number in mirror_numbers:
            if int(number) % 2 == 0:
                even_file.write(number + "\n")
            else:
                odd_file.write(number + "\n")


def read_and_print_file_iter(file_name, count=None):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            if count is None:
                count = len(lines)
            print(f'Az első {count} elem a {file_name}-ból: ')

            for i, line in enumerate(lines[:count]):
                print(f"{i+1}: {line.strip()}")
    except FileNotFoundError:
        print("A fájl nem található")
    except Exception as e:
        print(f"valami más hiba: {e}")


def main():
    n = 4
    write_mirror_numbers_to_file_iter(n)

    print("\nPáros tükörszámok: ")
    read_and_print_file_iter("tukor_paros.txt", count=5)

    print("\nPáratlan tükörszámok: ")
    read_and_print_file_iter("tukor_paratlan.txt", count=5)


main()

