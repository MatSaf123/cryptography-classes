import pytest
from task_02_hash.src import HashFunctions as hf


def test_hash_from_file_success():
    assert hf.Hashing.hash_from_file('testfile') == 'ca9d384cf040ac0e47904c34b8d2554d729a6690a3c7806bc1950887a730e8c7'


def test_hash_file_doesnt_exist():
    with pytest.raises(FileNotFoundError):
        hf.Hashing.hash_from_file('thereisnosuchfile')


def test_hash_with_all_sha512_result():
    assert hf.Hashing.hash_with_all('teststring', False)[
               'sha512'] == '6253b39071e5df8b5098f59202d414c37a17d6a38a875ef5f8c7d89b0212b028692d3d2090ce03ae1de66c862fa8a561e57ed9eb7935ce627344f742c0931d72'

# def test_hash_from_file_ubuntu():
#     assert hf.Hashing.hash_from_file('D:/ubuntu-18.04.5-desktop-amd64.iso') == 'f295570badb09a606d97ddfc3421d7bf210b4a81c07ba81e9c040eda6ddea6a0'
