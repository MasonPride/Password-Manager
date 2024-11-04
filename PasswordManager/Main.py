"""Main class for PasswordManager.

This class will load and display the programs gui.

Author: Mason Pride
Date: 10/29/2024
"""
from typing import List
from PasswordManager.Unlock import Unlock
from PasswordManager.gui.PrimaryWindow import PrimaryWindow
from PasswordManager.data.FileHandler import FileHandler
from PasswordManager.data.AccountManager import AccountManager
from PasswordManager.data.Account import Account

class Main:
    """Main Class."""

    @staticmethod
    def main(args: List[str]) -> None:
        """Main method."""
        unlock = Unlock().unlock_manager()
        if unlock:
            PrimaryWindow().mainloop()
        else:
            exit()
        #handler = FileHandler("AccountInfo.txt", b'ize-EjWncqijjNMgJsdhuHxm3o5xC4W1tZ9MRAH2Uog=')
        #handler.write("Instagram InstaUser InstaPassword")
        #handler.write(str(handler.get_key()))
        #text = handler.read()
        #print(text)
        #handler.clear()
        #accountMan = AccountManager()
        #print(accountMan)
        #accountMan.add_account(Account("Snapchat", "SnapUser", "SnapPassword"))
        #accountMan.remove_account(Account("Snapchat", "SnapUser", "SnapPassword"))
        #print(accountMan)
