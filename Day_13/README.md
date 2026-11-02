# Day 13 — Number Theory

## 🎯 Goals
- Master GCD, LCM, and their applications
- Implement the Sieve of Eratosthenes
- Understand prime factorization using SPF sieve

---

## 🔢 GCD & LCM

```python
from math import gcd
def lcm(a, b): return a // gcd(a, b) * b

gcd(48, 18)   # 6
lcm(4, 6)     # 12
```

**Key property:** `gcd(a, b) * lcm(a, b) = a * b`

---

## 🔍 Primality Check — O(√n)

```python
from math import isqrt
def is_prime(n):
    if n < 2: return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0: return False
    return True
```

---

## 🔭 Sieve of Eratosthenes — O(n log log n)

Finds all primes up to n. For n = 10^7, use `bytearray` (10x less memory):

```python
def sieve(n):
    is_prime = bytearray([1]) * (n+1)
    is_prime[0] = is_prime[1] = 0
    for i in range(2, isqrt(n)+1):
        if is_prime[i]:
            is_prime[i*i::i] = bytearray(len(is_prime[i*i::i]))
    return [i for i in range(n+1) if is_prime[i]]
```

---

## 📝 Exercises

### Exercise 1 — GCD & LCM
Print GCD and LCM of two numbers.

### Exercise 2 — Prime Check
Given n (up to 10^12), check if prime. Hint: trial division up to √n.

### Exercise 3 — Count Primes up to N
Using Sieve. N up to 10^7.
```
Input: 10    Output: 4   (2,3,5,7)
```

### Exercise 4 — Prime Factorization
Print prime factorization of n.
```
Input: 360    Output: 2^3 * 3^2 * 5
```

### Exercise 5 — Goldbach Conjecture
Express even n > 2 as sum of two primes.
```
Input: 28    Output: 5 23
```

---

## 🔗 Codeforces Practice
1. [A. Choosing Teams](https://codeforces.com/problemset/problem/432/A)
2. [B. Divisors](https://codeforces.com/problemset/problem/448/B)
3. [C. Primes or Palindromes?](https://codeforces.com/problemset/problem/568/B)
4. [D. Sieve](https://codeforces.com/problemset/problem/862/D)
