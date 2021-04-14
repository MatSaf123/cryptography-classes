import pytest
from src.encrypting import Encrypter


def test_valid_cleartext():
    # TODO: change later
    assert Encrypter.encrypt('abc') == 'abc'


def test_wrong_cleartext():
    with pytest.raises(ValueError):
        Encrypter.validate_cleartext('p83m')


def test_empty_cleartext():
    with pytest.raises(ValueError):
        Encrypter.validate_cleartext('')
