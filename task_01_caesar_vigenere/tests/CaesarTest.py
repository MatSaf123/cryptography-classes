import pytest
from task_01_caesar_vigenere.src.Caesar import CaesarCoder

coder = CaesarCoder()


def test_init():
    assert type(coder) is CaesarCoder


#   ENCODER

def test_encode():
    test_str = 'ABCDXYZ'
    assert coder.encode(test_str) == 'DEFGABC'


def test_encode_long():
    #   https://www.lipsum.com
    test_str = 'LOREM IPSUM DOLOR SIT AMET CONSECTETUR ADIPISCING ELIT MAURIS AUGUE NISI SOLLICITUDIN ID SAGITTIS SED TRISTIQUE VEL IPSUM PROIN ALIQUAM LUCTUS MAURIS'
    assert coder.encode(
        test_str) == 'ORUHP LSVXP GRORU VLW DPHW FRQVHFWHWXU DGLSLVFLQJ HOLW PDXULV DXJXH QLVL VROOLFLWXGLQ LG VDJLWWLV VHG WULVWLTXH YHO LSVXP SURLQ DOLTXDP OXFWXV PDXULV'


def test_encode_invalid_char():
    test_str = 'ab_34_$%'
    assert coder.encode(test_str) == 'ab_34_$%'


#   DECODER

def test_decode():
    test_str = 'DEFGABC'
    assert coder.decode(test_str) == 'ABCDXYZ'


def test_decode_long():
    #   https://www.lipsum.com
    test_str = 'ORUHP LSVXP GRORU VLW DPHW FRQVHFWHWXU DGLSLVFLQJ HOLW PDXULV DXJXH QLVL VROOLFLWXGLQ LG VDJLWWLV VHG WULVWLTXH YHO LSVXP SURLQ DOLTXDP OXFWXV PDXULV'
    assert coder.decode(
        test_str) == 'LOREM IPSUM DOLOR SIT AMET CONSECTETUR ADIPISCING ELIT MAURIS AUGUE NISI SOLLICITUDIN ID SAGITTIS SED TRISTIQUE VEL IPSUM PROIN ALIQUAM LUCTUS MAURIS'


def test_decode_invalid_char():
    test_str = 'ab_34_$%'
    assert coder.decode(test_str) == 'ab_34_$%'


#   ---

def test_negative_stride():
    coder = CaesarCoder(-3)
    test_str = 'XYZABC'
    assert coder.encode(test_str) == 'UVWXYZ'


def test_empty_str_in():
    with pytest.raises(AssertionError):
        test_str = ''
        coder.encode(test_str)
