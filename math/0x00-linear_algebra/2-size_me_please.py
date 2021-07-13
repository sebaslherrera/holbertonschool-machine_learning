#!/usr/bin/env python3

"""Module shape of a matrix """


def matrix_shape(matrix):
    """ Return the shape of a matrix
    returns a tuple with each index having the
    number of corresponding elements """

    ans = []
    while (isinstance(matrix, list)):
        ans.append(len(matrix))
        matrix = matrix[0]
    return ans
