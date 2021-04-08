from fastapi import FastAPI
from encrypting.encrypt_symmetric import SymetricEncrypter
from encrypting.encrypt_asymmetric import AsymmetricEncrypter
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

    return SE.generate_random_key()


@app.post('/symmetric/key')
def set_key_symmetric(key: str) -> bool:
    """Try to set symmetric key on the server.

    :param key: key in hexadecimal format provided by user
    :return: True if successfully saved the key, False if didn't
    :rtype: bool
    """

    try:
        SE.set_key(key)
    except ValueError:
        logger.info('Invalid key value entered.')
        return False
    else:
        return True


@app.post('/symmetric/encode')
def encode_symmetric(message: str) -> bytes:
    """Encodes message entered by user with symmetrical key set on server

    :param message: cleartext to be encoded
    :return: encoded message
    :rtype: bytes
    """

    try:
        result: bytes = SE.encode(message)
    except ValueError:
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

    try:
        result: bytes = SE.decode(message)
    except ValueError:
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
    """Get asymmetric keys saved on the server in OpenSSH format.

    :return: asymmetric keys in OpenSSH format
    :rtype: dict
    """
    try:
        return AE.get_keys_in_ssh_format()
    except ValueError:
        logger.info('You must first set the public and private key.')


@app.post('/asymmetric/key')
def set_keys_asymmetric(keys: dict) -> bool:
    """Try to set public and private asymmetric keys on the server.

    :param keys: public key and private key
    :return: True if successfully saved the key, False if didn't
    :rtype: bool
    """

    try:
        AE.set_keys(keys)
    except ValueError:
        logger.info('Invalid keys parameter value entered.')
        return False
    else:
        return True


@app.post('/asymmetric/sign')
def sign(message: str) -> bytes:
    """Give signature for message

    :param message: message of which the signature is created
    :return: signature for the message
    :rtype: bytes
    """

    try:
        return AE.sign_message(message)
    except ValueError:
        logger.info('Invalid input data or keys value on the server.')


@app.post('/asymmetric/verify')
def verify(message: str, signature: str) -> bool:
    """Verify message signature

    :param signature:
    :param message: message to verify
    :return: True if signature matches, False if it doesn't
    :rtype: bool
    """

    try:
        return AE.verify_message(message, signature)
    except ValueError:
        logger.info('Invalid input data or keys value on the server.')


@app.post('/asymmetric/encode')
def encode_asymmetric(message: str) -> bytes:
    """Encode message with asymmetric keys

    :param message: message to be encrypted
    :return: encrypted message
    :rtype: bytes
    """

    try:
        return AE.encode_message(message)
    except ValueError:
        logger.info('Invalid input data or keys value on the server.')


# # bugged
# @app.post('/asymmetric/decode')
# def decode_asymmetric(message: str) -> bytes:
#     """Decode message with asymmetric keys
#
#     :param message: message to be decrypted
#     :return: decrypted message
#     :rtype: bytes
#     """
#
#     try:
#         return AE.decode_message(message)
#     except ValueError:
#         logger.info('Invalid input data or keys value on the server.')
