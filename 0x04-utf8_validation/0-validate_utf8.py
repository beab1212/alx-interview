#!/usr/bin/python3
"""
0x04. UTF-8 Validation
Reference:
    https://en.wikipedia.org/wiki/UTF-8#Encoding
"""


def validUTF8(data):
    """
        Args:
            data (list)
        Returns:
            True if data is valid UTF-8 encoding else False

        # byte_size used to track byte size
    """

    byte_size = 1
    for number in data:
        binary = bin(number).replace('0b', '').rjust(8, '0')[-8:]
        if byte_size == 1:
            if binary.startswith('110'):
                byte_size = 2
            elif binary.startswith('1110'):
                byte_size = 3
            elif binary.startswith('11110'):
                byte_size = 4
            elif binary.startswith('10'):
                return False
        else:
            if not binary.startswith('10'):
                return False
            byte_size -= 1

    if byte_size != 1:
        return False
    else:
        return True
