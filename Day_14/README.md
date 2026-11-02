# Day 14 — Bit Manipulation

## 🎯 Goals
- Understand binary representation and bit operations
- Master common bit tricks used in competitive programming
- Use bitmasks for subset enumeration

---

## 🔬 Bit Operations Cheat Sheet

| Operation | Python | Result |
|-----------|--------|--------|
| AND | `a & b` | 1 only if both bits are 1 |
| OR | `a \| b` | 1 if either bit is 1 |
| XOR | `a ^ b` | 1 if bits differ |
| NOT | `~a` | flip all bits |
| Left shift | `a << k` | multiply by 2^k |
| Right shift | `a >> k` | divide by 2^k (floor) |

---

## 🔥 Essential Bit Tricks

```python
n & 1                # check if odd
n >> k & 1           # check if bit k is set
n | (1 << k)         # set bit k
n & ~(1 << k)        # clear bit k
n ^ (1 << k)         # toggle bit k
n & (n - 1)          # clear lowest set bit → 0 if power of 2
n & (-n)             # isolate lowest set bit
bin(n).count('1')    # count set bits (popcount)
```

### XOR Properties
```
a ^ a = 0     # same values cancel
a ^ 0 = a     # XOR with 0 = no change
XOR is commutative and associative
```

---

## 🗂️ Bitmask DP / Subset Enumeration

```python
n = 4
# Enumerate all 2^n subsets
for mask in range(1 << n):
    # Check if element i is in this subset
    subset = [i for i in range(n) if mask >> i & 1]

# Enumerate all subsets of a given mask
sub = mask
while sub > 0:
    # process sub
    sub = (sub - 1) & mask
```

---

## 📝 Exercises

### Exercise 1 — Count Set Bits
Count the number of 1 bits in n.
```
Input: 13    Output: 3    (1101 → three 1s)
```

### Exercise 2 — Power of 2 Check
```
Input: 16    Output: YES
Input: 15    Output: NO
```

### Exercise 3 — XOR of 1 to N
XOR of all integers from 1 to n (without a loop — O(1) formula).

### Exercise 4 — All Subsets via Bitmask
Print all subsets of array a.

### Exercise 5 — Single Number
Array where all numbers appear twice except one. Find the single one.
```
Input: 5 / 4 1 2 1 2    Output: 4
```

### Exercise 6 — Two Non-Repeating Numbers
Array where all appear twice except two. Find both.

---

## 🔗 Codeforces Practice
1. [A. Xor-sequences](https://codeforces.com/problemset/problem/374/A)
2. [B. Maximum XOR Secondary](https://codeforces.com/problemset/problem/281/D)
3. [C. Kefa and Dishes](https://codeforces.com/problemset/problem/580/D) — bitmask DP
4. [B. AND Segment](https://codeforces.com/problemset/problem/1515/F)
