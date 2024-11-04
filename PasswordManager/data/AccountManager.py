"""Account Manager class.

Creates and manages the accounts by using a 
List[Account]

Author: Mason Pride
Version: 0.1
"""
from typing import List
from PasswordManager.data.Account import Account
from PasswordManager.data.FileHandler import FileHandler


class AccountManager():
    """Account Manager class."""
    
    def __init__(self) -> None:
        self.__account_list: List[Account] = []
        self.__file_handler = FileHandler("AccountInfo.txt", b'ize-EjWncqijjNMgJsdhuHxm3o5xC4W1tZ9MRAH2Uog=')
        content = self.__file_handler.read()
        content = content.split("\n")
        for account in content:
            account_split = account.split(" ")
            self.__account_list.append(Account(account_split[0], account_split[1], account_split[2]))

    @property
    def account_list(self) -> List[Account]:
        """Getter for account list attribute"""
        return self.__account_list

    def add_account(self, account: Account) -> None:
        """Adds account to account list"""
        self.__account_list.append(account)
        self.__file_handler.write(str(account))

    def __str__(self) -> str:
        """String override method"""
        output = ""
        for account in self.__account_list:
            output += str(account)
            output += "\n"
        return output
