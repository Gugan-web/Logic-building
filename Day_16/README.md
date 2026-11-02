# Day 16 — DP: 0/1 Knapsack & Variants

## 🎯 Goals
- Master the 0/1 knapsack DP
- Understand space optimization (2D → 1D)
- Solve knapsack variants (unbounded, count, partition)

---

## 🎒 0/1 Knapsack

**Problem:** n items, each with weight w[i] and value v[i]. Capacity W. Maximize value.

### 2D DP — O(n × W) time, O(n × W) space
```python
dp = [[0]*(W+1) for _ in range(n+1)]
for i in range(1, n+1):
    for w in range(W+1):
        dp[i][w] = dp[i-1][w]          # skip item i
        if w >= weight[i-1]:
            dp[i][w] = max(dp[i][w],
                           dp[i-1][w - weight[i-1]] + value[i-1])  # take item i
answer = dp[n][W]
```

### 1D DP — O(W) space (MUST iterate w in reverse!)
```python
dp = [0] * (W + 1)
for i in range(n):
    for w in range(W, weight[i]-1, -1):   # REVERSE to avoid using item twice
        dp[w] = max(dp[w], dp[w - weight[i]] + value[i])
answer = dp[W]
```

---

## ♾️ Unbounded Knapsack (items can be reused)

```python
dp = [0] * (W + 1)
for w in range(1, W+1):
    for i in range(n):
        if weight[i] <= w:
            dp[w] = max(dp[w], dp[w - weight[i]] + value[i])
# Or: for each item, iterate w FORWARD (not reverse)
```

---

## 📝 Exercises

### Exercise 1 — Classic 0/1 Knapsack
```
Input:
4 10          ← n items, capacity W
1 1           ← weight value
3 4
4 5
5 7

Output: 13    (items 2+3+4 → 3+4+5=12 weight, 4+5+7=16? recalc)
```

### Exercise 2 — Count Subsets with Sum K
Count subsets of array with sum exactly K.

### Exercise 3 — Partition Equal Subset Sum
Can you partition array into two equal-sum subsets?
```
Input:  4 / 1 5 11 5
Output: YES   (1+5+5=11)
```

### Exercise 4 — Unbounded Coin Change (Count Ways)
Count number of ways to make amount n using unlimited coins.

### Exercise 5 — Minimum Subset Sum Difference
Partition array into two subsets to minimize |sum1 - sum2|.

---

## 🔗 Codeforces Practice
1. [C. Codeforces Round 495](https://codeforces.com/problemset/problem/1003/D)
2. [D. Petya and Array](https://codeforces.com/problemset/problem/1081/C)
3. [C. Gregor and the Two Painters](https://codeforces.com/problemset/problem/1548/C)
