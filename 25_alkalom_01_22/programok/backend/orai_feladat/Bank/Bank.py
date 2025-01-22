from o_25_alkalom_01_22.backend.orai_feladat.Accountable.Accountable import Accountable


class Bank(Accountable):
    """
    TODO: account_number példányváltozó (?)
    TODO: account_number check -> def
    TODO: property
    Represents a bank managing customer accounts.
    """

    def __init__(self) -> None:
        """
        Initialize the Bank with an empty dictionary of customers.
        """
        self.customers: dict[str, float] = {}

    def create_account(self, account_number: str, initial_balance: float = 0) -> None:
        """
        Create a new bank account if it does not already exist.

        :param account_number: The unique identifier for the account.
        :param initial_balance: The initial balance for the account.
        """
        if account_number in self.customers:
            print("Account already exists")
        else:
            self.customers[account_number] = initial_balance
            print("Account created")

    def make_deposit(self, account_number: str, amount: float) -> None:
        """
        Deposit money into an account.

        :param account_number: The unique identifier for the account.
        :param amount: The amount to deposit.
        """
        if account_number in self.customers:
            self.customers[account_number] += amount
        else:
            print("Account number does not exist")

    def make_withdrawal(self, account_number: str, amount: float) -> None:
        """
        Withdraw money from an account if sufficient funds are available.

        :param account_number: The unique identifier for the account.
        :param amount: The amount to withdraw.
        """
        # TODO: account_number check
        if account_number in self.customers:
            if self.customers[account_number] >= amount:
                self.customers[account_number] -= amount
                print("Withdrawal successful")
            else:
                print("Not enough money")
        else:
            print("Account number does not exist")

    def check_balance(self, account_number: str) -> None:
        """
        Print the balance of a specified account.

        :param account_number: The unique identifier for the account.
        """
        if account_number in self.customers:
            balance = self.customers[account_number]
            print(f'Balance: {balance}')
        else:
            print("Account number does not exist")
