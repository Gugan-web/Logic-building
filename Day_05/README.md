# Day 05 — Python Built-ins, Comprehensions & itertools

## 🎯 Goals
- Master Python's powerful built-in functions for CP
- Use list/set/dict comprehensions to write concise code
- Know itertools functions that save time in contests

---

## 🔧 Essential Built-ins

```python
# Math
abs(-5)         # 5
min(3, 1, 4)    # 1
max(3, 1, 4)    # 4
sum([1,2,3])    # 6
pow(2,10,MOD)   # fast modular power

# Sorting
sorted([3,1,2])              # new list [1,2,3]
sorted(a, key=lambda x: x[1])  # sort by second element
a.sort(key=lambda x: -x[0])    # in-place, descending by first

# Enumerate & Zip
list(enumerate(['a','b','c']))  # [(0,'a'),(1,'b'),(2,'c')]
list(zip([1,2],[3,4]))          # [(1,3),(2,4)]

# Reduce (use accumulate instead)
from functools import reduce
reduce(lambda a,b: a*b, [1,2,3,4])  # 24

# Accumulate (prefix operations)
from itertools import accumulate
list(accumulate([1,2,3,4]))          # [1,3,6,10]  prefix sum
list(accumulate([1,2,3,4], max))     # [1,2,3,4]  prefix max
```

---

## 🧩 Comprehensions

```python
# List comprehension
squares = [x*x for x in range(10)]
filtered = [x for x in a if x > 0]
flat = [x for row in grid for x in row]

# Set comprehension
unique = {x % 3 for x in range(10)}

# Dict comprehension
freq = {x: a.count(x) for x in a}

# Generator (memory efficient, use with sum/min/max)
total = sum(x*x for x in range(10**6))
```

---

## 🔄 itertools Essentials

```python
from itertools import (
    permutations,   # all orderings
    combinations,   # choose r from n
    combinations_with_replacement,
    product,        # cartesian product
    accumulate,     # prefix operations
    groupby,        # group consecutive equal elements
    chain,          # flatten iterables
    islice,         # slice an iterator
)

# Permutations
list(permutations([1,2,3]))      # all 6 orderings
list(permutations([1,2,3], 2))  # choose 2

# Combinations
list(combinations([1,2,3,4], 2)) # (1,2),(1,3),(1,4),(2,3),(2,4),(3,4)

# Product (nested loops replacement)
for i, j in product(range(3), range(3)):
    print(i, j)  # same as nested for i,j loops

# Chain (flatten)
from itertools import chain
flat = list(chain([1,2], [3,4], [5]))  # [1,2,3,4,5]
```

---

## 📝 Exercises

### Exercise 1 — All Pairs Sum
Given n numbers, find the minimum sum of any pair (i ≠ j).
```
Input:  4 / 3 1 4 1
Output: 2
```

### Exercise 2 — Frequency Map
Given n numbers, output each distinct number and its count, sorted by number.

### Exercise 3 — Generate All Subsets
For a small array (n ≤ 20), generate all 2^n subsets.

### Exercise 4 — Prefix Max Array
Given an array, output the prefix maximum at each position.
```
Input:  5 / 3 1 4 1 5
Output: 3 3 4 4 5
```

---

## 🔗 Codeforces Practice
1. [A. Helpful Maths](https://codeforces.com/problemset/problem/339/A) — sorting strings
2. [A. Beautiful Matrix](https://codeforces.com/problemset/problem/263/A)
3. [B. Maximum of Maximums of Minimums](https://codeforces.com/problemset/problem/808/C)
