import pytest
from Vigenere import VigenereCoder

coder = VigenereCoder('TEST')

def test_init():
    assert type(coder) is VigenereCoder

#   ENCODER

def test_encode():
    test_str = 'ABCDXYZ'
    assert coder.encode(test_str) == 'TFUWQCR'

def test_encode_long():
    #   https://www.lipsum.com
    test_str = 'LOREM IPSUM DOLOR SIT AMET CONSECTETUR ADIPISCING ELIT MAURIS AUGUE NISI SOLLICITUDIN ID SAGITTIS SED TRISTIQUE VEL IPSUM PROIN ALIQUAM LUCTUS MAURIS'
    assert coder.encode(test_str) == 'ESJXF MHLNQ VHESJ LBX SFXX UHGWWVMILNK EVBIMKVBRY XEML FTYJBL EMZNI FBLM KHEPAVBXMWBR AW LEYBMXAL LIV MKMKMBUMX OID BIWMF IVGBG EDBJYSF EYUMNW ETNVAL'

def test_encode_invalid_char():
    test_str = 'ab_34_$%'
    assert coder.encode(test_str) == 'ab_34_$%'


#   DECODER

def test_decode():
    test_str = 'TFUWQCR'
    assert coder.decode(test_str) == 'ABCDXYZ'

def test_decode_long():
    #   https://www.lipsum.com
    test_str = 'ESJXF MHLNQ VHESJ LBX SFXX UHGWWVMILNK EVBIMKVBRY XEML FTYJBL EMZNI FBLM KHEPAVBXMWBR AW LEYBMXAL LIV MKMKMBUMX OID BIWMF IVGBG EDBJYSF EYUMNW ETNVAL'
    assert coder.decode(test_str) == 'LOREM IPSUM DOLOR SIT AMET CONSECTETUR ADIPISCING ELIT MAURIS AUGUE NISI SOLLICITUDIN ID SAGITTIS SED TRISTIQUE VEL IPSUM PROIN ALIQUAM LUCTUS MAURIS'

def test_decode_invalid_char():
    test_str = 'ab_34_$%'
    assert coder.decode(test_str) == 'ab_34_$%'

#   --- 

def test_empty_str_in():
    with pytest.raises(AssertionError):
        test_str = ''
        coder.encode(test_str)

def test_cleartext_with_spaces():
    test_str = 'ABCD EFG H'
    assert coder.encode(test_str) == 'TFUW XJY A'

def test_generating_key():
    assert coder.generateKeyFromSecret('TEST ONE TWO THREE') == 'TEST TES TTE STTES'

def test_invalid_secret():
        with pytest.raises(AssertionError):
            coder = VigenereCoder('321')
