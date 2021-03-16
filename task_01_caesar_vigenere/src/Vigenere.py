class VigenereCoder:
    ALPHABET_SIZE = 26
    UPPERCASE_A_ASCII_CODE = 65

    @staticmethod
    def validate_input(cleartext: str, secret: str):
        assert cleartext != '', 'Input string cannot be empty.'
        assert secret != '', 'Secret cannot be empty.'
        assert secret.isalpha(), 'Secret must be alphabetical only.'
        assert secret.isupper(), 'Secret must be uppercase only.'

    @staticmethod
    def generate_key_from_secret(cleartext: str, secret: str) -> str:

        """
            Key generator, able to work with spaces
            in cleartext by adding spaces in key and
            maintaining order of characters using
            chars_skipped value. Returns a string
            key value.
        """

        encoded_chars = []
        skipped_chars = 0

        for i in range(len(cleartext)):
            if cleartext[i] == ' ':
                encoded_chars.append(cleartext[i])
                skipped_chars += 1
            else:
                encoded_chars.append(secret[(i - skipped_chars) % len(secret)])
        return ''.join(encoded_chars)

    @staticmethod
    def encode(cleartext: str, secret: str) -> str:

        """Encodes cleartext with Vigenere cipher."""

        VigenereCoder.validate_input(cleartext, secret)

        key = VigenereCoder.generate_key_from_secret(cleartext, secret)
        encoded_chars = []

        for i in range(len(cleartext)):
            c = cleartext[i]
            if c.isupper() and c.isalpha():
                encoded_chars.append(
                    chr((ord(c) + ord(key[i])) % VigenereCoder.ALPHABET_SIZE + VigenereCoder.UPPERCASE_A_ASCII_CODE))
            else:
                encoded_chars.append(c)
        return ''.join(encoded_chars)

    @staticmethod
    def decode(cleartext: str, secret: str) -> str:

        """Decodes encrypted text with Vigenere cipher."""

        VigenereCoder.validate_input(cleartext, secret)

        key = VigenereCoder.generate_key_from_secret(cleartext, secret)
        encoded_chars = []

        for i in range(len(cleartext)):
            c = cleartext[i]
            if c.isupper() and c.isalpha():
                encoded_chars.append(
                    chr((ord(c) - ord(key[i])) % VigenereCoder.ALPHABET_SIZE + VigenereCoder.UPPERCASE_A_ASCII_CODE))
            else:
                encoded_chars.append(c)
        return ''.join(encoded_chars)
