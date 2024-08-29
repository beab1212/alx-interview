#!/usr/bin/python3
"""N queens puzzle challenge
"""
import sys

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)

try:
    n_queen = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    exit(1)

if n_queen < 4:
    print('N must be at least 4')
    exit(1)


def sol_nqueens(n):
    """ self explanatory recursion """
    if n == 0:
        return [[]]
    inner_solution = sol_nqueens(n - 1)
    return [solution + [(n, i + 1)]
            for i in range(n_queen)
            for solution in inner_solution
            if safe_queen((n, i + 1), solution)]


def att_queen(square, queen):
    """
    self explanatory
    """
    (row1, col1) = square
    (row2, col2) = queen
    return (row1 == row2) or (col1 == col2) or\
        abs(row1 - row2) == abs(col1 - col2)


def safe_queen(sqr, queens):
    """
    self explanatory
    """
    for queen in queens:
        if att_queen(sqr, queen):
            return False
    return True


for answer in reversed(sol_nqueens(n_queen)):
    result = []
    for p in [list(p) for p in answer]:
        result.append([i - 1 for i in p])
    print(result)
