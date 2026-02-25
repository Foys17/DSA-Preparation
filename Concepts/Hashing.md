# Hashing & Dictionary in Python

## ✅ What is Hashing?

Hashing is a technique that allows very fast data lookup.

Python dictionaries use hashing internally.

Average operation time:

Insert → O(1)
Search → O(1)
Delete → O(1)

---

## ✅ Why Dictionary is Powerful

Dictionary allows:

- Fast search
- Frequency counting
- Mapping values

Example:

freq = {}

freq[x] = freq.get(x, 0) + 1

---

## ✅ Common Pattern – Frequency Count

Used in MANY problems.

Example:

nums = [1,1,2,2,2,3]

freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1
