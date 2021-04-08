from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from util import is_hexadecimal

class AsymmetricEncrypter:

    def __init__(self):
        self.__KEYS = {}

    def generate_random_keys(self) -> dict:
        """Generate and return random private and public asymmetric keys.

        :return: public and private asymmetric keys.
        :rtype:
        """

        priv_key_temp = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        publ_key_temp = priv_key_temp.public_key()

        private_key = priv_key_temp.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

        public_key = publ_key_temp.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        return {
            'private_key': private_key.hex(),
            'public_key': public_key.hex()
        }

    def set_keys(self, keys: dict) -> bool:
        """Validates input nad set public key and private key values.

        :param keys: public key and private key values
        :return: True if successfully saved keys, False if didn't
        :rtype: bool
        """

        public_key = keys['public_key']
        private_key = keys['private_key']

        if not public_key or not private_key:
            return False
        elif not is_hexadecimal(public_key) or not is_hexadecimal(public_key):
            return False
        else:
            self.__KEYS = keys
            return True

    def get_keys_in_ssh_format(self) -> dict:
        """Returns public key and private key saved in OpenSSH format.

        :return: public key, private key
        :rtype: dict
        """

        publ: str = 'x'
        priv: str = 'd'

        return {
            'public_key': publ,
            'private_key': priv
        }
