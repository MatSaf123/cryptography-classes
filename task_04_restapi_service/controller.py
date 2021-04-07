from fastapi import FastAPI
from encrypting.encrypt_symmetric import SymetricEncrypter
from encrypting.encrypt_asymmetric import AsymmetricEncrypter
from util import is_hexadecimal
import logging

logger = logging.getLogger('controller')
logging.basicConfig(level=logging.INFO)

app = FastAPI()

SE = SymetricEncrypter()
AE = AsymmetricEncrypter()


# symmetric endpoints

@app.get('/symmetric/key')
def get_random_key_symmetric() -> str:
    """Generates and returns a random symmetric key

    :return: randomly generated symmetric key
    :rtype: str (hexadecimal)
    """

    key = SE.generate_random_key()
    return key


@app.post('/symmetric/key')
def set_key_symmetric(key: str) -> bool:
    """Sets up symmetric key on server

    :param key: key in hexadecimal format provided by user
    :return: True if successfully saved the key, False if didn't
    :rtype: bool
    """

    if is_hexadecimal(key):
        SE.KEY = key
        return True
    else:
        return False


@app.post('/symmetric/encode')
def symmetric_encode(message: str) -> bytes:
    """Encodes message entered by user with symmetrical key set on server

    :param message: cleartext to be encoded
    :return: encoded message
    :rtype: bytes
    """

    try:
        assert SE.KEY is not None, 'Key value is not set'
    except AssertionError:
        logger.info('Set the key on the server before encoding a message.')
    else:
        return SE.encode(message)


@app.post('/symmetric/decode')
def symmetric_decode(message: str) -> bytes:
    """Decodes message entered by user with symmetrical key set on server

    :param message: encoded text to be decoded
    :return: decoded message
    :rtype: bytes
    """

    try:
        assert SE.KEY is not None
    except AssertionError:
        logger.info('Set the key on the server before decoding a message.')
    else:
        return SE.decode(message)


# asymmetric endpoints

@app.get('/asymmetric/key')
def get_random_keys_asymmetric() -> dict:
    """Generates and returns random public and private asymmetric keys

    :return: randomly generated asymmetric keys
    :rtype: dict
    """

    keys = AE.generate_random_keys()
    return keys