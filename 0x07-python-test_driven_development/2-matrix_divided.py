#!/usr/bin/python3

"""
Defines a matrix division function
"""


def matrix_divided(matrix, div):
    """ Divide all elements of a matrix.
    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If matrix is not a list of ints and floats
        TypeError: If each row of the matrix is not the same size
        TypeError: If div is not an integer or float
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """

    if (not isinstance(matrix, list) or matrix == []):
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    if (not isinstance(div, (int, float))):
        raise TypeError("div must be a number")

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists)" +
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if (not isinstance(x, (int, float))):
                raise TypeError("matrix must be a matrix (list of lists)" +
                                "of integers/floats")
    return [[round(x / div, 2) for x in row] for row in matrix]
