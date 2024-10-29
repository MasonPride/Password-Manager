"""Unlock PIN class

Changing this class will change the PIN
required to grant access to the Password Manager.

Author: Mason Pride
Date: 10/29/2024
"""
from enum import Enum


class UnlockPIN(str, Enum):
    """Set the desired PIN number here"""
    PIN = "1111"
