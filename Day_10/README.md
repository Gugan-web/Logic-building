# Day 10 — Prefix Sums & Difference Arrays

## 🎯 Goals
- Use prefix sums to answer range queries in O(1)
- Use difference arrays for range update in O(1)
- Apply 2D prefix sums for grid problems

---

## ➕ Prefix Sum (1D)

Precompute `prefix[i] = a[0] + a[1] + ... + a[i-1]`

```python
n = len(a)
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i+1] = prefix[i] + a[i]

# Range sum query [l, r] in O(1):
range_sum = prefix[r+1] - prefix[l]
```

Or using `itertools.accumulate`:
```python
from itertools import accumulate
prefix = [0] + list(accumulate(a))
```

---

## 📐 2D Prefix Sum

```python
# Build
ps = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        ps[i][j] = a[i-1][j-1] + ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1]

# Query: sum of rectangle (r1,c1) to (r2,c2) [0-indexed, inclusive]
def query(r1, c1, r2, c2):
    return ps[r2+1][c2+1] - ps[r1][c2+1] - ps[r2+1][c1] + ps[r1][c1]
```

---

## 📊 Difference Array (Range Updates)

When you need to **add v to all elements in range [l, r]** many times:

```python
diff = [0] * (n + 2)

def range_add(l, r, v):
    diff[l] += v
    diff[r+1] -= v

# Reconstruct actual array after all updates:
actual = []
curr = 0
for i in range(n):
    curr += diff[i]
    actual.append(curr)
```

---

## 📝 Exercises

### Exercise 1 — Range Sum Queries
Given array and q queries each asking sum of [l, r].
```
Input:
5 3
1 2 3 4 5
0 2
1 3
2 4

Output:
6
9
12
```

### Exercise 2 — Count Prefix Sums Equal to K
Count subarrays with sum exactly k (use prefix sum + dict).

### Exercise 3 — Range Add, Point Query
Apply m range additions, then answer point queries.

### Exercise 4 — 2D Grid Sum
Answer q queries: sum of rectangle (r1,c1) to (r2,c2).

### Exercise 5 — Equilibrium Index
Find index i where sum(a[:i]) == sum(a[i+1:]).

---

## 🔗 Codeforces Practice
1. [B. Little Girl and Maximum Sum](https://codeforces.com/problemset/problem/276/C)
2. [C. Ants](https://codeforces.com/problemset/problem/6/C)
3. [B. Prime Matrix](https://codeforces.com/problemset/problem/271/B)
4. [D. Vasya and Arrays](https://codeforces.com/problemset/problem/1037/C)
