class CaesarCoder:

    ALPHABET_SIZE = 26
    UPPERCASE_A_ASCII_CODE = 65

    @staticmethod
    def encode(cleartext: str, stride: int) -> str:

        """Encodes cleartext with Caesar cipher."""

        assert cleartext != '', 'Input string cannot be empty.'

        encoded_chars = []
        for i in range(len(cleartext)):
            c = cleartext[i]
            if c.isupper() and c.isalpha():
                encoded_chars.append(chr((ord(
                    c) + stride - CaesarCoder.UPPERCASE_A_ASCII_CODE) % CaesarCoder.ALPHABET_SIZE + CaesarCoder.UPPERCASE_A_ASCII_CODE))
            else:
                encoded_chars.append(c)
        return ''.join(encoded_chars)

    @staticmethod
    def decode(encrypted_text: str, stride: int) -> str:

        """Decodes encrypted text with Caesar cipher."""

        assert encrypted_text != '', 'Input string cannot be empty.'

        decoded_chars = []
        for i in range(len(encrypted_text)):
            c = encrypted_text[i]
            if c.isupper() and c.isalpha():
                decoded_chars.append(chr((ord(
                    c) - stride - CaesarCoder.UPPERCASE_A_ASCII_CODE) % CaesarCoder.ALPHABET_SIZE + CaesarCoder.UPPERCASE_A_ASCII_CODE))
            else:
                decoded_chars.append(c)
        return ''.join(decoded_chars)
