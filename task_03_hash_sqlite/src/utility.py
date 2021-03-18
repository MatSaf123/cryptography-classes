import hashlib as hl


class Hashing:
    """All hashing and encrypting functionality."""

    @staticmethod
    def encrypt(password: str, salt: bytes) -> str:
        """"Encrypts given password with pbkdf2_hmac.

        :param password: password to be encrypted
        :type password: str
        :param salt: random characters added at the end of password
        :type salt: bytes
        :return: hashed password
        :rtype: str
        """

        encrypted_password = hl.pbkdf2_hmac(
            'sha256',
            str.encode(password),
            salt,
            100000
        )
        return encrypted_password.hex()


