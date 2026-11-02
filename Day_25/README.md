# Day 25 — Combinatorics & Modular Inverse

## 🎯 Goals
- Precompute factorials for O(1) nCr queries
- Solve stars-and-bars, paths, derangements
- Apply inclusion-exclusion principle

---

## 🔢 Key Formulas

| Formula | Description |
|---------|-------------|
| `C(n,r) = n! / (r! × (n-r)!)` | Combinations (choose r from n) |
| `P(n,r) = n! / (n-r)!` | Permutations |
| `C(n+k-1, k-1)` | Distribute n items into k bins (stars & bars) |
| `C(n+m, n)` | Grid paths from (0,0) to (n,m) |
| `D(n) = (n-1)(D(n-1) + D(n-2))` | Derangements |
| `Cat(n) = C(2n,n) / (n+1)` | Catalan number |

---

## ⚡ Precomputed Factorials

```python
fact   = [1] * (MAXN + 1)
inv_f  = [1] * (MAXN + 1)
for i in range(1, MAXN+1):
    fact[i] = fact[i-1] * i % MOD
inv_f[MAXN] = pow(fact[MAXN], MOD-2, MOD)
for i in range(MAXN-1, -1, -1):
    inv_f[i] = inv_f[i+1] * (i+1) % MOD

def nCr(n, r):
    if r < 0 or r > n: return 0
    return fact[n] * inv_f[r] % MOD * inv_f[n-r] % MOD
```

---

## 📝 Exercises

### Exercise 1 — nCr mod MOD
```
Input:  10 3    Output: 120
```

### Exercise 2 — Stars and Bars
Ways to put n identical balls into k distinct boxes.
```
Input:  4 3     Output: 15   (C(6,2))
```

### Exercise 3 — Grid Paths
```
Input:  3 7     Output: 120
```

### Exercise 4 — Derangements
```
Input:  4       Output: 9
```

### Exercise 5 — Inclusion-Exclusion
Count integers 1..n divisible by at least one prime in list.

### Exercise 6 — Catalan Number
```
Input:  3       Output: 5   (5 valid bracket sequences of length 6)
```

---

## 🔗 Codeforces Practice
1. [D. Vasya and Triangle](https://codeforces.com/problemset/problem/1030/D)
2. [C. Tokitsukaze and Discard](https://codeforces.com/problemset/problem/1190/C)
3. [E. Subsets](https://codeforces.com/problemset/problem/566/E)
