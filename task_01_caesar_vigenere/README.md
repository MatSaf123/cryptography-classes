#   Caesar cipher, Vigenere cipher

### 

- [x] W dowolnym języku programowania wykonaj szyfrator i deszyfrator Cezara i Vigenere'a. Wersja konsolowa wystarczy. Miło byłoby, gdyby było jakieś fajne API, walidacja danych wejściowych, testy automatyczne.
- [x] Wykonaj manualny łamacz szyfru Cezara.
- [ ] Wykonaj automatyczny łamacz szyfru Cezara.


## Usage:
### Importing modules
```py
from src.Caesar import CaesarCoder as cc
from src.Vigenere import VigenereCoder as vc
from src.CaesarBreaker import CaesarBreaker as cb
```

### Using functions (CaesarCoder)

#### encode(cleartext: str, stride: int)

- params: `cleartext: str` (<b>uppercase</b> text to be encrypted); `stride: int` (shift value for the algorithm)
- output: `''.join(encoded_chars): str` (encoded cleartext)
```py
encoded_result = cc.encode(cleartext = 'ABCDXYZ', stride = 3)
```

#### decode(cleartext: str, stride: int)

- params: `encoded_text: str` (<b>uppercase</b> text to be decrypted); `stride: int` (shift value for the algorithm)
- output: `''.join(decoded_chars): str` (decoded encrypted_text)

```py
decoded_result = cc.decode(encoded_text='DEFGABC', stride=3)
```

### Using functions (VigenereCoder)

#### encode(cleartext: str, stride: int)

- params: `cleartext: str` (<b>uppercase</b> text to be encrypted); `secret: str` (<b>uppercase</b> string from which the [running key](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher#Running_key) is created)
- output: `''.join(encoded_chars): str` (encoded cleartext)
```py
encoded_result = vc.encode(cleartext = 'SAMPLESTRING', secret = 'CAT')
```

#### decode(cleartext: str, stride: int)

- params: `encoded_text: str` (<b>uppercase</b> text to be encrypted); `secret: str` (<b>uppercase</b> string from which the [running key](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher#Running_key) is created)
- output: `''.join(encoded_chars): str` (encoded cleartext)

```py
decoded_result = vc.decode(encoded_text='TFUWQCR', secret='TEST')
```

### Using functions (CaesarBreaker)

#### decipher_caesar_manual(encoded_text: str)
- params: `cleartext: str` (<b>uppercase</b> text to be encrypted); `secret: str` (<b>uppercase</b> string from which the [running key](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher#Running_key) is created)
- output: `cc.decode(encoded_text, correct_stride) :str` (decoded text)

After running function user has to choose the correct stride, after that program will return fully decrypted input text.

```py
cb.decipher_caesar_manual('XYZABC')
```

