import hashlib as hl
import logging

logger = logging.getLogger('hashing')
FORMAT = "%(funcName)20s(): %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.DEBUG)

#print(hl.algorithms_available)
#print(hl.algorithms_guaranteed)


def hash_with_md5(str_in: str):
    out = hl.md5()
    out.update(str_in.encode())
    logger.info(out.hexdigest())


def hash_with_blake2s(str_in: str):
    out = hl.blake2s()
    out.update(str_in.encode())
    logger.info(out.hexdigest())


def hash_with_blake2b(str_in: str):
    out = hl.blake2b()
    out.update(str_in.encode())
    logger.info(out.hexdigest())


def hash_with_sha1(str_in: str):
    out = hl.sha1()
    out.update(str_in.encode())
    logger.info(out.hexdigest())


def hash_with_shake_128(str_in: str):
    out = hl.shake_128()
    out.update(str_in.encode())
    logger.info(out.hexdigest(16))


def hash_with_shake_256(str_in: str):
    out = hl.shake_256()
    out.update(str_in.encode())
    logger.info(out.hexdigest(16))


def hash_with_sha384(str_in: str):
    out = hl.sha384()
    out.update(str_in.encode())
    logger.info(out.hexdigest())


def hash_with_sha512(str_in: str):
    out = hl.sha512()
    out.update(str_in.encode())
    logger.info(out.hexdigest())


def hash_with_sha3_224(str_in: str):
    out = hl.sha3_224()
    out.update(str_in.encode())
    logger.info(out.hexdigest())


def hash_with_sha3_256(str_in: str):
    out = hl.sha3_256()
    out.update(str_in.encode())
    logger.info(out.hexdigest())


def hash_with_sha3_512(str_in: str):
    out = hl.sha3_512()
    out.update(str_in.encode())
    logger.info(out.hexdigest())

# algorithms_available, but cannot be implemented

# def hash_with_sha512_224(str_in: str):
#     out = hl.sha512_224()
#     out.update(str_in.encode())
#     logger.info(out.hexdigest())
#
#
# def hash_with_md5_sha1(str_in: str):
#     out = hl.md5_sha1()
#     out.update(str_in.encode())
#     logger.info(out.hexdigest())
#
#
# def hash_with_mdc2(str_in: str):
#     out = hl.mdc2()
#     out.update(str_in.encode())
#     logger.info(out.hexdigest())
#
# def hash_with_ripmd160(str_in: str):
#     out = hl.ripmd160()
#     out.update(str_in.encode())
#     logger.info(out.hexdigest())
#
#
# def hash_with_sha512_256(str_in: str):
#     out = hl.sha512_256()
#     out.update(str_in.encode())
#     logger.info(out.hexdigest())
#
# def hash_with_whirlpool(str_in: str):
#     out = hl.whirlpool()
#     out.update(str_in.encode())
#     logger.info(out.hexdigest())
#
# def hash_with_sm3(str_in: str):
#     out = hl.sm3()
#     out.update(str_in.encode())
#     logger.info(out.hexdigest())
#
#
# def hash_with_md4(str_in: str):
#     out = hl.md4()
#     out.update(str_in.encode())
#     logger.info(out.hexdigest())

def hash_with_all(str_in: str):
    hash_with_md5(str_in)
    hash_with_blake2s(str_in)
    hash_with_blake2b(str_in)
    hash_with_sha1(str_in)
    hash_with_shake_128(str_in)
    hash_with_shake_256(str_in)
    hash_with_sha384(str_in)
    hash_with_sha3_224(str_in)
    hash_with_sha3_256(str_in)
    hash_with_sha3_512(str_in)

#hash_with_shake_128('testtext12345')
#hash_with_all('secondtext54321abc')