"""
Day 03 — Loops, Conditions & Basic Math
"""
import sys
from math import isqrt
input = sys.stdin.readline

MOD = 10**9 + 7


# ════════════════════════════════════════════════════
# CONCEPT: Loop Patterns
# ════════════════════════════════════════════════════

def loop_patterns():
    n = 10
    # Standard range
    for i in range(n):           print(i, end=' ')    # 0..9

    # Step loop (even numbers)
    for i in range(0, n, 2):    print(i, end=' ')    # 0,2,4,6,8

    # Reverse loop
    for i in range(n-1, -1, -1): print(i, end=' ')   # 9..0

    # Enumerate (index + value)
    a = [10, 20, 30]
    for i, v in enumerate(a):   print(i, v)

    # Zip (two lists together)
    b = [1, 2, 3]
    for x, y in zip(a, b):      print(x + y)

    # While loop
    while n > 1:
        n //= 2


# ════════════════════════════════════════════════════
# MATH TRICKS
# ════════════════════════════════════════════════════

def ceil_div(a, b):
    """Ceiling division without float: ceil(a/b)"""
    return (a + b - 1) // b

def digit_sum(n):
    """Sum of digits of n"""
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

def digit_sum_fast(n):
    """Using string conversion (simpler but slightly slower)"""
    return sum(int(c) for c in str(n))

def count_digits(n):
    """Number of digits in n"""
    if n == 0: return 1
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

def reverse_number(n):
    """Reverse digits of n"""
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev

def is_perfect_square(n):
    """Check if n is a perfect square (no float errors!)"""
    r = isqrt(n)
    return r * r == n

def trailing_zeros_factorial(n):
    """Count trailing zeros in n! = count factors of 5"""
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count

def is_prime_simple(n):
    """Check primality in O(sqrt(n))"""
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0: return False
    return True


# ════════════════════════════════════════════════════
# EXERCISES
# ════════════════════════════════════════════════════

def exercise_fizzbuzz():
    n = int(input())
    for i in range(1, n + 1):
        if i % 15 == 0:     print("FizzBuzz")
        elif i % 3 == 0:    print("Fizz")
        elif i % 5 == 0:    print("Buzz")
        else:               print(i)


def exercise_trailing_zeros():
    """Count trailing zeros in n!"""
    n = int(input())
    print(trailing_zeros_factorial(n))


def exercise_digit_sum():
    """Sum of digits of n^2"""
    n = int(input())
    print(digit_sum(n * n))


def exercise_count_divisible():
    """Count integers 1..n divisible by 2, 3, or 5 (inclusion-exclusion)"""
    n = int(input())
    a = n // 2
    b = n // 3
    c = n // 5
    ab = n // 6
    ac = n // 10
    bc = n // 15
    abc = n // 30
    print(a + b + c - ab - ac - bc + abc)


def exercise_collatz():
    """Count steps for Collatz sequence to reach 1"""
    n = int(input())
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    print(steps)


def main():
    exercise_trailing_zeros()


if __name__ == "__main__":
    main()
