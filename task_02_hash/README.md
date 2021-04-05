#   Hash functions part #1

###

- [x] Zaimplementuj hashowanie wszystkimi funkcjami zwracanymi przez algorithms_available z biblioteki hashlib wraz ze zwróceniem informacji o czasie hashowania dla danych wejściowych z konsoli.
- [x] Ściągnij duży plik (np. ubuntu) i sprawdź, czy hash się zgadza ([sprawdzone](https://github.com/MatSaf123/cryptography-classes/blob/master/task_02_hash/tests/HashFunctionsTest.py), test zakomentowany).
- [x] Zaimplementuj funkcję, która hashuje dowolny blik binarny z dysku. Sprawdź ją przez hashowanie obrazu ubuntu z pkt 2.
- [x] Za pomocą pakietu timeit zbadaj szybkość generowania hashy dla wiadomości o różnych rozmiarach. Przedstaw to na wykresie za pomocą matplotlib (mniej zalecane) czy plotly (zalecane).

## Usage:

#### Install required modules with:

```cmd
    pip install -r requirements.txt
```

### Importing functionalities
```py
import src.HashFunctions as hf
```

### Using functions

#### hash_with_all(str_in: str, display: bool = True)

- params: `str_in: str` (text input); `display: bool` (<b>True</b> if to display output logs)
- output: `d_out: dict` (dictionary filled with hashes, accessed by an algorithm name)
```py
hf.Hashing.hash_with_all('Helloworld')
h = hf.Hashing.hash_with_all('Helloworld', display = False)
md5_result = h['md5']
```
#### hash_from_file(str_in: str, display: bool = True)

- params: `str_in: str` (text input); `display: bool` (<b>True</b> if to display output logs)
- output: `out.hexdigest(): str` (hash returned as a string)
```py
hf.Hashing.hash_from_file('filename')
h = hf.Hashing.hash_from_file('filename', display = False)
hf.Hashing.hash_with_all('C:/file')
```
#### present_hash_time_for_strings(r: int = 30, algorithm: str = 'md5')

- params: `r: int` (number of strings, r is the length of max string); `algorithm: str` (name of one of the hash algorithms_available)
- output: none, results are displayed on a plot
```py
hf.Hashing.present_hash_time_for_strings()
hf.Hashing.present_hash_time_for_strings(r=45, algorithm='sha256')
```
