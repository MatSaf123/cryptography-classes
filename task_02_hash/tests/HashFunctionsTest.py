import pytest
from task_02_hash.src import HashFunctions as hf

def test_hash_from_file_success():
    assert hf.hash_from_file('testfile') == 'ca9d384cf040ac0e47904c34b8d2554d729a6690a3c7806bc1950887a730e8c7'

def test_hash_file_doesnt_exist():
    with pytest.raises(FileNotFoundError):
        hf.hash_from_file('thereisnosuchfile')

def test_hash_with_all_result():
    assert hf.hash_with_all('teststring', False)[0] == 'eb2c1252ac1d7d684f1b474b207610aa58c62d2b335b9adeac269d4eab5bd2e7bfe2f6a7a51be61b4f55e5c7dfced6922ca66af2f5eddf8d539f4ca1a28c1232'

# def test_hash_from_file_ubuntu():
#     assert hf.hash_from_file('D:/ubuntu-18.04.5-desktop-amd64.iso') == 'f295570badb09a606d97ddfc3421d7bf210b4a81c07ba81e9c040eda6ddea6a0'
