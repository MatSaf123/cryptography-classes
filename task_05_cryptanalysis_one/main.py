# main

import sys
from src.encrypting import Encrypter
import logging

logger = logging.getLogger('main')
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    en = Encrypter()

    s1 = sys.argv[1]

    logger.info(en.encrypt(s1, format_text=True))
