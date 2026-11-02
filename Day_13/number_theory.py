"""
Day 13 — Number Theory (GCD, Primes, Sieve of Eratosthenes)
"""
import sys
from math import gcd, isqrt
input = sys.stdin.readline

MOD = 10**9 + 7


def lcm(a, b):
    return a // gcd(a, b) * b


def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, isqrt(n)+1, 2):
        if n % i == 0: return False
    return True


def sieve(n):
    """Sieve of Eratosthenes: returns list of primes up to n"""
    is_prime = bytearray([1]) * (n+1)
    is_prime[0] = is_prime[1] = 0
    for i in range(2, isqrt(n)+1):
        if is_prime[i]:
            is_prime[i*i::i] = bytearray(len(is_prime[i*i::i]))
    return [i for i in range(n+1) if is_prime[i]]


def smallest_prime_factor(n):
    """SPF sieve: spf[i] = smallest prime factor of i"""
    spf = list(range(n+1))
    for i in range(2, isqrt(n)+1):
        if spf[i] == i:  # i is prime
            for j in range(i*i, n+1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


def factorize(n, spf):
    """Fast factorization using SPF table"""
    factors = {}
    while n > 1:
        p = spf[n]
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
    return factors


def count_divisors(n):
    """Count divisors of n"""
    count = 0
    for i in range(1, isqrt(n)+1):
        if n % i == 0:
            count += 2 if i != n // i else 1
    return count


def euler_phi(n):
    """Euler's totient function: count of integers 1..n coprime to n"""
    result = n
    p = 2
    temp = n
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1
    if temp > 1:
        result -= result // temp
    return result


# ════════════════════════════════════════════════════
# EXERCISES
# ════════════════════════════════════════════════════

def exercise1_gcd_lcm():
    a, b = map(int, input().split())
    print(gcd(a, b), lcm(a, b))


def exercise2_prime_check():
    n = int(input())
    print("YES" if is_prime(n) else "NO")


def exercise3_sieve_count():
    n = int(input())
    primes = sieve(n)
    print(len(primes))


def exercise4_prime_factorization():
    n = int(input())
    temp = n
    factors = []
    for p in range(2, isqrt(n)+1):
        if temp % p == 0:
            exp = 0
            while temp % p == 0:
                exp += 1
                temp //= p
            factors.append(f"{p}^{exp}")
    if temp > 1:
        factors.append(str(temp))
    print(' * '.join(factors))


def exercise5_goldbach():
    """Verify Goldbach: every even n > 2 is sum of two primes"""
    n = int(input())
    primes = set(sieve(n))
    for p in range(2, n//2 + 1):
        if p in primes and (n - p) in primes:
            print(p, n - p)
            return


def main():
    exercise3_sieve_count()


if __name__ == "__main__":
    main()
