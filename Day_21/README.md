# Day 21 — Trees & Binary Trees

## 🎯 Goals
- Represent and traverse trees (BFS/DFS)
- Compute diameter, height, subtree sizes
- Implement LCA with binary lifting O(log n) per query

---

## 🌳 Tree Key Facts
- A tree with n nodes has exactly n-1 edges
- There is exactly one path between any two nodes
- Rooted at node 1 by convention

---

## 📐 Tree Diameter — Two BFS Trick
1. BFS from any node → find farthest node `u`
2. BFS from `u` → distance to farthest node = **diameter**

---

## 👆 LCA with Binary Lifting
- Precompute `up[k][v]` = 2^k-th ancestor of v
- Build in O(n log n), answer each LCA query in O(log n)

---

## 📝 Exercises

### Exercise 1 — Tree Diameter
```
Input:  5 / edges: 1-2 1-3 3-4 4-5
Output: 3
```

### Exercise 2 — Tree Height
Maximum depth from root (node 1).

### Exercise 3 — Subtree Sizes
For each node, count number of nodes in its subtree.

### Exercise 4 — LCA
Answer q queries: LCA(u, v).

### Exercise 5 — Distance Between Nodes
`dist(u, v) = depth[u] + depth[v] - 2*depth[LCA(u,v)]`

---

## 🔗 Codeforces Practice
1. [C. Kefa and Park](https://codeforces.com/problemset/problem/580/C)
2. [D. Distance in Tree](https://codeforces.com/problemset/problem/161/D)
3. [E. LCA](https://codeforces.com/problemset/problem/236/D)
