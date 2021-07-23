#!/usr/bin/env python3

def poly_integral(poly, C=0):
    if not isinstance(poly, list) or not isinstance(C, int):
        return None

    ans = [C]
    for i in range(len(poly)):
        temp = poly[i] / (i + 1)
        if temp.is_integer():
            temp = int(temp)
        ans.append(temp)
    if ans[-1] == 0:
        ans.pop()
    return ans
