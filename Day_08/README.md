# Day 08 — Sorting & Binary Search (bisect)

## 🎯 Goals
- Master Python's sorting with custom keys
- Use `bisect` module for O(log n) search on sorted arrays
- Implement binary search from scratch

---

## 🔃 Sorting

```python
# Sort in-place
a.sort()
a.sort(reverse=True)
a.sort(key=lambda x: x[1])       # sort by index 1
a.sort(key=lambda x: (x[1], -x[0]))  # multi-key sort

# Return new sorted list
sorted(a)
sorted(a, key=abs)                # sort by absolute value
sorted(words, key=len)            # sort by length

# Sorting strings like integers
strs.sort(key=lambda s: int(s))
```

---

## 🔎 Binary Search — The Template

```python
def binary_search(a, target):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1  # not found
```

### Find first position ≥ target (lower bound)
```python
lo, hi = 0, len(a)
while lo < hi:
    mid = (lo + hi) // 2
    if a[mid] < target:  lo = mid + 1
    else:                hi = mid
# lo = first index where a[lo] >= target
```

---

## 📦 bisect Module (Built-in Binary Search)

```python
from bisect import bisect_left, bisect_right, insort

a = [1, 3, 3, 5, 7]

bisect_left(a, 3)    # 1 — first index where 3 can be inserted (leftmost)
bisect_right(a, 3)   # 3 — first index after all 3s (rightmost + 1)

# Count occurrences of x in sorted array
count = bisect_right(a, x) - bisect_left(a, x)

# Insert while keeping sorted
insort(a, 4)         # a = [1,3,3,4,5,7]

# Lower bound (first element >= x)
idx = bisect_left(a, x)

# Upper bound (first element > x)
idx = bisect_right(a, x)
```

---

## 📝 Exercises

### Exercise 1 — Search in Sorted Array
Given sorted array and target, return index or -1.

### Exercise 2 — Count Range
In sorted array, count elements in range [L, R].
```
Input:  5 / 1 3 5 7 9 / L=3 R=7
Output: 3
```

### Exercise 3 — Find Insert Position
Find where to insert x in sorted array to keep it sorted.

### Exercise 4 — Sort by Frequency
Sort array so that more frequent elements come first. Ties: smaller number first.
```
Input:  6 / 1 1 2 2 2 3
Output: 2 2 2 1 1 3
```

### Exercise 5 — Merge Sort (implement manually)
Implement merge sort and count inversions.

---

## 🔗 Codeforces Practice
1. [B. Vasya and Sorting](https://codeforces.com/problemset/problem/41/B)
2. [C. Number of Pairs](https://codeforces.com/problemset/problem/1538/C)
3. [B. Maximum Sum of Digits](https://codeforces.com/problemset/problem/1217/B)
4. [C. Fafa and his Company](https://codeforces.com/problemset/problem/935/C)
