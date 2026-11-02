# Day 23 — Disjoint Set Union (DSU / Union-Find)

## 🎯 Goals
- Implement DSU with path compression + union by rank
- Use DSU for connected components and Kruskal's MST
- Solve online connectivity queries

---

## 🔗 DSU — The Magic of O(α(n)) ≈ O(1)

Two optimizations make DSU nearly constant time:
1. **Path compression:** Flatten the tree during `find()`
2. **Union by rank:** Always attach smaller tree under larger

```python
def find(self, x):
    while self.parent[x] != x:
        self.parent[x] = self.parent[self.parent[x]]  # path halving
        x = self.parent[x]
    return x

def union(self, x, y):
    px, py = self.find(x), self.find(y)
    if px == py: return False
    if self.rank[px] < self.rank[py]: px, py = py, px
    self.parent[py] = px
    ...
```

---

## 🌲 Kruskal's MST

```python
edges.sort()   # sort by weight
for w, u, v in edges:
    if dsu.union(u, v):   # only add if connects two components
        mst_cost += w
```

---

## 📝 Exercises

### Exercise 1 — Connected Components
Count number of connected components.

### Exercise 2 — Kruskal's MST
Find minimum spanning tree cost.

### Exercise 3 — Cycle Detection
Does adding this edge create a cycle?

### Exercise 4 — Largest Component
Size of the largest connected component.

### Exercise 5 — Online Queries
Mix of union and find operations.

---

## 🔗 Codeforces Practice
1. [C. Vasya and Union-Find](https://codeforces.com/problemset/problem/368/C)
2. [D. Roads in Berland](https://codeforces.com/problemset/problem/196/E)
3. [C. Greg and Graph](https://codeforces.com/problemset/problem/295/B)
4. [E. Arpa's letter-marked tree](https://codeforces.com/problemset/problem/850/E)
