#!/usr/bin/env python3

"""Derive happiness in oneself from a good day's work"""


def poly_derivative(poly):
    """Derivative from list"""

    if not isinstance(poly, list) or len(poly) < 1:
        return None

    lenPoly = len(poly)
    ans = []

    if lenPoly == 1:
        return [0]

    for i in range(1, lenPoly):
        ans.append(poly[i] * i)
    return ans
