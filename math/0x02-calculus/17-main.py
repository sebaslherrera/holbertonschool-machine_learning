#!/usr/bin/env python3

poly_integral = __import__('17-integrate').poly_integral

poly = [5, 3, 0, 1]
print(poly_integral(poly))

poly = [5, 3, 0, 0]
print(poly_integral(poly))

# poly = ['hello']
# print(poly_integral(poly))

poly = [5, 3, 0, 1]
print(poly_integral(poly, 2))

poly = [5, 3, 0, 1]
print(poly_integral(poly, 2.3))

poly = [0]
print(poly_integral(poly, 4))


poly = []
print(poly_integral(poly, 4))
