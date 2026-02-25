"""
Problem: Check Palindrome String Using Recursion
"""

def is_palindrome(word, l, r):
    if l >= r:
        return True
    
    if word[l] != word[r]:
        return False
    
    return is_palindrome(word, l + 1, r - 1)

print(is_palindrome("nitin", 0, len("nitin") - 1))
