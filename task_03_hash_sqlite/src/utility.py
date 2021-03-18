import hashlib as hl


class Hashing:

    @staticmethod
    def encrypt(password: str, salt: bytes) -> str:
        encrypted_password = hl.pbkdf2_hmac(
            'sha256',
            str.encode(password),
            salt,
            100000
        )
        return encrypted_password.hex()
