#!/usr/bin/env python3
"""
Main file
"""

def rotate_2d_matrix(matrix):
    """
    Rotate matrix it 90 degrees
    """
    duplicate = matrix[:]

    for i in range(len(matrix)):
        column = [row[i] for row in duplicate]
        matrix[i] = column[::-1]
