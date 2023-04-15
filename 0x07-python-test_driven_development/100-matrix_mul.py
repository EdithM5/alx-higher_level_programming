#!/usr/bin/python3

""" this is a function that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """
    only matrices
    Validate inputs
    checks if they can be multiplied
    raise ValueError if they can't
    all rows should be of the same size
    """
    for matrix in (m_a, m_b):
        if not isinstance(matrix, list):
            raise TypeError(f"{matrix} must be a list")
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError(f"{matrix} must be a list of lists")
        if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
            raise ValueError(f"{matrix} can't be empty")
        if any(not isinstance(element, (int, float)) for row in matrix for element in row):
            raise TypeError(f"{matrix} should contain only integers or floats")
        if any(len(row) != len(matrix[0]) for row in matrix):
            raise TypeError(f"each row of {matrix} must be of the same size")
    # Check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError(f"{m_a} and {m_b} can't be multiplied")
    # Multiply matrices
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row.append(element)
        result.append(row)

    return (result)
