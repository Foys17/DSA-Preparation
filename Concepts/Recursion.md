# Recursion

## ✅ What is Recursion?

Recursion means a function calling itself.

Used when problems can be broken into smaller subproblems.

---

## ✅ Two Critical Parts

Every recursion MUST have:

1️⃣ Base Case → Stopping condition  
2️⃣ Recursive Case → Smaller problem call

Example:

def func(n):
    if n == 1:
        return 1
    
    return n + func(n-1)

---

## ✅ Base Case

Prevents infinite recursion.

Without base case → program crashes.

---

## ✅ Functional Recursion

Function returns value from recursive call.

Example:

return n + func(n-1)

---

## ✅ Parameter Recursion

Uses parameters to control flow.

Example:

func(i, n)

---

## ✅ Common Mistakes

❌ Forgetting base case  
❌ Forgetting return  
❌ Wrong recursive call
