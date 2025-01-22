from o_25_alkalom_01_22.backend.orai_feladat.Accountable.Accountable import Accountable
from o_25_alkalom_01_22.backend.orai_feladat.Person.Person import Person


class Shop:
    """
    TODO: adathalmaz tárolása -> elektornikai eszköz -> .... porszívó -> 10000
    Represents a shop with an inventory of items available for purchase.
    """

    def __init__(self) -> None:
        """
        Initialize the Shop with an empty inventory.
        """
        self.invetory: dict[str, float] = {}

    def add_item(self, item_name: str, price: float) -> None:
        """
        Add an item to the shop's inventory.

        :param item_name: The name of the item.
        :param price: The price of the item.
        """
        self.invetory[item_name] = price

    def buy_item(self, person: Person, bank: Accountable, item_name: str) -> None:
        """
        Allow a person to buy an item from the shop if they have sufficient funds.

        :param person: The person attempting to buy the item.
        :param bank: An instance of a class implementing the Accountable interface.
        :param item_name: The name of the item to purchase.
        """
        if item_name not in self.invetory:
            print(f'{item_name} nem kapható')
        elif not person.account_number:
            print(f'{person.name} nem rendelkezik számlával')
        else:
            price = self.invetory[item_name]
            if bank.customers.get(person.account_number, 0) >= price:
                bank.make_withdrawal(person.account_number, price)
                print(f'{person.name} megvette a(z) '
                      f'{item_name} terméket {price} áron')
            else:
                print("Nincs elegendő egyenleg...")
