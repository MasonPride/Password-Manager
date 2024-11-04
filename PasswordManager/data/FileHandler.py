from cryptography.fernet import Fernet


class FileHandler:
    def __init__(self, file_path: str, key: bytes = None):
        """
        Initializes the FileHandler with a file path and an encryption key.
        If no key is provided, a new key is generated.
        """
        self.file_path = file_path
        self.key = key or Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def write(self, content: str):
        """
        Encrypts the content and appends it to the file on a new line.
        """
        encrypted_content = self.cipher.encrypt(content.encode()) + b'\n'
        with open(self.file_path, 'ab') as file:
            file.write(encrypted_content)

    def read(self) -> str:
        """
        Reads the encrypted content from the file, decrypts each line, and returns it as a single string.
        """
        decrypted_content = []
        with open(self.file_path, 'rb') as file:
            for line in file:
                decrypted_line = self.cipher.decrypt(line.strip())
                decrypted_content.append(decrypted_line.decode())
        return "\n".join(decrypted_content)

    def get_key(self) -> bytes:
        """
        Returns the encryption key. This should be saved somewhere secure
        to decrypt the file later if needed.
        """
        return self.key

    def clear(self) -> None:
        open("AccountInfo.txt", "w").close()