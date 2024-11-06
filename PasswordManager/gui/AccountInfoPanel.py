"""Account Info Panel Class.

Creates the account info panel panel in our GUI.

Author: Mason Pride
Version: 0.1
"""
import tkinter as tk
from PasswordManager.data.Account import Account

class AccountInfoPanel(tk.Frame):
    """Account Info Frame."""
    
    def __init__(self, master, account: Account = None) -> None:
        """Creates the account info panel.

        Panel that handles inputting the account
        information parameters.

        Args:
            master (_type_): PrmaryWindow
            account (Account, optional): Account to be editted. Defaults to None.
        """
        self.__master = master
        tk.Frame.__init__(self, master=self.__master)
        self.grid_columnconfigure(0, weight=1)
        
        frame = tk.Frame(master=self)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid(row=0, column=0, sticky="EW")
        
        r = 0
        
        if account is None:
            self._account = Account()
        else:
            self._account = account
            old_plat_label = tk.Label(frame, text="Current Platform: " + str(account.platform))
            old_plat_label.grid(row=r, column=0, padx=5, pady=5, sticky="NSEW")
            
            r += 1

        platform_label = tk.Label(frame, text="Platform: ")
        platform_label.grid(row=r, column=0, padx=10, pady=10, sticky="NSEW")
        self.__platform_entry = tk.Entry(frame)
        self.__platform_entry.grid(row=r, column=1, padx=0, pady=10, sticky="NSEW")
        r += 1
        
        username_label = tk.Label(frame, text="Username: ")
        username_label.grid(row=r, column=0, padx=10, pady=10, sticky="NSEW")
        self.__username_entry = tk.Entry(frame)
        self.__username_entry.grid(row=r, column=1, padx=0, pady=10)
        r += 1
        
        password_label = tk.Label(frame, text="Password: ")
        password_label.grid(row=r, column=0, padx=10, pady=10, sticky="NSEW")
        self.__password_entry = tk.Entry(frame)
        self.__password_entry.grid(row=r, column=1, padx=0, pady=10)
        r += 1

        save_button = tk.Button(master=self, text="Save",
                            command=lambda:
                            self.action_performed("save"))
        save_button.grid(row=r, column=0, sticky="WE")
        r += 1

        cancel_button = tk.Button(master=self, text="Cancel",
                            command=lambda:
                            self.action_performed("cancel"))
        cancel_button.grid(row=r, column=0, sticky="WE")

    def action_performed(self, text: str):
        """Action performed method.

        Args:
            text (str): Representation of action
        """
        print(text)
        if text == "save":
            platform = self.__platform_entry.get()
            platform = platform.strip()
            
            username = self.__username_entry.get()
            username = username.strip()
            
            password = self.__password_entry.get()
            password = password.strip()

            self._account.platform = platform
            self._account.username = username
            self._account.password = password
            if platform and username and password:
                self.__master.save_account(self._account)
                self.destroy()
            else:
                print("Invalid parameters")
        if text == "cancel":
            self.destroy()