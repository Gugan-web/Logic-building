# Day 03 — Loops, Conditions & Basic Math

## 🎯 Goals
- Master Python loop patterns (range, enumerate, zip, while)
- Learn math tricks essential for competitive programming
- Understand time complexity: when is O(n²) too slow?

---

## ⏱️ Complexity Reference

| Complexity | Max n for 1s | Example |
|------------|-------------|---------|
| O(1) | Any | Formula |
| O(log n) | 10^18 | Binary search |
| O(√n) | 10^12 | Prime check |
| O(n) | 10^8 | Single loop |
| O(n log n) | 10^6 | Sorting |
| O(n²) | 10^4 | Nested loops |
| O(2^n) | 20–25 | Backtracking |

---

## 🔁 Loop Patterns

```python
# Basic
for i in range(n):          ...   # 0 to n-1
for i in range(1, n+1):     ...   # 1 to n
for i in range(n-1, -1, -1):...  # n-1 down to 0
for i in range(0, n, 2):    ...   # even indices only

# Enumerate (index + value)
for i, val in enumerate(a):  ...

# Zip (parallel lists)
for x, y in zip(a, b):       ...

# While
while n > 0:
    n //= 2
```

---

## 🧮 Math Tricks

### Ceiling division (no float needed)
```python
ceil_div = (a + b - 1) // b
# or simply:
import math; math.ceil(a / b)   # works but float-based
```

### Check even/odd
```python
n % 2 == 0   # even
n & 1        # odd (bitwise, slightly faster)
```

### Sum of digits
```python
sum(int(c) for c in str(n))   # pythonic
```

### Trailing zeros of n!
```python
def trailing_zeros(n):
    count = 0
    while n >= 5:
        n //= 5; count += n
    return count
```

### Perfect square (no float error!)
```python
from math import isqrt
def is_perfect_square(n):
    r = isqrt(n)
    return r * r == n
```

---

## 📝 Exercises

### Exercise 1 — FizzBuzz
Print 1 to n: multiples of 3 → "Fizz", 5 → "Buzz", both → "FizzBuzz".

### Exercise 2 — Trailing Zeros
Count trailing zeros in n! for n up to 10^9.
```
Input: 25    Output: 6
```

### Exercise 3 — Digit Sum of n²
```
Input: 9     Output: 9   (81 → 8+1=9)
```

### Exercise 4 — Collatz Sequence
Count steps for Collatz sequence: if n is even → n/2, else → 3n+1. Stop at 1.
```
Input: 6     Output: 8
```

### Exercise 5 — Count Divisible
Count integers from 1 to n divisible by 2, 3, or 5. Use inclusion-exclusion.
```
Input: 10    Output: 8
```

---

## 🔗 Codeforces Practice
1. [A. Pashmak and Garden](https://codeforces.com/problemset/problem/459/A)
2. [A. Tricky Sum](https://codeforces.com/problemset/problem/571/A)
3. [A. Next Round](https://codeforces.com/problemset/problem/458/A)
4. [B. Petya and Strings](https://codeforces.com/problemset/problem/96/A)
