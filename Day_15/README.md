# Day 15 — Dynamic Programming: Introduction

## 🎯 Goals
- Understand memoization vs tabulation
- Use Python's `@lru_cache` for instant memoization
- Solve classic intro DP problems

---

## 🧠 What is DP?

DP = **Recursion + Memoization** (top-down) or **Iteration + Table** (bottom-up)

Use DP when:
1. The problem has **overlapping subproblems** (same subproblem computed multiple times)
2. The problem has **optimal substructure** (optimal solution built from optimal sub-solutions)

---

## 🔝 Top-Down (Memoization) with `@lru_cache`

```python
from functools import lru_cache
import sys
sys.setrecursionlimit(300000)

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)
```

**Pros:** Easy to write (think recursively), only computes needed states  
**Cons:** Recursion overhead, stack overflow risk for deep recursion

---

## 🔽 Bottom-Up (Tabulation)

```python
def fib(n):
    if n <= 1: return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

**Pros:** No recursion, faster in practice, predictable memory  
**Cons:** Need to identify correct order of computation

---

## 📝 Exercises

### Exercise 1 — Fibonacci
Compute Fibonacci(n) mod 10^9+7. n up to 10^6.

### Exercise 2 — Climbing Stairs
Ways to climb n stairs (can take 1 or 2 steps at a time).
```
Input: 5    Output: 8
```

### Exercise 3 — Coin Change (Min Coins)
Minimum coins to make amount n from given denominations.
```
Input:  3 11 / 1 5 6
Output: 2   (5+6=11)
```

### Exercise 4 — Longest Common Subsequence (LCS)
Classic DP — find length of LCS of two strings.
```
Input:  ABCBDAB / BDCABA
Output: 4
```

### Exercise 5 — Maximum Subarray (DP view)
Kadane's algorithm as DP.

### Exercise 6 — House Robber
Rob max value from houses — can't rob adjacent.
```
Input:  5 / 2 7 9 3 1
Output: 12   (2+9+1)
```

---

## 🔗 Codeforces Practice
1. [A. Codeforces Subsequences](https://codeforces.com/problemset/problem/977/D)
2. [B. Vasya and Painting](https://codeforces.com/problemset/problem/1119/C)
3. [C. Sagheer and Digits](https://codeforces.com/problemset/problem/812/C)
4. [B. Number of Pairs](https://codeforces.com/problemset/problem/1538/C)

---

## 💡 DP Tips
- Start with brute force recursion → add memoization → optimize to tabulation
- State = what information you need to make decisions
- Transition = how to compute `dp[i]` from smaller states
- Base cases = simplest states with known answers
