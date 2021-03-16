import pytest
from task_01_caesar_vigenere.src.Caesar import CaesarCoder as cc


#   ENCODE

def test_encode():
    test_str = 'ABCDXYZ'
    assert cc.encode(test_str, 3) == 'DEFGABC'


def test_encode_long():
    #   https://www.lipsum.com
    test_str = 'LOREM IPSUM DOLOR SIT AMET CONSECTETUR ADIPISCING ELIT MAURIS AUGUE NISI SOLLICITUDIN ID SAGITTIS SED ' \
               'TRISTIQUE VEL IPSUM PROIN ALIQUAM LUCTUS MAURIS '
    assert cc.encode(
        test_str,
        3) == 'ORUHP LSVXP GRORU VLW DPHW FRQVHFWHWXU DGLSLVFLQJ HOLW PDXULV DXJXH QLVL VROOLFLWXGLQ LG VDJLWWLV VHG ' \
              'WULVWLTXH YHO LSVXP SURLQ DOLTXDP OXFWXV PDXULV '


def test_encode_invalid_char():
    test_str = 'ab_34_$%'
    assert cc.encode(test_str, 3) == 'ab_34_$%'


#   DECODE

def test_decode():
    test_str = 'DEFGABC'
    assert cc.decode(test_str, 3) == 'ABCDXYZ'


def test_decode_long():
    #   https://www.lipsum.com
    test_str = 'ORUHP LSVXP GRORU VLW DPHW FRQVHFWHWXU DGLSLVFLQJ HOLW PDXULV DXJXH QLVL VROOLFLWXGLQ LG VDJLWWLV VHG ' \
               'WULVWLTXH YHO LSVXP SURLQ DOLTXDP OXFWXV PDXULV '
    assert cc.decode(
        test_str,
        3) == 'LOREM IPSUM DOLOR SIT AMET CONSECTETUR ADIPISCING ELIT MAURIS AUGUE NISI SOLLICITUDIN ID SAGITTIS SED ' \
              'TRISTIQUE VEL IPSUM PROIN ALIQUAM LUCTUS MAURIS '


def test_decode_invalid_char():
    test_str = 'ab_34_$%'
    assert cc.decode(test_str, 3) == 'ab_34_$%'


#   ---

def test_negative_stride():
    test_str = 'XYZABC'
    assert cc.encode(test_str, -3) == 'UVWXYZ'


def test_empty_str_in():
    with pytest.raises(AssertionError):
        test_str = ''
        cc.encode(test_str, 3)
