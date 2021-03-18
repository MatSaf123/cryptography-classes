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


class Verification:
    """All password verification functionality."""

    @staticmethod
    def verify_password(password: str, account: list) -> bool:
        """Check if hashed logging data is correct compared with database record.

        :param password:
        :type password: str
        :param account:
        :type account: list
        :return: boolean, if the passwords are the same
        :rtype: bool
        """

        return account[1] == Hashing.encrypt(password, account[2])
