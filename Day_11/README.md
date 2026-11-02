# Day 11 — Recursion & Backtracking

## 🎯 Goals
- Understand recursion and the call stack
- Master the backtracking template
- Know when to increase recursion limit

---

## 🌀 Recursion in Python

Python's default recursion limit is **1000**. For DFS or recursive DP, always set:
```python
import sys
sys.setrecursionlimit(300000)
```

For very deep recursion (DFS on large graphs), use an **iterative** approach with an explicit stack to avoid stack overflow.

---

## 🔙 Backtracking Template

```python
def backtrack(state):
    if is_complete(state):
        save_solution(state)
        return
    for choice in get_choices(state):
        if is_valid(choice, state):
            apply(choice, state)     # make choice
            backtrack(state)         # recurse
            undo(choice, state)      # undo choice ← KEY STEP
```

**Pruning**: Add early `return` conditions to skip impossible branches. This is what separates fast backtracking from brute force.

---

## 📝 Exercises

### Exercise 1 — All Permutations
Generate all permutations of n numbers.

### Exercise 2 — N-Queens
Count ways to place N queens on N×N board with no attacks.
```
Input: 4    Output: 2
Input: 8    Output: 92
```

### Exercise 3 — Power Set (All Subsets)
Print all 2^n subsets of a given array.

### Exercise 4 — Generate Balanced Parentheses
Generate all valid parenthesis strings of length 2n.
```
Input: 3
Output: ((()))  (()())  (())()  ()(())  ()()()
```

### Exercise 5 — Subset Sum
Check if any subset of array sums to target.

---

## 🔗 Codeforces Practice
1. [A. Generate Parentheses](https://codeforces.com/problemset/problem/91/B)
2. [C. k-Rounding](https://codeforces.com/problemset/problem/858/C)
3. [B. Vasya and Socks](https://codeforces.com/problemset/problem/460/B)
