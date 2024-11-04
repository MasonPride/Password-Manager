"""Sample Main Project File.

This file is executed when the entire src directory is run using Python
and serves as the main entry point for the application.

Usage:
    python3 -m PasswordManager - execute this program (when run from project root).

Author: Mason Pride 
Date: 10/29/2024
"""

import sys
from PasswordManager.Main import Main
#print("In /PasswordManager/__main__.py")
Main.main(sys.argv)