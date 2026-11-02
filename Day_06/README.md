# Day 06 — dict, set, Counter & defaultdict

## 🎯 Goals
- Use `dict` and `set` as O(1) lookup structures
- Master `Counter` and `defaultdict` for frequency problems
- Know when to use each data structure

---

## 📘 dict — Hash Map

```python
d = {}
d['key'] = 10                  # insert / update
d.get('key', 0)                # get with default (no KeyError)
'key' in d                     # membership check O(1)
del d['key']                   # delete
d.items()                      # (key, value) pairs
d.keys(), d.values()           # key/value views
```

### Frequency counting with dict
```python
freq = {}
for x in a:
    freq[x] = freq.get(x, 0) + 1
```

---

## 📗 defaultdict — Auto-initializing dict

```python
from collections import defaultdict

# No KeyError — default value automatically set
freq = defaultdict(int)        # default: 0
graph = defaultdict(list)      # default: []
visited = defaultdict(bool)    # default: False

for x in a:
    freq[x] += 1               # no need to check if key exists

# Adjacency list for graphs
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)
```

---

## 📕 Counter — Frequency Counter

```python
from collections import Counter

a = [1, 2, 2, 3, 3, 3]
cnt = Counter(a)
# Counter({3: 3, 2: 2, 1: 1})

cnt[3]                  # 3
cnt[99]                 # 0 (no KeyError)
cnt.most_common(2)      # [(3,3), (2,2)]
cnt.most_common()       # all, sorted by count desc

# On strings
Counter("abracadabra")  # {'a':5,'b':2,'r':2,'c':1,'d':1}

# Arithmetic on counters
c1 = Counter("hello")
c2 = Counter("world")
c1 + c2                 # union (add counts)
c1 - c2                 # subtract (positive only)
c1 & c2                 # intersection (min of counts)
c1 | c2                 # union (max of counts)
```

---

## 📙 set — O(1) Lookup & Set Operations

```python
s = {1, 2, 3}
s.add(4)                # O(1)
s.remove(2)             # KeyError if missing
s.discard(99)           # safe remove (no error)
2 in s                  # O(1) membership
s & {2,3,4}             # intersection
s | {4,5}               # union
s - {1,3}               # difference
```

---

## 📝 Exercises

### Exercise 1 — Two Sum
Find two indices i, j such that a[i] + a[j] = target.
```
Input:  4 9 / 2 7 11 15
Output: 0 1
```

### Exercise 2 — Anagram Check
Check if two strings are anagrams.
```
Input:  listen / silent
Output: YES
```

### Exercise 3 — First Non-Repeating Character
Find the first character in a string that doesn't repeat.
```
Input:  aabbc
Output: c
```

### Exercise 4 — Group Anagrams
Group a list of words by anagram family.

### Exercise 5 — Subarray with Given Sum
Count subarrays with sum exactly k (using prefix sum + dict).

---

## 🔗 Codeforces Practice
1. [A. Mike and palindrome](https://codeforces.com/problemset/problem/798/A)
2. [B. Queries about less or equal elements](https://codeforces.com/problemset/problem/600/B)
3. [B. Vasya and strings](https://codeforces.com/problemset/problem/671/B)
4. [C. Kefa and Park](https://codeforces.com/problemset/problem/580/C)
