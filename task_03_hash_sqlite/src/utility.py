import hashlib as hl


class Hashing:
    """All hashing functionality."""

    @staticmethod
    def hash(password: str, salt: bytes) -> str:
        """"Hashes given password with pbkdf2_hmac.

        :param password: password to be hashed
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

    @staticmethod
    def check_if_hashed_passwords_match(password: str, user: list) -> bool:
        """Check if hashed logging data is correct when compared with database record.

        :param password: password entered by user
        :type password: str
        :param user: user data fetched from database
        :type user: list
        :return: boolean, if the passwords are the same
        :rtype: bool
        """

        return user[1] == Hashing.hash(password, user[2])
