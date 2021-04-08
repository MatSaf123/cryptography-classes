import os
from src.utility import Hashing as h


class User:

    def __init__(self, username: str, password: str):
        self.username = username
        self.salt = os.urandom(8)
        self.password = h.hash(password, self.salt)
