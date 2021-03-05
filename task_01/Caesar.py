
import string

class CaesarCoder:

    ALPHABET_SIZE = 26
    UPPERCASE_A_ASCII_CODE = 65

    def __init__(self, stride: int = 3):
        self.stride = stride

    def encode(self, str_in: str) -> str:

        '''

        Encodes cleartext with Caesar cipher.

        '''

        assert str_in != '', 'Input string cannot be empty.'
        str_out = ''
        
        for i in range(len(str_in)):
            c = str_in[i]
            #   ENCRYPT IF UPPERCASE ALPHABETICAL
            if c.isupper() and c.isalpha():
                str_out += chr((ord(c) + self.stride - self.UPPERCASE_A_ASCII_CODE) % self.ALPHABET_SIZE + self.UPPERCASE_A_ASCII_CODE)
            #   IF NOT UPPERCASE/ALPHA, REWRITE CHAR
            else:
                str_out += c
        return str_out
    
    def decode(self, str_in: str) -> str:
        
        '''

        Decodes encrypted text with Caesar cipher.

        '''

        assert str_in != '', 'Input string cannot be empty.'
        str_out = ''
        
        for i in range(len(str_in)):
            c = str_in[i]
            #   ENCRYPT IF UPPERCASE ALPHABETICAL
            if c.isupper() and c.isalpha():
                str_out += chr((ord(c) - self.stride - self.UPPERCASE_A_ASCII_CODE) % self.ALPHABET_SIZE + self.UPPERCASE_A_ASCII_CODE)
            #   IF NOT UPPERCASE/ALPHA, REWRITE CHAR
            else:
                str_out += c

        return str_out