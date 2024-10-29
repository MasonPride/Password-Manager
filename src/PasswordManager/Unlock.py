"""Class to unlock the manager

Author: Mason Pride
Date: 10/29/2024
"""
from src.PasswordManager.data.UnlockPIN import UnlockPIN

class Unlock():
    """Unlock class."""
    
    @staticmethod
    def unlock_manager() -> bool:
        user_input = input("Please enter the password: ")
        # Check if the entered password matches the correct password
        if user_input == UnlockPIN.PIN:
            print("Password correct! Access granted.")
            return True
            # Continue with the rest of the program here
        else:
            print("Incorrect password! Access denied.")
            return False
    