# helper functions

def is_hexadecimal(value: str) -> bool:
    """Check if string is a hexadecimal encoding of a integer numerical value.

    :param value: string value about to be validated
    :return: True if value represents a hexadecimal number, False if not
    :rtype: bool
    """

    for c in value:
        if ((c < '0' or c > '9') and
                (c < 'a' or c > 'f')):
            return False
    return True
