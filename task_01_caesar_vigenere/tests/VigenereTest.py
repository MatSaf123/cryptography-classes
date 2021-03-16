import pytest
from task_01_caesar_vigenere.src.Vigenere import VigenereCoder


#   ENCODER

def test_encode():
    test_str = 'ABCDXYZ'
    assert VigenereCoder.encode(test_str, 'TEST') == 'TFUWQCR'


def test_encode_long():
    #   https://www.lipsum.com
    test_str = 'LOREM IPSUM DOLOR SIT AMET CONSECTETUR ADIPISCING ELIT MAURIS AUGUE NISI SOLLICITUDIN ID SAGITTIS SED TRISTIQUE VEL IPSUM PROIN ALIQUAM LUCTUS MAURIS'
    assert VigenereCoder.encode(test_str,
                                'TEST') == 'ESJXF MHLNQ VHESJ LBX SFXX UHGWWVMILNK EVBIMKVBRY XEML FTYJBL EMZNI FBLM KHEPAVBXMWBR AW LEYBMXAL LIV MKMKMBUMX OID BIWMF IVGBG EDBJYSF EYUMNW ETNVAL'


def test_encode_invalid_char():
    test_str = 'ab_34_$%'
    assert VigenereCoder.encode(test_str, 'TEST') == 'ab_34_$%'


#   DECODER

def test_decode():
    test_str = 'TFUWQCR'
    assert VigenereCoder.decode(test_str, 'TEST') == 'ABCDXYZ'


def test_decode_long():
    #   https://www.lipsum.com
    test_str = 'ESJXF MHLNQ VHESJ LBX SFXX UHGWWVMILNK EVBIMKVBRY XEML FTYJBL EMZNI FBLM KHEPAVBXMWBR AW LEYBMXAL LIV MKMKMBUMX OID BIWMF IVGBG EDBJYSF EYUMNW ETNVAL'
    assert VigenereCoder.decode(test_str,
                                'TEST') == 'LOREM IPSUM DOLOR SIT AMET CONSECTETUR ADIPISCING ELIT MAURIS AUGUE NISI SOLLICITUDIN ID SAGITTIS SED TRISTIQUE VEL IPSUM PROIN ALIQUAM LUCTUS MAURIS'


def test_decode_invalid_char():
    test_str = 'ab_34_$%'
    assert VigenereCoder.decode(test_str, 'TEST') == 'ab_34_$%'


#   ---

def test_empty_str_in():
    with pytest.raises(AssertionError):
        test_str = ''
        VigenereCoder.encode(test_str, 'TEST')


def test_cleartext_with_spaces():
    test_str = 'ABCD EFG H'
    assert VigenereCoder.encode(test_str, 'TEST') == 'TFUW XJY A'


def test_generating_key():
    assert VigenereCoder.generate_key_from_secret('TEST ONE TWO THREE', 'TEST') == 'TEST TES TTE STTES'


def test_invalid_secret():
    with pytest.raises(AssertionError):
        result = VigenereCoder.decode('somecleartext', '__invalid_secret__')
