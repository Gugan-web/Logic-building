# Day 26 — Advanced Graphs: Topological Sort & SCC

## 🎯 Goals
- Implement topological sort (Kahn's + DFS)
- Find Strongly Connected Components with Kosaraju's
- Solve DP on DAGs

---

## ⬆️ Topological Sort

Only possible on **DAGs** (no cycles). Process nodes so all edges go forward.

**Kahn's (BFS):** Start from nodes with in-degree 0.

```python
queue = deque([u for u in range(1, n+1) if in_degree[u] == 0])
while queue:
    u = queue.popleft()
    order.append(u)
    for v in graph[u]:
        in_degree[v] -= 1
        if in_degree[v] == 0: queue.append(v)
```

If `len(order) < n` → **cycle exists**.

---

## 🔁 SCC — Strongly Connected Components

```
Kosaraju's: Two DFS passes
1. DFS on original graph → record finish order
2. DFS on reversed graph in reverse finish order → each DFS tree = one SCC
```

---

## 📝 Exercises

### Exercise 1 — Topological Sort
Print any valid ordering of n tasks with m prerequisites.

### Exercise 2 — Course Schedule
Can all n courses be completed given m prerequisites?

### Exercise 3 — Count SCCs
How many SCCs in the directed graph?

### Exercise 4 — Longest Path in DAG
```
Input:
5 5
1 2 / 1 3 / 3 4 / 2 4 / 4 5
Output: 3
```

---

## 🔗 Codeforces Practice
1. [B. Choosing Balls](https://codeforces.com/problemset/problem/402/D)
2. [D. Course Schedule](https://codeforces.com/problemset/problem/954/D)
3. [E. Inna and Binary Logic](https://codeforces.com/problemset/problem/390/E)
