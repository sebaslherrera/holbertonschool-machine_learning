#!/usr/bin/env python3

"""Module Line up"""


def add_arrays(arr1, arr2):
    """Adds two arrays element-wise"""

    lenArr1 = len(arr1)
    lenArr2 = len(arr2)

    if lenArr1 != lenArr2:
        return None

    ans = []

    for i in range(lenArr1):
        ans.append(arr1[i] + arr2[i])

    return ans
