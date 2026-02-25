"""
Problem: Reverse Array Using Recursion

Idea:
- Swap outer elements
- Move inward
"""

def reverse(arr, left, right):
    if left >= right:
        return
    
    arr[left], arr[right] = arr[right], arr[left]
    reverse(arr, left + 1, right - 1)

arr = [1, 2, 3, 4, 5]

reverse(arr, 0, len(arr) - 1)

print(arr)
