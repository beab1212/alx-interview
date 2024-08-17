#!/usr/bin/env python3
"""
Main file
"""

def rotate_2d_matrix(matrix):
    """
    Rotate it 90 degrees clockwise
    """
    duplicate = matrix[:]

    for i in range(len(matrix)):
        column = [row[i] for row in duplicate]
        matrix[i] = column[::-1]
