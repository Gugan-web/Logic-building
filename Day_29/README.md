# Day 29 — Master Templates & Problem Patterns

## 🎯 Goals
- Have a unified, highly optimized reference library for competitive programming
- Instantly recall and copy-paste tested templates for Fast I/O, Math, Graph, Tree, and DP patterns
- Learn the rapid categorization pattern for Codeforces contests (Div. 2 / Div. 3)

---

## ⚡ Quick Pattern Cheatsheet

| Problem Characteristic | Primary Candidate Technique | Time Complexity |
|---|---|---|
| Range sum / point updates | Fenwick Tree (BIT) / Segment Tree | $O(\log n)$ per query |
| Range update + Range query | Lazy Segment Tree / Difference Array | $O(\log n)$ or $O(1) + O(n)$ |
| Dynamic connectivity / Cycle detection | Disjoint Set Union (DSU) | $O(\alpha(n))$ |
| Single source shortest path ($w_i \ge 0$) | Dijkstra with `heapq` | $O((V + E) \log V)$ |
| 0/1 edge weights shortest path | 0-1 BFS with `collections.deque` | $O(V + E)$ |
| Monotonic answer condition ("min of max") | Binary Search on Answer | $O(f(n) \cdot \log(\text{range}))$ |
| Subarray sum equals $K$ | Hash Map with Prefix Sums | $O(n)$ |
| Substring / Pattern matching | Z-algorithm / KMP / Rolling Hash | $O(n + m)$ |
| Tree LCA / Distance queries | Binary Lifting | $O(n \log n)$ precomputation, $O(\log n)$ query |
| Combinatorics with large modulo | Precomputed factorials + Fermat Inverse | $O(n)$ precomputation, $O(1)$ query |

---

## 📂 Included in `templates_patterns.py`

1. **Section 1: Fast I/O & Modulo Configuration**
   - High-performance input wrappers (`inp`, `inpl`, `inps`)
   - `sys.setrecursionlimit(300000)` safety
2. **Section 2: Number Theory & Modular Arithmetic**
   - Modular exponentiation & inverse via Fermat's Little Theorem
   - Extended Euclidean algorithm
   - Linear / Odd-only Sieve of Eratosthenes
   - Prime factorization in $O(\sqrt{n})$
3. **Section 3: Disjoint Set Union (DSU)**
   - Path compression and union-by-rank/size
4. **Section 4: Range Query Structures**
   - 1D Binary Indexed Tree (Fenwick)
   - Iterative / Recursive Segment Tree
5. **Section 5: Graph Traversals**
   - Breadth-First Search (BFS) & Depth-First Search (DFS)
   - Dijkstra's algorithm with priority queue
   - Kahn's algorithm for Topological Sort
6. **Section 6: Tree Utilities**
   - Tree Diameter via 2-BFS/DFS
   - LCA via Binary Lifting
7. **Section 7: String Algorithms**
   - Z-Algorithm & Prefix Function (KMP)

---

## 📝 Practice Exercises

### Exercise 1 — Contest Pre-check
Run `templates_patterns.py` under Python 3 and verify that all templates pass internal sanity assertions.

### Exercise 2 — Pattern Identification
Given a problem with $N \le 10^5$, queries asking for the median element in a growing multiset, which template from Day 29 would you adapt? (Two heaps / Fenwick tree with binary lifting).

---

## 🔗 Codeforces Recommended Contests
Use your template library to solve recent Div. 2 / Div. 3 contests:
1. [Codeforces Round 900 (Div. 3)](https://codeforces.com/contest/1878)
2. [Codeforces Round 910 (Div. 2)](https://codeforces.com/contest/1898)
3. [Educational Codeforces Round 160](https://codeforces.com/contest/1913)
