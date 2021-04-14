# main

import logging
from src.encrypting import Encrypter

logger = logging.getLogger('main')
logging.basicConfig(level=logging.INFO)


def encrypt_text(cleartext: str) -> str:
    """Encrypts cleartext with custom cipher

    :param cleartext: not encrypted text about to be encrypted
    :return: encrypted cleartext
    """

    try:
        Encrypter.validate_cleartext(cleartext)
        cipher = Encrypter.encrypt(cleartext)
    except ValueError as e:
        logger.info(str(e))
    else:
        return cipher


if __name__ == '__main__':
    pass
