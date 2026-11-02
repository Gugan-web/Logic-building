"""
Day 25 — Combinatorics & Modular Inverse
"""
import sys
from math import gcd, comb
input = sys.stdin.readline

MOD = 10**9 + 7


# ════════════════════════════════════════════════════
# PRECOMPUTE FACTORIALS — O(n) setup, O(1) per query
# ════════════════════════════════════════════════════
class Combinatorics:
    def __init__(self, maxn, mod=MOD):
        self.mod = mod
        self.fact   = [1] * (maxn + 1)
        self.inv_f  = [1] * (maxn + 1)
        for i in range(1, maxn + 1):
            self.fact[i] = self.fact[i-1] * i % mod
        self.inv_f[maxn] = pow(self.fact[maxn], mod - 2, mod)
        for i in range(maxn - 1, -1, -1):
            self.inv_f[i] = self.inv_f[i+1] * (i+1) % mod

    def nCr(self, n, r):
        if r < 0 or r > n: return 0
        return self.fact[n] * self.inv_f[r] % self.mod * self.inv_f[n-r] % self.mod

    def nPr(self, n, r):  # permutations
        if r < 0 or r > n: return 0
        return self.fact[n] * self.inv_f[n-r] % self.mod

    def catalan(self, n):  # C(2n, n) / (n+1)
        return self.nCr(2*n, n) * pow(n+1, self.mod-2, self.mod) % self.mod


# ════════════════════════════════════════════════════
# EXERCISES
# ════════════════════════════════════════════════════
C = Combinatorics(2 * 10**6)


def exercise1_ncr():
    """Compute C(n, r) mod MOD"""
    n, r = map(int, input().split())
    print(C.nCr(n, r))


def exercise2_stars_and_bars():
    """Ways to distribute n identical items into k distinct bins (with 0 allowed)
    = C(n + k - 1, k - 1)"""
    n, k = map(int, input().split())
    print(C.nCr(n + k - 1, k - 1))


def exercise3_paths_in_grid():
    """Count paths from (0,0) to (n,m) moving only right or down
    = C(n+m, n)"""
    n, m = map(int, input().split())
    print(C.nCr(n + m, n))


def exercise4_derangements():
    """Number of derangements of n elements (no fixed points)
    D(n) = (n-1)*(D(n-1) + D(n-2))"""
    n = int(input())
    if n == 0: print(1); return
    if n == 1: print(0); return
    d = [0] * (n + 1)
    d[1] = 0; d[2] = 1
    for i in range(3, n + 1):
        d[i] = (i - 1) * (d[i-1] + d[i-2]) % MOD
    print(d[n])


def exercise5_inclusion_exclusion():
    """At least 1 of k events using inclusion-exclusion
    |A1 ∪ A2 ∪ ... ∪ Ak| = sum of odd-sized intersections - even-sized"""
    # Example: count integers 1..n divisible by at least one prime in list p[]
    n, k = map(int, input().split())
    primes = list(map(int, input().split()))

    total = 0
    for mask in range(1, 1 << k):
        product = 1
        bits = 0
        for i in range(k):
            if mask >> i & 1:
                product *= primes[i]
                bits += 1
                if product > n: break
        if product <= n:
            if bits % 2 == 1:
                total += n // product
            else:
                total -= n // product
    print(total % MOD)


def exercise6_catalan():
    """n-th Catalan number: number of valid bracket sequences of length 2n"""
    n = int(input())
    print(C.catalan(n))


def main():
    exercise1_ncr()


if __name__ == "__main__":
    main()
