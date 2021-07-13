#!/usr/bin/env python3

""" Module matrix transponse """


def matrix_transpose(matrix):
    """ Return the transponse of a matrix
    Switch rows by cols and cols by rows"""

    lenRows = len(matrix)
    lenCols = len(matrix[0])

    ans = [[0] * lenRows for i in range(lenCols)]

    for i in range(lenCols):
        for j in range(lenRows):
            ans[i][j] = matrix[j][i]

    return ans
