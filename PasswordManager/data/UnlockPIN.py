<<<<<<< HEAD:PasswordManager/data/UnlockPIN.py
"""Unlock PIN class

Changing this class will change the PIN
required to grant access to the Password Manager.

Author: Mason Pride
Date: 10/29/2024
"""
from enum import Enum


class UnlockPIN(str, Enum):
    """Set the desired PIN number here"""
=======
"""Unlock PIN class

Changing this class will change the PIN
required to grant access to the Password Manager.

Author: Mason Pride
Date: 10/29/2024
"""
from enum import Enum


class UnlockPIN(str, Enum):
    """Set the desired PIN number here"""
>>>>>>> e8fe7d370b317e60bdf7eb265efec038b6de25d6:src/PasswordManager/data/UnlockPIN.py
    PIN = "1111"