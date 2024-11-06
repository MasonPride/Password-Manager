"""Account class.

Creates the account object consisting of 
a platform, username, and password.

Author: Mason Pride
Version: 0.1
"""


class Account():
    """Account class.

    Creates the acount object.
    """
    def __init__(self, platform: str = None, username: str = None, password: str = None) -> None:
        """Account object Constructor.

        Args:
            platform: the platform (instagram, snapchat, facebook, etc.)
            username: the username of the platform
            password: the password of the platfrom
        """
        self.__platform: str = platform
        self.__username: str = username
        self.__password: str = password 
        
    @property
    def platform(self) -> str:
        """Platform getter method.

        Returns:
            str: Platform name
        """
        return self.__platform
    
    @platform.setter
    def platform(self, value: str) -> None:
        """Platform setter method.

        Args:
            value (str): Platform name
        """
        self.__platform = value

    @property
    def username(self) -> str:
        """Username getter method.

        Returns:
            str: Username
        """
        return self.__username
    
    @username.setter
    def username(self, value: str) -> None:
        """Username setter method.

        Args:
            value (str): Username
        """
        self.__username = value
    
    @property
    def password(self) -> str:
        """Password getter method.

        Returns:
            str: Password
        """
        return self.__password
    
    @password.setter
    def password(self, value: str) -> None:
        """Password setter method.

        Args:
            value (str): Password
        """
        self.__password = value

    def __str__(self) -> str:
        """String description sizes.

        Returns:
            string description
        """
        return str(self.platform) + " " + str(self.username) + " " + str(self.password)
    
    def __eq__(self, value: object) -> bool:
        """Equals override method.

        Args:
            value (object): Object to check if equals

        Returns:
            bool: True if equals; False otherwise
        """
        if isinstance(value, Account):
            return (self.__platform == value.platform and
                    self.__username == value.username and
                    self.__password == value.password)
        else:
            return False      
