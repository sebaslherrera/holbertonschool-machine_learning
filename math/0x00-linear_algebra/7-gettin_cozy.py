#!/usr/bin/env python3

"""Getting cozy module"""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenates two matrices along a specific axis"""

    ans = []

    if axis == 0 and len(mat1[0]) == len(mat2[0]):
        return mat1 + mat2
    elif axis == 1 and len(mat1) == len(mat2):
        for i in range(len(mat1)):
            ans.append(mat1[i] + mat2[i])
        return ans

    return None
