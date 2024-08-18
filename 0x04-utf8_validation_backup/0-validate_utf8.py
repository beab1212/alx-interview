#!/usr/bin/python3
""" validUTF8 """


def validUTF8(data):
    """validUTF8
        Args:
            data (list):
        Returns:
            True if data is valid UTF-8 encoding else False
    """
    status = 0

    for item in data:
        binary = bin(item).replace('0b', '').rjust(8, '0')[-8:]
        if status == 0:
            if binary.startswith('110'):
                status = 1
            if binary.startswith('1110'):
                status = 2
            if binary.startswith('11110'):
                status = 3
            if binary.startswith('10'):
                return False
        else:
            if not binary.startswith('10'):
                return False
            status -= 1

    if status != 0:
        return False

    return True
