import pytest
from Caesar import CaesarCoder

coder = CaesarCoder()

#   ENCODER

def test_encode_lowercase():
    test_str = 'abcdxyz'
    assert coder.encode(test_str) == 'defgabc'

def test_encode_uppercase():
    test_str = 'ABCDXYZ'
    assert coder.encode(test_str) == 'DEFGABC'

def test_encode_lower_and_upper():
    test_str = 'aBcDxYz'
    assert coder.encode(test_str) == 'dEfGaBc'

def test_encode_long():
    #   https://www.lipsum.com
    test_str = 'Lorem ipsum dolor sit amet consectetur adipiscing elit Mauris augue nisi sollicitudin id sagittis sed tristique vel ipsum Proin aliquam luctus mauris'
    assert coder.encode(test_str) == 'Oruhp lsvxp groru vlw dphw frqvhfwhwxu dglslvflqj holw Pdxulv dxjxh qlvl vroolflwxglq lg vdjlwwlv vhg wulvwltxh yho lsvxp Surlq doltxdp oxfwxv pdxulv'

def test_encode_invalid_char():
    test_str = 'aB_d'
    #   coder returns an empty string if it encounters an invalid char
    assert coder.encode(test_str) == ''

#   DECODER

def test_decode_lowercase():
    test_str = 'defgabc'
    assert coder.decode(test_str) == 'abcdxyz'

def test_decode_uppercase():
    test_str = 'DEFGABC'
    assert coder.decode(test_str) == 'ABCDXYZ'

def test_decode_lower_and_upper():
    test_str = 'dEfGaBc'
    assert coder.decode(test_str) == 'aBcDxYz'

def test_decode_long():
    #   https://www.lipsum.com
    test_str = 'Oruhp lsvxp groru vlw dphw frqvhfwhwxu dglslvflqj holw Pdxulv dxjxh qlvl vroolflwxglq lg vdjlwwlv vhg wulvwltxh yho lsvxp Surlq doltxdp oxfwxv pdxulv'
    assert coder.decode(test_str) == 'Lorem ipsum dolor sit amet consectetur adipiscing elit Mauris augue nisi sollicitudin id sagittis sed tristique vel ipsum Proin aliquam luctus mauris'

def test_decode_invalid_char():
    test_str = 'aB_d'
    #   coder returns an empty string if it encounters an invalid char
    assert coder.decode(test_str) == ''