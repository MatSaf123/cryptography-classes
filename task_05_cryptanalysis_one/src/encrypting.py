# all encrypting logic

import logging


class Encrypter:
    __ALPHABET_SIZE = 26
    __UPPERCASE_A_ASCII_CODE = 65

    logger = logging.getLogger('encrypter')
    logging.basicConfig(level=logging.INFO)

    def validate_cleartext(self, cleartext: str):
        """Checks if cleartext is not empty and alphabetical only.

        :param cleartext: cleartext to be validated
        """

        if not cleartext:
            raise ValueError('Cleartext cannot be empty.')
        elif not cleartext.isalpha():
            raise ValueError('Cleartext contains not allowed characters (allowed chars: a-z A-Z)')

    def encrypt(self, cleartext: str, format_text: bool = False) -> str:
        """Encrypts cleartext with custom cipher

        :param format_text: True if to force formatting (remove all commas, dots etc.)
        :param cleartext: text about to be encrypted
        :return: encrypted cleartext
        """

        # converts cleartext to uppercase, removes whitespaces
        cleartext = cleartext.upper().replace(' ', '')

        try:
            self.validate_cleartext(cleartext)
        except ValueError as e:

            if format_text:
                formatted_cleartext = []
                for c in cleartext:
                    if c.isalpha():
                        formatted_cleartext.append(c)
                    else:
                        continue
                cleartext = ''.join(formatted_cleartext)
            else:
                self.logger.info(str(e))
                return ''

        encrypted_chars: list = []

        for i in range(len(cleartext)):
            c = cleartext[i]

            stride = int((len(cleartext) - i) % self.__ALPHABET_SIZE)

            encrypted_chars.append(chr((ord(
                c) + stride - self.__UPPERCASE_A_ASCII_CODE) % self.__ALPHABET_SIZE + self.__UPPERCASE_A_ASCII_CODE))

        return ''.join(encrypted_chars)

    def decrypt(self, cipher: str) -> str:
        """Decrypts encrypted text

        :param cipher: encrypted text
        :return: decrypted text
        """

        decrypted_chars: list = []

        for i in range(len(cipher)):
            c = cipher[i]

            stride = int((len(cipher) - i) % self.__ALPHABET_SIZE)

            decrypted_chars.append(chr((ord(
                c) - stride - self.__UPPERCASE_A_ASCII_CODE) % self.__ALPHABET_SIZE + self.__UPPERCASE_A_ASCII_CODE))

        return ''.join(decrypted_chars)
