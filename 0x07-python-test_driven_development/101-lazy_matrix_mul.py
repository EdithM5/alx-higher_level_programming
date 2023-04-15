#!/usr/bin/python3


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    >>> lazy_matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    array([[19, 22],
           [43, 50]])

    >>> lazy_matrix_mul([[1, 2], [3, 4]], [[1], [2]])
    array([[ 5],
           [11]])

    >>> lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2, 3], [4, 5, 6]])
    Traceback (most recent call last):
        ...
    ValueError: shapes (2,2) and (2,3) not aligned: 2 (dim 1) != 2 (dim 0)

    >>> lazy_matrix_mul([[1, 2], [3, 4], [5, 6]], [[1], [2]])
    Traceback (most recent call last):
        ...
    ValueError: shapes (3,2) and (2,1) not aligned: 2 (dim 1) != 2 (dim 0)

    >>> lazy_matrix_mul([[1, 2], [3, 'four']], [[5, 6], [7, 8]])
    Traceback (most recent call last):
        ...
    ValueError: could not convert string to float: 'four'

    >>> lazy_matrix_mul([], [[]])
    Traceback (most recent call last):
        ...
    ValueError: operands could not be broadcast together with shapes (0,2) (1,0)

    >>> lazy_matrix_mul([[1, 2], [3, 4]], {})
    Traceback (most recent call last):
        ...
    AttributeError: 'dict' object has no attribute 'shape'

    >>> lazy_matrix_mul(42, [[1, 2], [3, 4]])
    Traceback (most recent call last):
        ...
    AttributeError: 'int' object has no attribute 'shape'
    """
    try:
        m_a = np.array(m_a, dtype=float)
    except ValueError:
        raise TypeError("each element of m_a should be an integer or a float")
        m_b = np.array(m_b, dtype=float)
    except ValueError:
        raise TypeError("each element of m_b should be an integer or a float")

    try:
        result = np.matmul(m_a, m_b)
    except ValueError as e:
        raise ValueError(str(e))

    return (result.tolist())
