#!/usr/bin/env python3

"""Module across the planes"""


def add_matrices2D(mat1, mat2):
    """Adds two matrices element-wise"""

    rowLen1 = len(mat1)
    colLen1 = len(mat1[0])

    rowLen2 = len(mat2)
    colLen2 = len(mat2[0])

    if (rowLen1 != rowLen2) or (colLen1 != colLen2):
        return None

    ans = [[0] * colLen1 for i in range(rowLen1)]

    for i in range(rowLen1):
        for j in range(rowLen2):
            ans[i][j] = mat1[i][j] + mat2[i][j]

    return ans
