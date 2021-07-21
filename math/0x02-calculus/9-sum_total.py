#!/usr/bin/env python3

"""Our life is the sum total of all the decisions we
 make every day, and those decisions are determined by our priorities"""


def summation_i_squared(n):

    if not isinstance(n, int) or n < 1:
        return None
    return int(((n*(n+1)*(2*n+1))/6))
