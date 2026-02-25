"""
Problem: Store Frequency in Dictionary
Pattern: Very Important for Interviews
"""

nums = [1,1,1,2,2,2,2,3,3,4,4,4,4,4,5,5,5]

freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1

print(freq)
