# Recursion Patterns (High Value for Interviews)

Recursion problems often follow repeated patterns.

---

## ✅ Print / Traversal Pattern

Used when printing sequences.

Example:

Print 1 → N

Logic:

- Call recursion first
- Print while returning (backtracking)

Reference:
https://codeanddebug.in/blog/python-program-print-1-to-n-without-loops/

---

## ✅ Functional Recursion

Definition:

Function RETURNS value from recursive call.

Example:

sum(n) = n + sum(n-1)

Used in:

✔ Sum problems  
✔ Fibonacci  
✔ Factorial  

---

## ✅ Factorial Pattern

Definition:

n! = n × (n-1)!

Stopping condition:

n == 1

Reference:
https://codeanddebug.in/blog/find-factorial-of-number-using-recursion/

---

## ✅ Fibonacci Pattern

Definition:

fib(n) = fib(n-1) + fib(n-2)

Base cases:

fib(0) = 0  
fib(1) = 1

Reference:
https://codeanddebug.in/blog/fibonacci-number/

---

## ✅ Two Pointer Recursion

Used for:

✔ Reverse array  
✔ Palindrome string  

Idea:

- Compare / Swap outer elements
- Move inward

Reference:
https://codeanddebug.in/blog/reverse-array-using-recursion-and-while-loop/

Reference:
https://codeanddebug.in/blog/palindrome-string-recursive-iterative-solution/

---

## ✅ Golden Rule of Recursion

Every recursion MUST have:

1️⃣ Base Case (Stop condition)  
2️⃣ Recursive Case (Smaller problem)

Without base case → Infinite recursion → Crash
