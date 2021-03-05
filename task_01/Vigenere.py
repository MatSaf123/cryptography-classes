import string

class VigenereCoder():
    
    ALPHABET_SIZE = 26
    UPPERCASE_A_ASCII_CODE = 65

    def __init__(self, secret):
        assert secret != '', 'Secret cannot be empty.'
        assert secret.isalpha() and secret.isupper(), 'Secret must be uppercase-alphabetical only.'
        self.secret = secret

    def generateKeyFromSecret(self, str_in) -> str:
        #   THIS GENERATOR WORKS WITH SPACES IN CLEARTEXT
        #   FOR EVERY SPACE ENCOUNTERED, INCREASE CHARS_SKIPPED COUNTER BY ONE
        #   CHARS_SKIPPED IS LATER USED TO MAINTAIN SECRET-CHARS ORDER
        key = ''
        chars_skipped = 0
        for i in range(len(str_in)):
            if str_in[i] == ' ':
                key += str_in[i]
                chars_skipped += 1
            else:
                key += self.secret[(i-chars_skipped) % len(self.secret)]                 
        return key

    def encode(self, str_in: str) -> str:
        
        assert str_in != '', 'Input string cannot be empty.'
        
        str_out = ''
        key = self.generateKeyFromSecret(str_in)
        for i in range(len(str_in)):
            c = str_in[i]
            if c.isupper() and c.isalpha():
                str_out += chr((ord(c) + ord(key[i])) % self.ALPHABET_SIZE + self.UPPERCASE_A_ASCII_CODE)
            else:
                str_out += c
        return str_out

    def decode(self, str_in: str) -> str:
        
        assert str_in != '', 'Input string cannot be empty.'
        
        str_out = ''
        key = self.generateKeyFromSecret(str_in)
        for i in range(len(str_in)):
            c = str_in[i]
            if c.isupper() and c.isalpha():
                str_out += chr((ord(c) - ord(key[i])) % self.ALPHABET_SIZE + self.UPPERCASE_A_ASCII_CODE)
            else:
                str_out += c
        return str_out

