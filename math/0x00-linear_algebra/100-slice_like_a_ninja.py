#!/usr/bin/env python3

"""Slice Like A Ninja"""


def np_slice(matrix, axes={}):
    """Slices a matrix along specific axes"""

    ans = [slice(None)] * len(matrix.shape)

    for key, value in axes.items():
        ans[key] = slice(*value)

    return matrix[tuple(ans)]
