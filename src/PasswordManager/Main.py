"""Main class for PasswordManager.

This class will load and display the programs gui.

Author: Mason Pride
Date: 10/29/2024
"""
from typing import List
from src.PasswordManager.Unlock import Unlock
from src.PasswordManager.gui.PrimaryWindow import PrimaryWindow


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