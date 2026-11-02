# Day 24 — String Algorithms: KMP & Z-Function

## 🎯 Goals
- Implement Z-function for pattern matching in O(n)
- Understand KMP failure function
- Solve string period, rotation, and occurrence problems

---

## 🔤 Z-Function

`z[i]` = length of the longest string starting at position `i` that is also a prefix of `s`.

```python
def z_function(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z
```

**Find pattern in text:** Compute z for `pattern + '#' + text`. Position `i` has a match if `z[i] == len(pattern)`.

---

## 🔄 String Period

Using KMP failure function: `period = n - fail[n-1]` (if `n % period == 0`).

---

## 📝 Exercises

### Exercise 1 — Pattern Occurrences
Find all positions of pattern in text.
```
Input:  aababab / ab
Output: 2 / 2 4
```

### Exercise 2 — Shortest Period
Find the shortest repeating period of a string.
```
Input:  abababab    Output: 2
```

### Exercise 3 — Distinct Substrings
Count distinct substrings of s.

### Exercise 4 — String Rotation Check
Is s2 a rotation of s1?

### Exercise 5 — Longest Palindromic Prefix

---

## 🔗 Codeforces Practice
1. [B. Password](https://codeforces.com/problemset/problem/126/E) — KMP prefix function
2. [E. Minimal Spanning Tree](https://codeforces.com/problemset/problem/1100/E)
3. [D. Petya and Exam](https://codeforces.com/problemset/problem/526/F)
