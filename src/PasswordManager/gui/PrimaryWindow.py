"""Primary Window class.

Represents the Primary window

Author: Mason Pride
Date: 10/29/2024
"""
import tkinter as tk

class PrimaryWindow(tk.Tk):
    """Unlock Window"""
    def __init__(self) -> None:
        """Contrsucts the PrimaryWindow"""
        tk.Tk.__init__(self)
        self.minsize(width=500, height=500)
        self.title("Password Manager")
        
