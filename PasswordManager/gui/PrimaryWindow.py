"""Primary Window class.

Represents the Primary window

Author: Mason Pride
Date: 10/29/2024
"""
import tkinter as tk
from PasswordManager.data.Account import Account
from PasswordManager.gui.InfoPanel import InfoPanel
from tkinter.ttk import Treeview, Scrollbar
from typing import Dict


class PrimaryWindow(tk.Tk):
    """Unlock Window"""
    def __init__(self) -> None:
        """Contrsucts the PrimaryWindow"""
        tk.Tk.__init__(self)
        self.minsize(width=270, height=400)
        self.title("Password Manager")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.__main = None
        self.__info_panel = InfoPanel(self)
        self.__info_panel.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")
        
    def action_performed(self, text: str) -> None:
        print(text)
        if text == "Instagram":
            print(text.username)

    def load_info_panel(self) -> None:
        """Loads the menu panel."""
        self.load_panel(InfoPanel(self))

    def load_panel(self, panel):
        """Load panel.

        Loads the given panel.

        Args:
            panel: Panel to be loaded.
        """
        if self.__main is not None:
            self.__main.destroy()
        self.__main = panel
        self.__main.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")
        
    def save_account(self, account: Account) -> None:
        self.__info_panel.save_account(account)
        