# Day 04 — Lists & Strings

## 🎯 Goals
- Master Python list operations used in competitive programming
- Handle string manipulation efficiently
- Know which operations are O(1) vs O(n)

---

## 📋 List Operations & Complexity

| Operation | Syntax | Complexity |
|-----------|--------|------------|
| Access | `a[i]` | O(1) |
| Append | `a.append(x)` | O(1) amortized |
| Pop from end | `a.pop()` | O(1) |
| Pop from front | `a.pop(0)` | **O(n)** — use deque! |
| Insert | `a.insert(i, x)` | O(n) |
| Sort | `a.sort()` | O(n log n) |
| Reverse | `a.reverse()` | O(n) |
| Search | `x in a` | O(n) |
| Count | `a.count(x)` | O(n) |
| Slice | `a[l:r]` | O(r-l) |

---

## 🔥 Essential List Tricks

```python
# Create filled list
a = [0] * n
a = [[] for _ in range(n)]   # 2D list — use this, NOT [[]] * n !

# List comprehension
squares = [i*i for i in range(n)]
evens   = [x for x in a if x % 2 == 0]

# Min/Max/Sum
print(min(a), max(a), sum(a))

# Sorted (returns new list)
b = sorted(a)              # ascending
b = sorted(a, reverse=True) # descending
b = sorted(a, key=lambda x: -x)  # custom key

# Reverse
a.reverse()          # in-place
a[::-1]              # new reversed list

# Flatten 2D list
flat = [x for row in grid for x in row]
```

---

## 🔤 String Tricks

```python
s = "Hello World"

s.lower()        # "hello world"
s.upper()        # "HELLO WORLD"
s.strip()        # remove leading/trailing whitespace
s.split()        # ['Hello', 'World']
s.split(',')     # split by comma
'|'.join(['a','b','c'])  # "a|b|c"

s[2:5]           # "llo"  (slicing)
s[::-1]          # "dlroW olleH" (reverse)
s.count('l')     # 3
s.find('o')      # 4 (first index, -1 if not found)
s.replace('l','L')  # "HeLLo WorLd"

# Check type
s.isdigit()      # all digits?
s.isalpha()      # all letters?
s.isalnum()      # all alphanumeric?

# Convert int to/from string
str(42)          # "42"
int("42")        # 42
list("abc")      # ['a', 'b', 'c']
```

---

## 📝 Exercises

### Exercise 1 — Rotate Array
Given array a of n elements and rotation count k, rotate left by k positions.
```
Input:  5 2 / 1 2 3 4 5
Output: 3 4 5 1 2
```

### Exercise 2 — Palindrome Check
Check if a string is a palindrome (ignore case, consider only alphanumeric).
```
Input:  "A man a plan a canal Panama"
Output: YES
```

### Exercise 3 — Most Frequent Element
Find the most frequently occurring element in an array.

### Exercise 4 — String Compression
Compress "aaabbbcc" → "a3b3c2".

### Exercise 5 — 2D Grid Max
Find maximum element in a 2D grid.

---

## 🔗 Codeforces Practice
1. [A. String Task](https://codeforces.com/problemset/problem/118/A) — string operations
2. [A. Petya and Strings](https://codeforces.com/problemset/problem/96/A)
3. [B. Vasya and String](https://codeforces.com/problemset/problem/671/B)
4. [A. Pangram](https://codeforces.com/problemset/problem/520/A)

---

## ⚠️ Common Pitfalls

```python
# WRONG: All rows share the same list!
grid = [[0] * m] * n
grid[0][0] = 1   # changes ALL rows!

# CORRECT:
grid = [[0] * m for _ in range(n)]
```
