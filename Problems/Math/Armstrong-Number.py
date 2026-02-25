"""
Problem: Armstrong Number
Reference: https://codeanddebug.in/blog/python-program-to-check-armstrong-number/
"""

def is_armstrong(n):
    num = n
    power = len(str(n))
    total = 0

    while num > 0:
        digit = num % 10
        total += digit ** power
        num //= 10

    return total == n
