import argparse


def main():
    parser = argparse.ArgumentParser(description="Argparse példa")

    # kötelező pozicionális argumentum
    parser.add_argument("nev", type=str, help="Add meg a neved")

    # opcionális argumentum
    parser.add_argument("-n", "--number", type=int, default=1, help="Az istmétlések száma")

    # lehetőségek
    parser.add_argument("operation", type=str,
                        choices=["add", "subtract", "multiply", "divide"]
                        )

    # forrásfájl
    parser.add_argument("--source", type=str, help="Forrás fájl neve")

    # célfájl
    parser.add_argument("--destination", type=str, help="Cél fájl neve")

    # debug
    parser.add_argument("--debug", action="store_true", help="Debug mód bekapcsolása")

    # argumentumok feldolgozása
    args = parser.parse_args()

    if args.debug:
        print("[DEBUG] Debug mód bekapcsolva")

    print(f'Helló, {args.nev}! A választott művelet {args.operation}')

    # fájlnévek kíírása
    if args.source and args.destination:
        print(f'Másolás innen: {args.source} ide: {args.destination}')

    #
    for _ in range(args.number):
        print(f'Művelet végrehajtása: {args.operation}')


if __name__ == "__main__":
    main()
