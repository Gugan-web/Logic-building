# Day 20 — Shortest Path: Dijkstra & BFS Variants

## 🎯 Goals
- Implement Dijkstra's algorithm for weighted graphs
- Use 0-1 BFS for edge weights of 0 or 1
- Apply multi-source BFS

---

## ⚡ Dijkstra's Algorithm

**Works for:** non-negative edge weights  
**Complexity:** O((V + E) log V)

```python
import heapq

def dijkstra(graph, src, n):
    dist = [float('inf')] * (n+1)
    dist[src] = 0
    heap = [(0, src)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]: continue      # outdated
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist
```

---

## 🎰 Algorithm Selection Guide

| Weights | Algorithm | Complexity |
|---------|-----------|------------|
| Unweighted | BFS | O(V+E) |
| 0 or 1 | 0-1 BFS (deque) | O(V+E) |
| Non-negative | Dijkstra | O((V+E) log V) |
| Any (no neg cycle) | Bellman-Ford | O(VE) |
| All pairs | Floyd-Warshall | O(V³) |

---

## 📝 Exercises

### Exercise 1 — SSSP with Dijkstra
Print shortest distances from source to all nodes.

### Exercise 2 — Path Cost
Minimum cost path between two specific nodes.

### Exercise 3 — Multi-Source BFS
Shortest distance from any of k given source nodes to all others.

### Exercise 4 — Path Reconstruction
Print the actual shortest path (not just the distance).

---

## 🔗 Codeforces Practice
1. [E. Dijkstra?](https://codeforces.com/problemset/problem/20/C) — classic Dijkstra
2. [D. Roads not only in Berland](https://codeforces.com/problemset/problem/196/E)
3. [C. Berland Subway](https://codeforces.com/problemset/problem/884/E)
4. [D. Greg and Graph](https://codeforces.com/problemset/problem/295/B)
