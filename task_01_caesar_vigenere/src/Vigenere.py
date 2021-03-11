

class VigenereCoder():
    ALPHABET_SIZE = 26
    UPPERCASE_A_ASCII_CODE = 65

    def __init__(self, secret):

        """
            Validates if secret is composed only of
            uppercase alphabetical characters.
        """

        assert secret != '', 'Secret cannot be empty.'
        assert secret.isalpha() and secret.isupper(), 'Secret must be uppercase-alphabetical only.'
        self.secret = secret

    def generateKeyFromSecret(self, str_in) -> str:

        """
            Key generator, able to work with spaces
            in cleartext by adding spaces in key and
            maintaining order of characters using
            chars_skipped value. Returns a string
            key value.
        """

        key = ''
        chars_skipped = 0
        for i in range(len(str_in)):
            if str_in[i] == ' ':
                key += str_in[i]
                chars_skipped += 1
            else:
                key += self.secret[(i - chars_skipped) % len(self.secret)]
        return key

    def encode(self, str_in: str) -> str:

        """
            Encodes cleartext with Vigenere cipher.
        """

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

        """
            Decodes encrypted text with Vigenere cipher.
        """

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
