#!/usr/bin/python3
"""
a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    matrix is a list of integers/ floats
    each row must be the same size
    div must be an int/float and not zero
    return new matrix round to 2 decimap places
    """

    try:
        row_lengths = set()
        for row in matrix:
            if not isinstance(row, list):
                raise TypeError("matrix must be a matrix (list of lists)"
                                "of integers/floats")
            if not all(isinstance(val, (int, float)) for val in row):
                raise TypeError("matrix must be a matrix (list of lists)"
                                "of integers/floats")
            row_lengths.add(len(row))
        if len(row_lengths) > 1:
            raise TypeError("Each row of the matrix must have the same size")
    except TypeError:
        raise

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div and round to 2 decimal places
    new_matrix = []
    for row in matrix:
        new_row = []
        for val in row:
            new_val = round(val / div, 2)
            new_row.append(new_val)
        new_matrix.append(new_row)

    return (new_matrix)
