# Day 18 — DP: Grid & 2D Problems

## 🎯 Goals
- Solve grid traversal problems with DP
- Master directional DP patterns (right/down, all 4/8 directions)
- Apply DP on triangles and 2D shapes

---

## 🗺️ Grid DP Pattern

```
State:   dp[i][j] = best answer to reach cell (i,j)
Base:    dp[0][0] = grid[0][0]
Transition (can only go right/down):
    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
Answer:  dp[n-1][m-1]
```

---

## 📝 Exercises

### Exercise 1 — Unique Paths
Count distinct paths from (0,0) to (n-1,m-1) moving only right or down.
```
Input:  3 7     Output: 28
```

### Exercise 2 — Minimum Cost Path
Find path with minimum sum from top-left to bottom-right.

### Exercise 3 — Pascal's Triangle Path
Min sum path from top to bottom in a triangle (each step goes to adjacent below).
```
Input:
3
2
3 4
6 5 7

Output: 10
```

### Exercise 4 — Maximal Square
Find largest square of '1's in a binary grid. Output its area.

### Exercise 5 — Dungeon Game
Minimum starting health to survive dungeon (rooms with positive/negative HP).

---

## 🔗 Codeforces Practice
1. [A. Ilya and Matrix](https://codeforces.com/problemset/problem/313/B)
2. [C. Vasya and Grid](https://codeforces.com/problemset/problem/1051/E)
3. [D. Grid Game](https://codeforces.com/problemset/problem/1039/D)
