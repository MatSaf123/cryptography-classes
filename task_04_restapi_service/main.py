from fastapi import FastAPI
from encrypting.encrypt_symmetric import SymetricEncrypter

app = FastAPI()

SE = SymetricEncrypter()


# symmetric endpoints

@app.get('/symmetric/key')
def get_key_symmetric():
    key = SE.generate_random_key()
    return key
