# Day 02 — Data Types, Overflow & Modular Arithmetic

## 🎯 Goals
- Understand Python's arbitrary precision integers (no overflow!)
- Master modular arithmetic patterns
- Use `pow(base, exp, mod)` efficiently

---

## 🐍 Python Integer: No Overflow!

Unlike C++, **Python integers have no fixed size** — they grow as large as needed.

```python
x = 10 ** 100   # googol — works perfectly in Python!
print(x)        # 10000000...0 (100 zeros)
```

This means:
- No risk of overflow
- But large numbers are **slower** to compute
- Still need modular arithmetic when the problem says "print answer mod 10^9+7"

---

## 📊 Numeric Types in Python

| Type | Description | Example |
|------|-------------|---------|
| `int` | Arbitrary precision integer | `123456789012345678901234567890` |
| `float` | 64-bit floating point (~15 digits precision) | `3.14159` |
| `complex` | Complex number | `3 + 4j` |
| `Decimal` | High-precision decimal (import) | `Decimal('1.0') / Decimal('3.0')` |

### Float Pitfalls
```python
# Never compare floats with ==
0.1 + 0.2 == 0.3   # False!  (floating point error)
abs((0.1 + 0.2) - 0.3) < 1e-9   # Correct comparison
```

---

## 🔢 Modular Arithmetic

When the problem says **"output the answer modulo 10^9+7"**:

```python
MOD = 10**9 + 7
```

### Basic Rules
```python
# Addition
result = (a + b) % MOD

# Subtraction (add MOD to prevent negative)
result = (a - b + MOD) % MOD

# Multiplication
result = (a * b) % MOD

# Power — use Python's built-in pow (very fast!)
result = pow(a, b, MOD)   # a^b mod MOD
```

### Modular Inverse
Needed for **division in modular arithmetic** (when MOD is prime):
```python
# Method 1: Fermat's little theorem (MOD must be prime)
inv_b = pow(b, MOD - 2, MOD)
result = a * inv_b % MOD   # a / b mod MOD

# Method 2: Extended GCD (works for any MOD)
def modinv(a, m):
    g, x = ext_gcd(a, m)
    return x % m if g == 1 else -1

def ext_gcd(a, b):
    if a == 0: return b, 0
    g, x = ext_gcd(b % a, a)
    return g, (1 - (b // a) * x)   # simplified
```

---

## 🔥 Common Python Math Operations

```python
from math import gcd, lcm, isqrt, comb

# GCD and LCM
gcd(12, 8)          # 4
lcm(4, 6)           # 12

# Integer square root (exact, no float error)
isqrt(16)           # 4
isqrt(17)           # 4 (floor)

# Combinations nCr (Python 3.8+)
comb(10, 3)         # 120

# Power (fast, modular)
pow(2, 100, MOD)    # 2^100 mod MOD
```

---

## 📝 Exercises

### Exercise 1 — Modular Power
Compute `a^b mod (10^9+7)`. (a, b up to 10^9)
```
Input:  2 10
Output: 1024
```

### Exercise 2 — Large Fibonacci
Compute Fibonacci(n) mod (10^9+7). (n up to 10^6)
```
Input:  10
Output: 55
```

### Exercise 3 — Modular Division
Compute `(a / b) mod (10^9+7)` where division is exact in math.
```
Input:  10 2
Output: 5
```

### Exercise 4 — Sum of Powers
Compute `1^k + 2^k + 3^k + ... + n^k mod (10^9+7)`.
```
Input:  3 2
Output: 14    (1 + 4 + 9)
```

---

## 🔗 Codeforces Practice
1. [A. Modular Exponentiation](https://codeforces.com/problemset/problem/913/B)
2. [B. New Year and Ancient Prophecy](https://codeforces.com/problemset/problem/1070/E)
3. [A. Lucky Division](https://codeforces.com/problemset/problem/121/A)

---

## 💡 Key Takeaways
- Python has **no integer overflow** — big advantage over C++
- Always use `pow(a, b, mod)` — it's O(log b) and built-in
- `(a - b + MOD) % MOD` prevents negative modular results
- `from math import gcd, lcm, isqrt, comb` — know these!
