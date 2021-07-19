#!/usr/bin/env python3

"""Squashed Like Sardines module"""


def check_shape(mat):
    """Check if the two matrices has the same shape
    if not return None"""
    shape = []
    while isinstance(mat, list):
        shape.append(len(mat))
        mat = mat[0]
    # print("shapes are {}".format(shape))
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


def cat_matrices(mat1, mat2, axis=0):
    """Main function"""
    shapes = (check_shape(mat1), check_shape(mat2))

    return []
