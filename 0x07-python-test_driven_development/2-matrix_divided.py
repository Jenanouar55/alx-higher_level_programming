#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.
The 2-matrix_divided module supplies one function, matrix_divided(matrix, div).
"""
def matrix_divided(matrix, div):
    """
    Divide all elements in the matrix by div and return the result as a new matrix.

    Args:
        matrix (list of list of int/float): The input matrix to be divided.
        div (int or float): The divisor used for division.

    Returns:
        list of list of float: A new matrix where each element is the result of matrix element divided by div.
    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                or if div is not a number (integer or float).
        TypeError: If each row of the matrix does not have the same size,
                or if any element in the matrix is not an integer or float.
        ZeroDivisionError: If div is zero.
    """
    # Validate matrix input
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")


    size = None
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        # Check row size consistency
        if size is None:
            size = len(row)
        elif len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")

        # Check element types in the row
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        # Validate divisor
        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")

        if div == 0:
            raise ZeroDivisionError("division by zero")

        # Perform matrix division and rounding
        return [[round(i / div, 2) for i in l] for l in matrix]
