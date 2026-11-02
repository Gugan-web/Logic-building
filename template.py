"""
================================================================
  MASTER PYTHON COMPETITIVE PROGRAMMING TEMPLATE
  For Codeforces / ICPC / Competitive Programming
================================================================
"""

import sys
import os
from math import gcd, lcm, isqrt, log2, ceil, floor, comb, factorial
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate, product
from bisect import bisect_left, bisect_right, insort
from heapq import heappush, heappop, heapify, nlargest, nsmallest
from functools import lru_cache, reduce
import threading

# ─── Fast Input ──────────────────────────────────────────────
input = sys.stdin.readline          # 5-10x faster than built-in input()
# For even faster: read all at once
# data = sys.stdin.read().split()
# idx = 0
# def rd(): global idx; idx += 1; return data[idx-1]

def inp():    return int(input())
def inpl():   return list(map(int, input().split()))
def inps():   return input().strip()
def inpsl():  return input().split()

# ─── Constants ───────────────────────────────────────────────
MOD  = 10**9 + 7
MOD2 = 998244353
INF  = float('inf')
PI   = 3.141592653589793

# ─── Fast Output ─────────────────────────────────────────────
out = sys.stdout.write              # faster than print()
# Usage: out(str(answer) + '\n')
# Or collect all answers in a list and print at end:
# print('\n'.join(map(str, answers)))

# ─── Math Utilities ──────────────────────────────────────────
def power(base, exp, mod=MOD):
    """Fast modular exponentiation: base^exp % mod"""
    return pow(base, exp, mod)          # Python built-in is already fast!

def modinv(a, m=MOD):
    """Modular inverse using Fermat's little theorem (m must be prime)"""
    return pow(a, m - 2, m)

def modinv_ext(a, m):
    """Modular inverse using extended Euclidean (works for any m)"""
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        return -1  # no inverse
    return x % m

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x, y = extended_gcd(b % a, a)
    return g, y - (b // a) * x, x

# ─── Sieve of Eratosthenes ───────────────────────────────────
def sieve(n):
    """Return list of booleans: is_prime[i] = True if i is prime"""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, isqrt(n) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return is_prime

# ─── Recursion Limit (for DFS/recursive DP) ──────────────────
sys.setrecursionlimit(300000)

# ─── Graph Utilities ─────────────────────────────────────────
def make_graph(n, edges, directed=False):
    """Build adjacency list from edge list"""
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)
        if not directed:
            g[v].append(u)
    return g

# ─── DSU (Union-Find) ────────────────────────────────────────
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank   = [0] * n
        self.size   = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # path compression
            x = self.parent[x]
        return x

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return False
        if self.rank[px] < self.rank[py]: px, py = py, px
        self.parent[py] = px
        self.size[px] += self.size[py]
        if self.rank[px] == self.rank[py]: self.rank[px] += 1
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return self.size[self.find(x)]

# ─── Segment Tree (point update, range query) ────────────────
class SegTree:
    def __init__(self, n, func=max, default=0):
        self.n    = n
        self.func = func
        self.default = default
        self.tree = [default] * (2 * n)

    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i >>= 1
            self.tree[i] = self.func(self.tree[2*i], self.tree[2*i+1])

    def query(self, l, r):  # [l, r)
        res = self.default
        l += self.n; r += self.n
        while l < r:
            if l & 1: res = self.func(res, self.tree[l]); l += 1
            if r & 1: r -= 1; res = self.func(res, self.tree[r])
            l >>= 1; r >>= 1
        return res

# ─── Precompute Factorials (for combinatorics) ───────────────
def precompute_factorials(n, mod=MOD):
    fact   = [1] * (n + 1)
    inv_f  = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i-1] * i % mod
    inv_f[n] = pow(fact[n], mod - 2, mod)
    for i in range(n - 1, -1, -1):
        inv_f[i] = inv_f[i+1] * (i+1) % mod
    def nCr(n, r):
        if r < 0 or r > n: return 0
        return fact[n] * inv_f[r] % mod * inv_f[n-r] % mod
    return fact, inv_f, nCr

# ─── Main Solve Function ─────────────────────────────────────
def solve():
    # Write your solution here
    pass

# ─── Entry Point ─────────────────────────────────────────────
def main():
    t = 1
    # t = inp()   # uncomment for multiple test cases
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()

# ─── For deep recursion (DFS on large graphs) ────────────────
# threading.stack_size(1 << 27)  # 128 MB stack
# thread = threading.Thread(target=main)
# thread.start()
