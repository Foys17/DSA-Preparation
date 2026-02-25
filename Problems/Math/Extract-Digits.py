"""
Problem: Extract Digits from Number
Reference: https://codeanddebug.in/blog/extraction-of-digits-in-python/

Idea:
- Use % 10 to get last digit
- Use // 10 to remove digit

Time Complexity: O(digits)
Space Complexity: O(1)
"""

def extractDigits(num: int) -> None:
    n = num
    while n > 0:
        last_digit = n % 10
        print(last_digit, end="")
        n = n // 10
