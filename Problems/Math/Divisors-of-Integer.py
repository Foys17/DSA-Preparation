"""
Problem: Print Divisors of Integer
Reference: https://codeanddebug.in/blog/python-program-print-divisors-factors-integer/
"""

from math import sqrt

def divisors(n):
    result = []

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            result.append(i)

            if n // i != i:
                result.append(n // i)

    result.sort()
    return result
