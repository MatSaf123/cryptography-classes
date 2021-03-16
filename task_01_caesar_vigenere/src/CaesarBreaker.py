from Caesar import CaesarCoder as cc


class CaesarBreaker:

    @staticmethod
    def decipher_caesar_manual(encoded_text: str) -> str:
        """
            Takes encoded text, brute-force decrypts first part of it
            and lets user decide, which of the decrypted strings is the
            correct one. Then, decrypts the rest of text.
        """

        last_decrypted = cc.decode(encoded_text[0:20], 1)
        for i in range(cc.ALPHABET_SIZE):
            print(i + 1, ':', last_decrypted)
            last_decrypted = cc.decode(last_decrypted, 1)

        correct_stride = int(input('Which one is the correct one? (1-26): '))
        # print('Full text:', cc.decode(encoded_text, correct_stride))
        return cc.decode(encoded_text, correct_stride)

