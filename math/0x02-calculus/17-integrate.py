#!/usr/bin/env python3

"""17 Integrate Module """


def poly_integral(poly, C=0):
    """Return an list of the integrated polynomial"""
    if (not isinstance(poly, list) or
        len(poly) == 0 or
        not all(isinstance(x, (int, float)) for x in poly) or
            not isinstance(C, (int, float))):
        return None

    ans = [C]
    for i in range(len(poly)):
        temp = poly[i] / (i + 1)
        if temp.is_integer():
            temp = round(temp)
        ans.append(temp)
    if ans[-1] == 0:
        ans.pop()
    return ans
