# Day 30 — Mock Contest + Full Practice Set

## 🎯 Goals
- Put together all 30 days of logic building, data structures, and algorithms into a real contest simulation
- Practice contest time management (2 hours, 5 problems from Div. 2/Div. 3 range)
- Master debugging under pressure and corner-case verification

---

## 🏆 Mock Contest Problem Set

| Problem | Title | Difficulty / Rating | Core Concepts |
|---|---|---|---|
| **A** | Divisibility Permutation | ~800 | Parity, Pigeonhole Principle, Constructive Algorithms |
| **B** | Balanced Subsegment XOR | ~1100 | Prefix XOR, Frequency Map, Two-Sum Analog |
| **C** | Factory Pipeline Capacity | ~1300 | Binary Search on Answer, Monotonicity Check |
| **D** | Network Reconstruction | ~1500 | Minimum Spanning Tree (MST), Kruskal's Algorithm, DSU |
| **E** | Maximum Score Tree Partition | ~1700 | Tree Dynamic Programming, Independent Set, Iterative DFS |

---

## ⏱️ Contest Simulation Strategy

1. **First 15 Minutes:**
   - Skim all problems A through C.
   - Solve Problem A immediately (constructive/math).
   - Check constraints on $N$ and test with boundary cases ($N=1, N=2, \text{odd/even}$).

2. **Minutes 15 to 45:**
   - Solve Problem B and Problem C.
   - If Problem C asks for "minimum possible maximum" or "minimum time to satisfy target", immediately test monotonicity for Binary Search on Answer.

3. **Minutes 45 to 90:**
   - Tackle Problem D (Graph / MST / DSU) or Problem E (Tree DP / Segment Tree).
   - Watch out for recursion depth in Python! Use `sys.setrecursionlimit(300000)` or write iterative DFS with a manual stack.

4. **Last 30 Minutes:**
   - Verify all corner cases:
     - Disconnected graphs ($M < N - 1$)
     - Modulo overflow ($10^9 + 7$)
     - $0$ or negative weights
     - Single element inputs ($N=1$)

---

## 🚀 Running the Mock Contest

Test your solutions against all built-in test suites:

```bash
python Day_30/mock_contest.py
```

---

## 🎓 Beyond Day 30: Next Steps

Congratulations on completing the 30-Day Logic Building Curriculum! You now possess the foundation to tackle Codeforces contests up to Candidate Master level.

### Next Roadmap:
1. **Participate Live:** Enter every Codeforces Div. 2, Div. 3, and Div. 4 round.
2. **Upsolve Without Fail:** Always solve at least one problem you couldn't solve during the contest within 24 hours of contest end.
3. **CSES Problem Set:** Complete the entire [CSES Problem Set](https://cses.fi/problemset/) (Dynamic Programming, Tree Algorithms, Graph Algorithms, Range Queries).
4. **PyRival & C++ Transition (Optional):** When $O(N \log^2 N)$ solutions in Python hit tight 1.0s time limits, keep C++ templates handy or use PyPy3 on Codeforces!
