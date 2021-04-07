from fastapi import FastAPI
from encrypting.encrypt_symmetric import SymetricEncrypter
import logging

logger = logging.getLogger('controller')
logging.basicConfig(level=logging.INFO)

app = FastAPI()

SE = SymetricEncrypter()


# symmetric endpoints

@app.get('/symmetric/key')
def get_random_key_symmetric() -> str:
    """Generate and return randomly generated symmetric key

    :return: randomly generated symmetric key
    """

    key = SE.generate_random_key()
    return key


@app.post('/symmetric/key')
def set_key_symmetric(key: str) -> bool:
    """Set the symmetric key on the server

    :param key: key provided in hexadecimal format
    :return:
    """
    try:
        int(key, 16)    # raise ValueError if cannot convert from hex to int
        SE.KEY = key
    except ValueError:
        logger.info('Provided key value is not in hexadecimal format.')
        return False
    except Exception:
        logger.info('There was an error, try to enter different key value.')
        return False
    else:
        return True


