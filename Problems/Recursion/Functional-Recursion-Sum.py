"""
Concept: Functional Recursion

Definition:
Function returns value from recursive call.

Example:
sum(n) = n + sum(n-1)
"""

def func(n):
    if n == 1:
        return 1
    
    return n + func(n - 1)

print(func(4))
