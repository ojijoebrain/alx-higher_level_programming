#!/usr/bin/python3

def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Raises:
        TypeError: When the matrix contains non-numbers.
        TypeError: When the matrix contains rows of different sizes.
        TypeError: When div is not an int or float.
        ZeroDivisionError: When div is 0.
    Returns:
        A new matrix result of the division.
    """
    if (
        not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(ele, (int, float)) for row in matrix for ele in row)
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
