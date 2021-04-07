from cryptography.fernet import Fernet


class SymetricEncrypter:

    def __init__(self):
        self.KEY = None

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

        f = Fernet(bytes.fromhex(self.KEY))
        return f.encrypt(bytes(message, 'utf-8'))

    def decode(self, message) -> bytes:
        """Symmetrically decrypts encrypted text

        :param message: encrypted text entered by user
        :return: decrypted message
        :rtype: bytes
        """

        f = Fernet(bytes.fromhex(self.KEY))
        return f.decrypt(bytes(message, 'utf-8'))
