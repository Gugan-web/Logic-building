# Day 17 — DP: LCS, LIS & Edit Distance

## 🎯 Goals
- Implement LCS in O(n×m)
- Implement LIS in **O(n log n)** using patience sorting
- Solve Edit Distance (Levenshtein distance)

---

## 🔤 LCS — Longest Common Subsequence

**State:** `dp[i][j]` = LCS length of `s[:i]` and `t[:j]`

**Transition:**
```python
if s[i-1] == t[j-1]:   dp[i][j] = dp[i-1][j-1] + 1
else:                   dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```
Time: O(n×m), Space: O(n×m) or O(m) with optimization

---

## 📈 LIS — Longest Increasing Subsequence

### O(n log n) — Patience Sorting
```python
from bisect import bisect_left

tails = []
for x in a:
    pos = bisect_left(tails, x)  # find position to place x
    if pos == len(tails):
        tails.append(x)          # extend LIS
    else:
        tails[pos] = x           # replace with smaller tail
# len(tails) = LIS length
```

---

## ✏️ Edit Distance

Minimum operations (insert, delete, replace) to transform `s` into `t`.

```python
dp[i][j] = min(
    dp[i-1][j] + 1,      # delete from s
    dp[i][j-1] + 1,      # insert into s
    dp[i-1][j-1] + (0 if s[i-1]==t[j-1] else 1)  # replace
)
```

---

## 📝 Exercises

### Exercise 1 — LCS with Reconstruction
Print both the LCS length and the actual sequence.

### Exercise 2 — LIS (O(n log n))
```
Input:  8 / 10 9 2 5 3 7 101 18
Output: 4   (2,3,7,101 or 2,5,7,101)
```

### Exercise 3 — Edit Distance
```
Input:  kitten / sitting
Output: 3
```

### Exercise 4 — LDS (Longest Decreasing Subsequence)
Hint: negate all values and find LIS.

### Exercise 5 — Count all LIS
```
Input:  5 / 1 3 5 4 7
Output: 2   (two LIS of length 4)
```

---

## 🔗 Codeforces Practice
1. [B. Polycarp's Letters](https://codeforces.com/problemset/problem/978/D)
2. [C. Increasing Sequence](https://codeforces.com/problemset/problem/1207/D)
3. [D. LIS Count](https://codeforces.com/problemset/problem/570/E)
