"""Info Panel Class.

Creates the info panel in our GUI.

Author: Mason Pride
Version: 0.1
"""
import tkinter as tk
from tkinter import simpledialog
from tkinter.ttk import Treeview, Scrollbar
from typing import Dict
#from PasswordManager.data.AccountManager import AccountManager
from PasswordManager.data.Account import Account
from PasswordManager.gui.AccountInfoPanel import AccountInfoPanel


class InfoPanel(tk.Frame):
    """Creates the Info Panel.
    
    Args:
        tk (_type_): Frame
    """
    
    def __init__(self, master) -> None:
        """InfoPanel Constructor.

        Args:
            master (_type_): PrimaryWindow
        """
        self.__master = master
        tk.Frame.__init__(self, master=self.__master)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.__items: Dict[str, Account] = dict()
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
        
        add_button = tk.Button(master=self, text="Add Account",
                            command=lambda:
                            self.load_account_panel("add"))
        add_button.grid(row=2, column=0, sticky="NSEW")
        
        edit_button = tk.Button(master=self, text="Edit Account",
                            command=lambda:
                            self.action_performed("edit"))
        edit_button.grid(row=3, column=0, sticky="WE")
        
        delete_button = tk.Button(master=self, text="Delete Account",
                            command=lambda:
                            self.action_performed("delete"))
        delete_button.grid(row=4, column=0, sticky="WE")
            
    def load_account_panel(self, text: str, account: Account = None):
        """Loads an account panel.

        Loads the account panel with appropriate 
        account settings

        Args:
            text (str): _description_
            account (Account, optional): Account to open. Defaults to None.
        """
        self.__master.load_panel(AccountInfoPanel(self.__master))        
    
    def save_account(self, account: Account) -> None:
        """Save account method.

        Saves an instance of an account to our info panel.

        Args:
            account (Account): Instance of an account.
        """
        for account_id, value in self.__items.items():
            if account is value:
                self.__update_tree(account, account_id)
                return
        self.__items[self.__update_tree(account)] = account
    
    def __update_tree(self, account: Account, index: str = "end") -> str:
        """Updates the tree in our InfoPanel.

        Args:
            account (Account): Account
            index (str, optional): Current index. Defaults to "end".

        Returns:
            str: Index
        """
        if index == "end":
            index = self.__order_list.insert(parent="",
                                             index="end",
                                             text=str(account.platform))
        else:
            self.__order_list.item(index, text=str(account.platform))
            for child in self.__order_list.get_children(index):
                self.__order_list.delete(child)
        self.__order_list.item(index)
        self.__order_list.insert(parent=index, index="end", text="Username: " + str(account.username))
        self.__order_list.insert(parent=index, index="end", text="Password: " + str(account.password))
        return index
    
    def action_performed(self, text: str) -> None:
        """Action performed method.

        Args:
            text (str): Representation of action
        """
        print(text)
        if text == "edit":
            node = self.__order_list.focus()
            if node:
                while node not in self.__items:
                    node = self.__order_list.parent(node)
                account: Account = self.__items[node]
                if isinstance(account, Account):
                    self.__master.load_panel(AccountInfoPanel(self.__master, account))
        elif text == "delete":
            node = self.__order_list.focus()
            if node:
                while node not in self.__items:
                    node = self.__order_list.parent(node)
                del self.__items[node]
                self.__order_list.delete(node)
            