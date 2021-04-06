import os
from cryptography.fernet import Fernet


class SymetricEncrypter:

    @staticmethod
    def generate_random_key() -> hex:
        """Symmetrically generate a random key

        :return: randomly generated key
        """

        key = Fernet.generate_key()
        return key.hex()
