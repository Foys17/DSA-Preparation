# Digit Based Problems (Very Common in DSA)

Many beginner problems involve extracting and manipulating digits.

Core idea always uses:

last_digit = n % 10
n = n // 10

---

## ✅ Extraction of Digits

Goal → Process digits one by one.

Logic:

- % 10 → last digit বের করে
- // 10 → last digit remove করে

Example:

4356 → 6 → 5 → 3 → 4

Reference:
https://codeanddebug.in/blog/extraction-of-digits-in-python/

---

## ✅ Counting Digits

Goal → Number-এ কয়টা digit আছে।

Logic:

Repeatedly divide by 10 until number becomes 0.

Time Complexity → O(digits)

Reference:
https://codeanddebug.in/blog/python-program-to-count-number-of-digits/

---

## ✅ Reversing a Number

Used in MANY problems (palindrome, etc).

Logic:

rev = rev * 10 + last_digit

---

## ✅ Palindrome Number

Definition → Same forward & backward.

Approach:

1️⃣ Reverse number  
2️⃣ Compare with original

Important edge case:

Negative numbers → NOT palindrome

Reference:
https://codeanddebug.in/blog/palindrome-number-program-in-python/

---

## ✅ Armstrong Number

Definition:

Sum of digits raised to power of number of digits = original number

Example:

153 → 1³ + 5³ + 3³ = 153

Steps:

1️⃣ Count digits  
2️⃣ Extract digits  
3️⃣ Compute power sum

Reference:
https://codeanddebug.in/blog/python-program-to-check-armstrong-number/

---

## ✅ Divisors / Factors of Integer

Goal → Find numbers that divide n.

Optimized idea:

Check only till √n

Why?

Divisors always come in pairs.

Example:

36 → (1,36), (2,18), (3,12), (4,9), (6,6)

Reference:
https://codeanddebug.in/blog/python-program-print-divisors-factors-integer/
