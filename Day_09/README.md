# Day 09 — Two Pointers & Sliding Window

## 🎯 Goals
- Master the two-pointer technique for O(n) solutions
- Use sliding window for subarray/substring problems
- Recognize when these patterns apply

---

## 👆👆 Two Pointers

Two pointers works when the array is **sorted** or when you need to find pairs/triples.

### Pattern: Sum of two numbers
```python
a.sort()
lo, hi = 0, len(a) - 1
while lo < hi:
    s = a[lo] + a[hi]
    if s == target:
        # found!
        lo += 1; hi -= 1
    elif s < target:
        lo += 1
    else:
        hi -= 1
```

### Pattern: Remove duplicates in-place
```python
a.sort()
write = 1
for read in range(1, n):
    if a[read] != a[write - 1]:
        a[write] = a[read]
        write += 1
# unique elements: a[:write]
```

---

## 🪟 Sliding Window

Use when you need the **best/count of subarrays** of fixed or variable size.

### Fixed Window (size k)
```python
window_sum = sum(a[:k])
best = window_sum
for i in range(k, n):
    window_sum += a[i] - a[i - k]   # slide: add new, remove old
    best = max(best, window_sum)
```

### Variable Window (find min length with sum >= S)
```python
lo = 0
window_sum = 0
min_len = float('inf')
for hi in range(n):
    window_sum += a[hi]
    while window_sum >= S:
        min_len = min(min_len, hi - lo + 1)
        window_sum -= a[lo]
        lo += 1
```

---

## 📝 Exercises

### Exercise 1 — Two Sum (Sorted Array)
Find two indices i < j such that a[i] + a[j] = target.
```
Input:  4 9 / 2 7 11 15
Output: 0 1
```

### Exercise 2 — Max Subarray Sum (Kadane's)
Find the maximum sum contiguous subarray.
```
Input:  8 / -2 1 -3 4 -1 2 1 -5
Output: 6
```

### Exercise 3 — Minimum Window Substring
Find smallest substring of s containing all characters of t.

### Exercise 4 — Longest Subarray with Sum ≤ K
Find longest subarray where sum does not exceed k.

### Exercise 5 — 3 Sum
Find all unique triplets that sum to 0.

---

## 🔗 Codeforces Practice
1. [B. Ants](https://codeforces.com/problemset/problem/6/C)
2. [C. Common Divisors](https://codeforces.com/problemset/problem/1204/C)
3. [B. Two Buttons](https://codeforces.com/problemset/problem/520/B)
4. [C. Vasya and Multiset](https://codeforces.com/problemset/problem/1051/C)
