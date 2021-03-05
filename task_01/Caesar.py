
import string

class CaesarCoder:

    def __init__(self, stride=3):
        self.stride = stride

    def encode(self, str_in):

        str_out = ''
        
        for i in range(len(str_in)):
            c = str_in[i]
            
            #   IF SPACE, SKIP
            if ord(c) == 32:
                str_out += ' '
                continue

            #   END IF INVALID INPUT
            if c.isalpha() == False:
                print('Invalid character in input string at index:',i)
                return ''

            #   ENCRYPT UPPERCASE
            if c.isupper():
                str_out += chr((ord(c) + self.stride - 65) % 26 + 65)
            #   ENCRYPT LOWERCASE
            else:
                str_out += chr((ord(c) + self.stride - 97) % 26 + 97)

        return str_out
    
    def decode(self, str_in):
        str_out = ''

        for i in range(len(str_in)):
            c = str_in[i]

            #   IF SPACE, SKIP
            if ord(c) == 32:
                str_out += ' '
                continue

            #   END IF INVALID INPUT
            if c.isalpha() == False:
                print('Invalid character in input string at index:',i)
                return ''

            #   DECRYPT UPPERCASE
            if c.isupper():
                str_out += chr((ord(c) - self.stride - 65) % 26 + 65)
            #   DECRYPT LOWERCASE
            else:
                str_out += chr((ord(c) - self.stride - 97) % 26 + 97)

        return str_out