#!/usr/bin/env python3

def check_shapes(mat1, mat2):
    shape = []
    while (isinstance(mat1, list) and isinstance(mat2, list)):
        lenMat1 = len(mat1)
        lenMat2 = len(mat2)
        if lenMat1 != lenMat2:
            return None
        shape.append(lenMat1)
        mat1 = mat1[0]
        mat2 = mat2[0]

    return shape


def helper(mat1, mat2):
    # Base case
    if not isinstance(mat1, list) and not isinstance(mat2, list):
        return mat1 + mat2

    ans = []
    for m in zip(mat1, mat2):
        ans.append(helper(m[0], m[1]))
    return ans


def add_matrices(mat1, mat2):
    if check_shapes(mat1, mat2) is None:
        return None
    return helper(mat1, mat2)
