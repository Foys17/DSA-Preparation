"""
Problem: Print numbers from 1 to N using Recursion

Idea:
- First go till base case
- Then print while returning (backtracking)

Flow:
func(5)
→ func(4)
→ func(3)
→ func(2)
→ func(1)
→ STOP → Print starts
"""

def print_1_to_n(n):
    if n == 0:
        return
    
    print_1_to_n(n - 1)
    print(n)

print_1_to_n(5)
