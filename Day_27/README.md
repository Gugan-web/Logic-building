# Day 27 — Binary Search on Answer

## 🎯 Goals
- Recognize problems where the answer space is monotonic
- Apply "binary search + feasibility check" pattern
- Handle both integer and floating point binary search

---

## 🔑 The Key Insight

**"Binary search on answer"** = when you can't compute the answer directly, but you can check: *"Is X a valid answer?"*

If `feasible(X)` is monotonic:
- If X works, then all Y > X also work → find **minimum** feasible X
- If X works, then all Y < X also work → find **maximum** feasible X

```python
def binary_search_answer(lo, hi, feasible):
    result = hi
    while lo <= hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            result = mid   # X works, but try smaller
            hi = mid - 1
        else:
            lo = mid + 1   # X doesn't work, need larger
    return result
```

---

## 💡 Recognition Clues
- "Minimize the maximum..."
- "Maximize the minimum..."
- "Find the smallest k such that..."
- "At least k operations..."

---

## 📝 Exercises

### Exercise 1 — Koko Eating Bananas
Find minimum eating speed k so Koko finishes all piles in h hours.

### Exercise 2 — Allocate Minimum Pages
Divide n books among m students to minimize max pages any student reads.

### Exercise 3 — Aggressive Cows (SPOJ Classic)
Place k cows in stalls to maximize minimum distance between any two cows.

### Exercise 4 — Smallest Divisor
Find smallest divisor d so `sum(ceil(a[i]/d)) <= threshold`.

### Exercise 5 — Nth Root (float binary search)
Find x such that x^n = target.

---

## 🔗 Codeforces Practice
1. [C. Magic Ship](https://codeforces.com/problemset/problem/1117/C) — binary search on time
2. [D. Enduring Exodus](https://codeforces.com/problemset/problem/1585/F)
3. [B. Mahmoud and Ehab and the Xor](https://codeforces.com/problemset/problem/862/E)
4. [C. Vasya and Robot](https://codeforces.com/problemset/problem/1073/E)
