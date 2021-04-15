# main

from src.encrypting import Encrypter

if __name__ == '__main__':
    en = Encrypter()
    text = 'Some test message'
    print('Cleartext:', text)
    cipher = en.encrypt(text)
    print('Encrypted text:', cipher)
    print('Decrypted text:', en.decrypt(cipher))