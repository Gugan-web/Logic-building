# Day 12 — Greedy Algorithms

## 🎯 Goals
- Understand the greedy paradigm
- Recognize greedy problems vs DP problems
- Master common greedy patterns

---

## 🤑 What is Greedy?

A greedy algorithm makes the **locally optimal choice at each step**, hoping it leads to the global optimum.

**Key question:** Can I prove that picking the best choice NOW never makes things worse later?

### Greedy vs DP
| | Greedy | Dynamic Programming |
|-|--------|---------------------|
| Choices | One optimal per step | Explores all options |
| Speed | O(n) or O(n log n) | Usually O(n²) or more |
| Proof needed | Yes! | No |
| When | Overlapping optimal substructure with exchange argument | When greedy fails |

---

## 🔑 Common Greedy Patterns

### 1. Sort + Greedy
```python
# Activity selection: maximize non-overlapping intervals
intervals.sort(key=lambda x: x[1])  # sort by end time
count, last_end = 0, -inf
for start, end in intervals:
    if start >= last_end:
        count += 1
        last_end = end
```

### 2. Two Heaps
```python
# Assign tasks optimally
```

### 3. Greedy on strings
```python
# Always process the most urgent character first
```

---

## 📝 Exercises

### Exercise 1 — Coin Change (Greedy version)
With coins [1, 5, 10, 25], find minimum coins for amount n. (Works because denominations are multiples!)

### Exercise 2 — Activity Selection
Maximum number of non-overlapping intervals.
```
Input:
3
1 3
2 4
3 5

Output: 2
```

### Exercise 3 — Minimum Platforms
Minimum train platforms needed (interval scheduling).

### Exercise 4 — Jump Game
Given array where a[i] = max jump from i, can you reach end?

### Exercise 5 — Fractional Knapsack
Maximize value given weight capacity (items can be split).

---

## 🔗 Codeforces Practice
1. [A. Vasya the Hipster](https://codeforces.com/problemset/problem/493/A)
2. [B. Mahmoud and Ehab and the Backpack](https://codeforces.com/problemset/problem/862/B)
3. [C. Mike and Chocolate Thieves](https://codeforces.com/problemset/problem/689/C)
4. [B. Arpa and a game with Mojtaba](https://codeforces.com/problemset/problem/850/B)
