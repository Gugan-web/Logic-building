# Day 07 — Stack, Queue (deque) & Heap (heapq)

## 🎯 Goals
- Implement stack and queue efficiently using Python's `deque`
- Use `heapq` for priority queue problems
- Recognize which problems need each structure

---

## 📦 Stack (LIFO)

Use Python `list` as a stack:
```python
stack = []
stack.append(x)     # push  O(1)
stack.pop()         # pop   O(1)
stack[-1]           # peek  O(1)
len(stack) == 0     # empty check
```

**When to use:** Matching brackets, undo operations, DFS (iterative), monotonic stack

---

## 🚂 Queue (FIFO)

**Never use `list.pop(0)` — it's O(n)!** Use `deque`:
```python
from collections import deque

q = deque()
q.append(x)         # enqueue right  O(1)
q.appendleft(x)     # enqueue left   O(1)
q.popleft()         # dequeue        O(1)
q.pop()             # pop right      O(1)
q[0]                # front element  O(1)
```

**When to use:** BFS, sliding window, level-order traversal

---

## 🔺 Heap / Priority Queue (heapq)

Python's `heapq` is a **min-heap**:
```python
import heapq

h = []
heapq.heappush(h, 5)       # push
heapq.heappop(h)            # pop minimum
h[0]                        # peek minimum (no pop)
heapq.heapify(a)            # convert list to heap O(n)

# Max-heap trick: negate values!
heapq.heappush(h, -x)       # push as negative
-heapq.heappop(h)           # pop maximum

# Push (value, item) tuples for custom priority
heapq.heappush(h, (dist, node))
dist, node = heapq.heappop(h)
```

**When to use:** Dijkstra, task scheduling, K-th largest/smallest

---

## 📝 Exercises

### Exercise 1 — Valid Brackets
Check if a string of brackets `()[]{}` is valid.
```
Input:  ([{}])
Output: YES

Input:  ([)]
Output: NO
```

### Exercise 2 — Sliding Window Maximum
Find maximum in every window of size k.
```
Input:  5 3 / 1 3 -1 -3 5
Output: 3 3 5
```

### Exercise 3 — K Largest Elements
Find the k largest elements from a stream without sorting all.
```
Input:  6 3 / 3 1 4 1 5 9
Output: 4 5 9
```

### Exercise 4 — Stock Span
For each day, find how many consecutive previous days had stock price ≤ today.

### Exercise 5 — Merge K Sorted Lists
Merge k sorted arrays using a heap.

---

## 🔗 Codeforces Practice
1. [B. Queue at School](https://codeforces.com/problemset/problem/266/B)
2. [C. Vasya and String](https://codeforces.com/problemset/problem/671/C)
3. [B. Maximum Sum of Digits](https://codeforces.com/problemset/problem/1217/B)
4. [D. Primitive Divisors](https://codeforces.com/problemset/problem/sspds)
