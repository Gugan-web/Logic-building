"""
Day 02 — Data Types, Overflow & Modular Arithmetic
Python has no overflow — but we still need modular arithmetic!
"""

import sys
from math import gcd, lcm, isqrt, comb
input = sys.stdin.readline

MOD = 10**9 + 7


# ─── Modular Arithmetic Helpers ──────────────────────────────

def modinv(a, mod=MOD):
    """Modular inverse using Fermat's little theorem (mod must be prime)"""
    return pow(a, mod - 2, mod)


def ext_gcd(a, b):
    """Extended Euclidean: returns (gcd, x, y) such that a*x + b*y = gcd"""
    if a == 0:
        return b, 0, 1
    g, x, y = ext_gcd(b % a, a)
    return g, y - (b // a) * x, x


def modinv_general(a, m):
    """Modular inverse using extended GCD (works when m is not prime)"""
    g, x, _ = ext_gcd(a, m)
    if g != 1:
        return -1  # inverse doesn't exist
    return x % m


# ════════════════════════════════════════════════════
# EXERCISE 1: a^b mod MOD
# ════════════════════════════════════════════════════
def exercise1():
    a, b = map(int, input().split())
    print(pow(a, b, MOD))


# ════════════════════════════════════════════════════
# EXERCISE 2: Fibonacci(n) mod MOD
# ════════════════════════════════════════════════════
def exercise2():
    n = int(input())
    if n <= 1:
        print(n)
        return
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, (a + b) % MOD
    print(b)


# ════════════════════════════════════════════════════
# EXERCISE 3: Modular Division (a / b) mod MOD
# ════════════════════════════════════════════════════
def exercise3():
    a, b = map(int, input().split())
    # Division in modular arithmetic = multiply by inverse
    result = a * modinv(b) % MOD
    print(result)


# ════════════════════════════════════════════════════
# EXERCISE 4: Sum of 1^k + 2^k + ... + n^k mod MOD
# ════════════════════════════════════════════════════
def exercise4():
    n, k = map(int, input().split())
    total = 0
    for i in range(1, n + 1):
        total = (total + pow(i, k, MOD)) % MOD
    print(total)


# ─── Demos ───────────────────────────────────────────────────

def demo_no_overflow():
    """Python integers grow arbitrarily large"""
    x = 10 ** 1000
    print(f"10^1000 has {len(str(x))} digits")  # 1001 digits
    print("Last 10 digits:", x % (10**10))


def demo_modular_arithmetic():
    a, b = 10**9, 10**9
    # Safe multiplication with modular arithmetic
    product = a * b % MOD        # Python doesn't overflow: just slower
    print(f"10^9 * 10^9 mod MOD = {product}")

    # Subtraction (watch for negatives!)
    diff = (a - b + MOD) % MOD   # Always add MOD before taking mod
    print(f"Subtraction result: {diff}")


def demo_math_functions():
    print(gcd(48, 18))           # 6
    print(lcm(4, 6))             # 12
    print(isqrt(17))             # 4 (integer square root)
    print(comb(10, 3))           # 120


def main():
    # demo_no_overflow()
    # demo_modular_arithmetic()
    # demo_math_functions()
    exercise1()


if __name__ == "__main__":
    main()
