#!/usr/bin/python3
"""
a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):

    """
    matrix is a list of integers/ floats
    each row must be the same size
    div must be an int/float and not zero
    return new matrix round to 2 decimal places
    """
    # Check if matrix is a matrix of integers or floats
    if not all(isinstance(row, list) and all(isinstance(val, (int, float))for val in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    # Check if each row of the matrix has the same size
    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div and round to 2 decimal places
    new_matrix = [[round(val / div, 2) for val in row] for row in matrix]

    return (new_matrix)
