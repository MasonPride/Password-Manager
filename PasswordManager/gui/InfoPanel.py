"""Info Panel Class.

Creates the info panel panel in our GUI.

Author: Mason Pride
Version: 0.1
"""
import tkinter as tk
from tkinter import simpledialog
from tkinter.ttk import Treeview, Scrollbar
from typing import Dict
from PasswordManager.data.AccountManager import AccountManager
from PasswordManager.data.Account import Account


class InfoPanel(tk.Frame):
    
    def __init__(self, master) -> None:
        self.__master = master
        tk.Frame.__init__(self, master=self.__master)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        list_frame = tk.Frame(master=self)
        list_frame.grid_columnconfigure(0, weight=1)
        list_frame.grid_rowconfigure(0, weight=1)
        self.__order_list = Treeview(master=list_frame, show="tree",
                                     selectmode="browse")
        order_list_scrollbar = Scrollbar(master=list_frame, orient="vertical",
                                         command=self.__order_list.yview)
        self.__order_list.configure(yscrollcommand=order_list_scrollbar.set)
        self.__order_list.grid(row=0, column=0, sticky="NSEW")
        order_list_scrollbar.grid(row=0, column=1, sticky="NSE")
        list_frame.grid(row=0, column=0, columnspan=2, sticky="NSEW")
        
        new_button = tk.Button(master=self, text="Add Account",
                            command=lambda:
                            self.action_performed("add"))
        new_button.grid(row=2, column=0, sticky="NSEW")
        
        self.__account_manager = AccountManager()
        for info in self.__account_manager.account_list:
            self.__update_tree(info)
            
    def __update_tree(self, account: Account, index: str = "end") -> str:
        if index == "end":
        # new item
            index = self.__order_list.insert(parent="", index=index, text=str(account.platform))
        self.__order_list.item(index)
        self.__order_list.insert(parent=index, index="end", text="Username: " + str(account.username))
        self.__order_list.insert(parent=index, index="end", text="Password: " + str(account.password))
        return index

    def action_performed(self, text: str) -> None:
        print(text)
        if text == "add":
            platform = simpledialog.askstring("Platform", "What platform?")
            username = simpledialog.askstring("Username", "What your username?")
            password = simpledialog.askstring("Password", "What is your password?")
            new_account = Account(platform, username, password)
            self.__account_manager.add_account(new_account)
            self.__update_tree(new_account)
            