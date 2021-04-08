from fastapi import FastAPI
from encrypting.encrypt_symmetric import SymetricEncrypter
from encrypting.encrypt_asymmetric import AsymmetricEncrypter
import logging
import json

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
    """Validates and sets up symmetric key on server

    :param key: key in hexadecimal format provided by user
    :return: True if successfully saved the key, False if didn't
    :rtype: bool
    """

    return SE.set_key(key)


@app.post('/symmetric/encode')
def encode_symmetric(message: str) -> bytes:
    """Encodes message entered by user with symmetrical key set on server

    :param message: cleartext to be encoded
    :return: encoded message
    :rtype: bytes
    """

    result: bytes = SE.encode(message)

    if result == b'':
        logger.info('You need to set up the key first before encoding anything.')
    else:
        return result


@app.post('/symmetric/decode')
def decode_symmetric(message: str) -> bytes:
    """Decodes message entered by user with symmetrical key set on server

    :param message: encoded text to be decoded
    :return: decoded message
    :rtype: bytes
    """

    result: bytes = SE.decode(message)

    if result == b'':
        logger.info('You need to set up the key first before decoding anything.')
    else:
        return result


# asymmetric endpoints

@app.get('/asymmetric/key')
def get_and_set_random_keys_asymmetric() -> dict:
    """Generates and returns random public and private asymmetric keys;
    saves them on the server.

    :return: randomly generated asymmetric keys
    :rtype: dict
    """

    keys = AE.generate_random_keys()
    AE.set_keys(keys)
    return keys


@app.get('/asymmetric/key/ssh')
def get_keys_in_ssh_format_asymmetric() -> dict:
    """TODO

    :return: asymmetric keys in OpenSSH format
    :rtype: dict
    """

    return {}
