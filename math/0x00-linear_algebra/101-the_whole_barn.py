#!/usr/bin/env python3

"""The Whole Barn module"""


def check_shapes(mat1, mat2):
    """Check if the two matrices has the same shape
    if not return None"""
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
    """Recursion method to sum the matrices"""
    # Base case
    if not isinstance(mat1, list) and not isinstance(mat2, list):
        return mat1 + mat2

    ans = []
    for m in zip(mat1, mat2):
        ans.append(helper(m[0], m[1]))
    return ans


def add_matrices(mat1, mat2):
    """Main function"""
    if check_shapes(mat1, mat2) is None:
        return None
    return helper(mat1, mat2)
