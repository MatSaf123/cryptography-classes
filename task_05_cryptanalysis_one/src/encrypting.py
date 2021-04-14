# all encrypting logic


class Encrypter:

    @staticmethod
    def validate_cleartext(cleartext: str):
        """Checks if cleartext is not empty and alphabetical only.

        :param cleartext: cleartext to be validated
        """

        if not cleartext:
            raise ValueError('Cleartext cannot be empty.')
        elif not cleartext.isalpha():
            raise ValueError('Cleartext contains not allowed characters (allowed chars: a-z A-Z)')

    @staticmethod
    def encrypt(cleartext: str) -> str:
        """Encrypts cleartext with custom cipher

        TODO: implement encrypting

        :param cleartext: not encrypted text about to be encrypted
        :return: encrypted cleartext
        """

        return cleartext
