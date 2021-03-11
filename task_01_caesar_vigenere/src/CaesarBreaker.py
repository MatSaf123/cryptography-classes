from Caesar import CaesarCoder


class CaesarBreaker():

    def __init__(self):
        pass

    def decipherCaesar(self, str_in: str) -> str:
        """
            Takes encoded text, brute-force decrypts first part of it
            and lets user decide, which of the decrypted texts is the
            correct one.
        """

        coder = CaesarCoder(1)
        ALPHABET_SIZE = coder.ALPHABET_SIZE

        part_of_str = str_in[0:20]
        last = coder.decode(part_of_str)
        for i in range(ALPHABET_SIZE):
            print(i + 1, ':', last)
            last = coder.decode(last)
        x = int(input('Which one is the correct one? (1-26): '))

        coder = CaesarCoder(x)
        str_out = coder.decode(str_in)
        print('Full text:', str_out)
        return str_out


#   Lorem Ipsum - 'ORUHP LSVXP GRORU VLW DPHW FRQVHFWHWXU DGLSLVFLQJ HOLW PDXULV DXJXH QLVL VROOLFLWXGLQ LG VDJLWWLV VHG WULVWLTXH YHO LSVXP SURLQ DOLTXDP OXFWXV PDXULV'
ENCRYPTED_TEXT = input('Enter encrypted text: ')
cb = CaesarBreaker()
cb.decipherCaesar(ENCRYPTED_TEXT)
