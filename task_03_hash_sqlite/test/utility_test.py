from task_03_hash_sqlite.src.utility import Hashing as h


def test_hash_success():
    assert h.hash('password123',
                     b'\xa1\xe2\x06p\x1d\xf29\xdf') == '6cba4b66a94081531eaf0507e219551a062c6d59f74201308c44e36a8cb1f56b'


def test_hash_empty():
    assert h.hash('',
                     b'\xf6S\xf4\rq\xb5\x90\x95') == 'ef5697f3c511aa6bbf9e04cc10f134d7d55cd98313bc8b4e22363c8a1b07afc3'


def test_passwords_are_the_same():
    assert h.check_if_hashed_passwords_match(
        'password_02',
        ['user_02', 'd04d29b91fbb4f37aaca9c995654823a3abc33cd8bd500d56f56de681d9f1b10', b'm\x93\t\xbe\xff\xb2p\xab']
    )
