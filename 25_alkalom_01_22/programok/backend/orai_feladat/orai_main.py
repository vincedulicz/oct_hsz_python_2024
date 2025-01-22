from o_25_alkalom_01_22.backend.orai_feladat.Bank.Bank import Bank
from o_25_alkalom_01_22.backend.orai_feladat.Person.Person import Person
from o_25_alkalom_01_22.backend.orai_feladat.Shop.Shop import Shop


def main() -> None:
    """
    TODO: args kezelése
    Demonstrate the functionality of the Bank, Person, and Shop classes.
    """
    bank = Bank()

    person1 = Person("János", 30, "12345", "Magyarország")
    person1.greet()
    person1.open_bank_account(bank, initial_balance=1000)

    shop = Shop()
    shop.add_item("Laptop", 500)
    shop.add_item("Telefon", 300)
    shop.add_item("Drága", 100000)

    shop.buy_item(person1, bank, "Laptop")
    shop.buy_item(person1, bank, "Telefon")

    bank.check_balance(person1.account_number)

    shop.buy_item(person1, bank, "Drága")

    bank.check_balance(person1.account_number)


if __name__ == "__main__":
    main()
