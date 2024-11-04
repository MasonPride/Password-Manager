"""Primary Window class.

Represents the Primary window

Author: Mason Pride
Date: 10/29/2024
"""
import tkinter as tk

from PasswordManager.data.Account import Account
from PasswordManager.gui.InfoPanel import InfoPanel
import tkinter as tk
from tkinter.ttk import Treeview, Scrollbar
from typing import Dict

class PrimaryWindow(tk.Tk):
    """Unlock Window"""
    def __init__(self) -> None:
        """Contrsucts the PrimaryWindow"""
        tk.Tk.__init__(self)
        self.minsize(width=200, height=400)
        self.title("Password Manager")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.__info_panel = InfoPanel(self)
        self.__info_panel.grid(row=0, column=0, rowspan=2, padx=10, pady=10, sticky="NSEW")
        
    def action_performed(self, text: str) -> None:
        print(text)
        if text == "Instagram":
            print(text.username)
