import base64
import hashlib
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature
from util import is_hexadecimal


class AsymmetricEncrypter:

    def __init__(self):
        self.__KEYS: dict = {
            'public_key': None,
            'private_key': None
        }

    def generate_random_keys(self) -> dict:
        """Generate and return random private and public asymmetric keys.

        :return: public and private asymmetric keys.
        :rtype:
        """

        priv_pem = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

        publ_pem = priv_pem.public_key()

        private_key = priv_pem.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.OpenSSH,
            encryption_algorithm=serialization.NoEncryption()
        )

        public_key = publ_pem.public_bytes(
            encoding=serialization.Encoding.OpenSSH,
            format=serialization.PublicFormat.OpenSSH
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

        new_public_key = keys['public_key']
        new_private_key = keys['private_key']

        if not new_public_key or not new_private_key:
            return False
        elif not is_hexadecimal(new_public_key) or not is_hexadecimal(new_private_key):
            return False
        else:
            self.__KEYS = keys
            return True

    def get_keys_in_ssh_format(self) -> dict:
        """Returns public key and private key saved in OpenSSH format.

        :return: public key, private key
        :rtype: dict
        """

        if self.__KEYS['public_key'] is None:
            return self.__KEYS
        else:
            publ: str = self.__KEYS['public_key']
            priv: str = self.__KEYS['private_key']

            return {
                'public_key': bytes.fromhex(publ),
                'private_key': bytes.fromhex(priv)
            }

    def sign_message(self, message: str) -> bytes:
        """Create a signature with use of secret key for message

        :param message: message of which the signature is created
        :return: signature for the message
        :rtype: bytes
        """

        if self.__KEYS['private_key'] is None:
            return b''

        private_key: bytes = bytes.fromhex(self.__KEYS['private_key'])

        key = serialization.load_ssh_private_key(
            private_key,
            password=None,
            backend=default_backend()
        )

        hashed_message = hashlib.sha256(message.encode('utf-8')).hexdigest()

        signature = key.sign(
            bytes(hashed_message.encode('ascii')),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256())

        return base64.b64encode(signature)

    def verify_message(self, message: str, signature: str) -> bool:
        """Verify message with it's signature and local public key.

        :param signature: signature for incoming message
        :param message: incoming message
        :return: True if match, False if not
        :rtype: bool
        """

        if self.__KEYS['public_key'] is None:
            raise ValueError('Key is not set')

        public_key: bytes = bytes.fromhex(self.__KEYS['public_key'])

        key = serialization.load_ssh_public_key(
            public_key,
            backend=default_backend()
        )

        decoded_signature = base64.b64decode(signature)

        prehashed_message = hashlib.sha256(message.encode('ascii')).hexdigest()

        try:
            key.verify(
                decoded_signature,
                bytes(prehashed_message.encode('ascii')),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH),
                hashes.SHA256())
        except InvalidSignature:
            return False
        else:
            return True
