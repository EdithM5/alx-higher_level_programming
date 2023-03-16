#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    # Define the function to square a value
    def square(x):
        return x**2

    # Use map to apply the square function to each value in the matrix
    result = list(map(lambda row: list(map(square, row)), matrix))
    return result
