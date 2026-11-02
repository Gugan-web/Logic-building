"""
Day 14 — Bit Manipulation
"""
import sys
input = sys.stdin.readline


# ─── Bit Tricks Reference ────────────────────────────────────
# n & 1          → last bit (1 if odd, 0 if even)
# n >> 1         → divide by 2 (right shift)
# n << 1         → multiply by 2 (left shift)
# n & (n-1)      → clear lowest set bit
# n & (-n)       → isolate lowest set bit
# n | (1 << k)   → set bit k
# n & ~(1 << k)  → clear bit k
# n ^ (1 << k)   → toggle bit k
# n >> k & 1     → check bit k
# bin(n).count('1')  → popcount (number of set bits)


def is_odd(n):             return bool(n & 1)
def is_power_of_2(n):      return n > 0 and (n & (n - 1)) == 0
def set_bit(n, k):         return n | (1 << k)
def clear_bit(n, k):       return n & ~(1 << k)
def toggle_bit(n, k):      return n ^ (1 << k)
def check_bit(n, k):       return bool(n >> k & 1)
def lowest_set_bit(n):     return n & (-n)
def count_set_bits(n):     return bin(n).count('1')
def next_power_of_2(n):    n -= 1; n |= n>>1; n |= n>>2; n |= n>>4; n |= n>>8; n |= n>>16; return n+1


# ════════════════════════════════════════════════════
# EXERCISE 1: Count set bits (popcount)
# ════════════════════════════════════════════════════
def exercise1_popcount():
    n = int(input())
    print(bin(n).count('1'))


# ════════════════════════════════════════════════════
# EXERCISE 2: Check if power of 2
# ════════════════════════════════════════════════════
def exercise2_power_of_2():
    n = int(input())
    print("YES" if is_power_of_2(n) else "NO")


# ════════════════════════════════════════════════════
# EXERCISE 3: XOR from 1 to n (pattern-based)
# ════════════════════════════════════════════════════
def xor_1_to_n(n):
    if n % 4 == 0:   return n
    if n % 4 == 1:   return 1
    if n % 4 == 2:   return n + 1
    if n % 4 == 3:   return 0

def exercise3_xor():
    n = int(input())
    print(xor_1_to_n(n))


# ════════════════════════════════════════════════════
# EXERCISE 4: All Subsets using Bitmask
# ════════════════════════════════════════════════════
def exercise4_bitmask_subsets():
    n = int(input())
    a = list(map(int, input().split()))
    for mask in range(1 << n):
        subset = [a[i] for i in range(n) if mask >> i & 1]
        print(*subset)


# ════════════════════════════════════════════════════
# EXERCISE 5: Single Number (find element appearing once)
# ════════════════════════════════════════════════════
def exercise5_single_number():
    """XOR of array — duplicates cancel out, leaving the single element"""
    n = int(input())
    a = list(map(int, input().split()))
    result = 0
    for x in a:
        result ^= x
    print(result)


# ════════════════════════════════════════════════════
# EXERCISE 6: Two non-repeating numbers
# ════════════════════════════════════════════════════
def exercise6_two_singles():
    n = int(input())
    a = list(map(int, input().split()))
    xor = 0
    for x in a: xor ^= x    # xor = a XOR b (the two singles)

    # Find any set bit in xor (the two numbers differ here)
    bit = xor & (-xor)       # lowest set bit

    a_val = b_val = 0
    for x in a:
        if x & bit: a_val ^= x
        else:       b_val ^= x

    print(min(a_val, b_val), max(a_val, b_val))


def main():
    exercise5_single_number()


if __name__ == "__main__":
    main()
