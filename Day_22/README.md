# Day 22 — Segment Trees & BIT (Fenwick Tree)

## 🎯 Goals
- Implement a Segment Tree for range queries
- Add lazy propagation for range updates
- Use BIT for simpler prefix sum / inversion count

---

## 🌲 When to Use Each

| Problem | Use |
|---------|-----|
| Range sum / max / min, point update | Segment Tree |
| Range update (add to range), range query | Lazy Seg Tree |
| Prefix sums + point updates | BIT (simpler, 2x faster) |
| Count inversions | BIT |

---

## 📦 BIT — Fenwick Tree

```python
class BIT:
    def __init__(self, n):
        self.tree = [0] * (n+1)
        self.n = n

    def update(self, i, delta):  # 1-indexed
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):          # prefix sum [1..i]
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s
```

---

## 📝 Exercises

### Exercise 1 — Range Max with Updates
Support: `U i v` (update a[i]=v), `Q l r` (max of a[l..r]).

### Exercise 2 — BIT Prefix Sum
Support: `U i v` (set a[i]=v), `Q l r` (sum of a[l..r]).

### Exercise 3 — Count Inversions
Count pairs (i,j) where i<j but a[i]>a[j] using BIT.
```
Input:  5 / 3 1 4 1 5
Output: 3
```

---

## 🔗 Codeforces Practice
1. [D. Nested Segments](https://codeforces.com/problemset/problem/652/D)
2. [E. Little Artem and Time Machine](https://codeforces.com/problemset/problem/632/E)
3. [C. Arpa and a game with Mojtaba](https://codeforces.com/problemset/problem/850/C)
