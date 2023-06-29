#!/usr/bin/python3
"""
Pascal triangle
"""


def pascal_triangle(n):
    """
    This function returns a list of lists of integers representing
    the pascal's triangle of n
    """
    result = []

    if n <= 0:
        return result
    else:
        for i in range(n):
            row = str(11 ** i)
            array_row = []
            for i in row:
                array_row.append(int(i))
            result.append(array_row)
        return result
