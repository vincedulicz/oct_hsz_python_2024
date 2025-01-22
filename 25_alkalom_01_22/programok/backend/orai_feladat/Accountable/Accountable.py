from abc import ABC, abstractmethod


class Accountable(ABC):
    """
    TODO: account_number amount -> példányváltozó
    Abstract base class to define the interface for banking operations.
    """

    @abstractmethod
    def create_account(self, account_number: str, initial_balance: float = 0) -> None:
        """
        Create a new bank account.

        :param account_number: The unique identifier for the account.
        :param initial_balance: The initial balance for the account (default is 0).
        """
        pass

    @abstractmethod
    def make_deposit(self, account_number: str, amount: float) -> None:
        """
        Deposit money into an account.

        :param account_number: The unique identifier for the account.
        :param amount: The amount to deposit.
        """
        pass

    @abstractmethod
    def make_withdrawal(self, account_number: str, amount: float) -> None:
        """
        Withdraw money from an account.

        :param account_number: The unique identifier for the account.
        :param amount: The amount to withdraw.
        """
        pass

    @abstractmethod
    def check_balance(self, account_number: str) -> None:
        """
        Check the balance of an account.

        :param account_number: The unique identifier for the account.
        """
        pass
