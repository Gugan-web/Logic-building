# Day 19 — Graph Theory: BFS & DFS

## 🎯 Goals
- Build adjacency list graphs from edge input
- Implement BFS (shortest path, level order)
- Implement DFS (iterative preferred for large graphs)
- Detect cycles and bipartiteness

---

## 🔗 Graph Representation

```python
from collections import defaultdict
g = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)    # omit for directed graph
```

---

## 🌊 BFS — Level-by-Level Traversal

```python
from collections import deque

def bfs(start):
    dist = {start: 0}
    q = deque([start])
    while q:
        node = q.popleft()
        for nb in graph[node]:
            if nb not in dist:
                dist[nb] = dist[node] + 1
                q.append(nb)
    return dist
```

**Use BFS for:** Shortest path (unweighted), level traversal, bipartite check

---

## 🌲 DFS — Depth First

```python
# Iterative (preferred — no recursion limit issues)
def dfs(start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited: continue
        visited.add(node)
        for nb in graph[node]: stack.append(nb)
    return visited
```

**Use DFS for:** Connected components, cycle detection, topological sort, flood fill

---

## 📝 Exercises

### Exercise 1 — Shortest Path (unweighted)
BFS from src to dst. Print distance or -1.

### Exercise 2 — Count Connected Components
How many separate components in the graph?

### Exercise 3 — Bipartite Check
Can graph be 2-colored? (NO odd cycles allowed)

### Exercise 4 — Cycle Detection
Does the undirected graph have a cycle?

### Exercise 5 — Flood Fill
Count cells reachable from (sr, sc) with same character in a grid.

---

## 🔗 Codeforces Practice
1. [B. Vasya and Chess](https://codeforces.com/problemset/problem/493/B)
2. [C. Kefa and Park](https://codeforces.com/problemset/problem/580/C) — tree BFS
3. [C. Tourist](https://codeforces.com/problemset/problem/58/E) — DFS
4. [B. Lena and Queries](https://codeforces.com/problemset/problem/360/E)
