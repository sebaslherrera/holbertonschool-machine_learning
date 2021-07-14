#!/usr/bin/env python3

"""Ridin’ Bareback module"""


def mat_mul(mat1, mat2):
    """Matrix multiplication"""

    rowLen1 = len(mat1)
    colLen1 = len(mat1[0])
    rowLen2 = len(mat2)
    colLen2 = len(mat2[0])

    if colLen1 != rowLen2:
        return None

    ans = [[0] * colLen2 for i in range(rowLen1)]

    for i in range(rowLen1):
        for j in range(colLen2):
            ans[i][j] = 0
            for k in range(colLen1):
                ans[i][j] += mat1[i][k] * mat2[k][j]

    return ans
