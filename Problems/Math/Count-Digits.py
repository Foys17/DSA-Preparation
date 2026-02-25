"""
Problem: Count Digits
Reference: https://codeanddebug.in/blog/python-program-to-count-number-of-digits/
"""

def countDigits(n):
    cnt = 0
    while n > 0:
        cnt += 1
        n //= 10
    return cnt
