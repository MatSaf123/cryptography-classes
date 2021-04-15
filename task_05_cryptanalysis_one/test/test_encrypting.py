import pytest
from src.encrypting import Encrypter

en = Encrypter()


def test_valid_cleartext_encrypt():
    assert en.encrypt('Some test message') == 'HCZQEOBBTKXWDIF'


def test_valid_cleartext_decrypt():
    assert en.decrypt('HCZQEOBBTKXWDIF') == 'SOMETESTMESSAGE'


def test_wrong_cleartext():
    with pytest.raises(ValueError):
        en.validate_cleartext('Z340')


def test_empty_cleartext():
    with pytest.raises(ValueError):
        en.validate_cleartext('')
