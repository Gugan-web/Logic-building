# Day 28 — Game Theory: Nim & Sprague-Grundy

## 🎯 Goals
- Solve Nim and its variants using XOR
- Understand the Sprague-Grundy theorem
- Compute Grundy values with mex

---

## 🎮 Nim — The Foundation

**Rule:** Players alternate taking any positive number from one pile. Last to move wins.

**Winning condition:** First player wins iff `XOR of all pile sizes ≠ 0`

```python
xor = pile[0] ^ pile[1] ^ pile[2] ^ ...
print("First" if xor != 0 else "Second")
```

---

## 🔢 Sprague-Grundy Theorem

Every impartial game position has a **Grundy number** (nimber):

```
Grundy(pos) = mex({Grundy(next) for all moves from pos})
mex = Minimum EXcludant = smallest non-negative integer not in set
```

For combined games: **XOR of individual Grundy numbers** determines the winner.

---

## 📝 Exercises

### Exercise 1 — Basic Nim
```
Input:  3 / 3 4 5
Output: First   (XOR = 3^4^5 = 2 ≠ 0)
```

### Exercise 2 — Nim with Move Restrictions
Can only take 1, 2, or 3 per turn. Use Grundy values.

### Exercise 3 — Staircase Nim
Piles on stairs. Only XOR of **odd-indexed** stairs matters.

### Exercise 4 — Coin Row Game
Pick coins from row ends optimally (not strictly Nim — use DP).

---

## 🔗 Codeforces Practice
1. [C. Euclid's Game](https://codeforces.com/problemset/problem/7/C)
2. [D. Nim and Queries](https://codeforces.com/problemset/problem/768/E)
3. [B. Game with Sticks](https://codeforces.com/problemset/problem/451/B)
4. [C. Alice and the Cake](https://codeforces.com/problemset/problem/916/C)
