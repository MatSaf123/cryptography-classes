from cryptography.fernet import Fernet
from util import is_hexadecimal

class SymetricEncrypter:

    def __init__(self):
        self.__KEY = None

    def set_key(self, key: str) -> bool:
        """Validates and sets up symmetric key on server

        :param key: key in hexadecimal format provided by user
        :return: True if successfully saved the key, False if didn't
        :rtype: bool
        """

        if is_hexadecimal(key):
            self.__KEY = key
            return True
        else:
            return False

    def generate_random_key(self) -> str:
        """Generate a random key

        :return: randomly generated key
        :rtype: str (hexadecimal)
        """

        key = Fernet.generate_key()
        return key.hex()

    def encode(self, message: str) -> bytes:
        """Symmetrically encrypts cleartext

        :param message: cleartext entered by user
        :return: encrypted message
        :rtype: bytes
        """

        if self.__KEY is None:
            return b''
        else:
            f = Fernet(bytes.fromhex(self.__KEY))
            return f.encrypt(bytes(message, 'utf-8'))

    def decode(self, message) -> bytes:
        """Symmetrically decrypts encrypted text

        :param message: encrypted text entered by user
        :return: decrypted message
        :rtype: bytes
        """

        if self.__KEY is None:
            return b''
        else:
            f = Fernet(bytes.fromhex(self.__KEY))
            return f.decrypt(bytes(message, 'utf-8'))
