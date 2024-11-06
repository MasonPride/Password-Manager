"""Account Manager class.

Creates and manages the accounts by using a 
List[Account].

Author: Mason Pride
Date: 10/29/24
"""
from typing import List
from PasswordManager.data.Account import Account
from PasswordManager.data.FileHandler import FileHandler
from typing import Dict


class AccountManager():
    """Account Manager class.
    
    Creates the account manager, in charge
    reading the conetent from AccountInfo.txt,
    and creating a list of all accounts
    """
    
    def __init__(self) -> None:
        """Constructor for AccountManager.
        
        Creates the account list, file handler,
        and reads content from the file.
        """
        self.__account_list: List[Account] = []
        self.__file_handler = FileHandler("AccountInfoTest.txt", b'ize-EjWncqijjNMgJsdhuHxm3o5xC4W1tZ9MRAH2Uog=')
        content = self.__file_handler.read()
        if content:
            content = content.split("\n")
            for account in content:
                account_split = account.split(" ")
                self.__account_list.append(Account(account_split[0], account_split[1], account_split[2]))
        else:
            print("File contents empty")

    @property
    def account_list(self) -> List[Account]:
        """Getter for account list attribute.
        
        Returns:
            List[Account] representing the account list"""
        return self.__account_list

    def add_account(self, account: Account) -> None:
        """Adds account to account list.
        
        Adds a desired account to the account list.
        
        Args:
            account: Account being added to list.
        """
        if account in self.__account_list:
            print("Already in account list")
        if account.platform != "" and account.username != "" and account.password != "":
            self.__account_list.append(account)
            self.__file_handler.write(str(account))
        else:
            print("Could not add account, invalid account settings")

    def __str__(self) -> str:
        """String override method."""
        output = ""
        for account in self.__account_list:
            output += str(account)
            output += "\n"
        return output
