"""
Day 15 — Dynamic Programming: Introduction
Top-down (lru_cache) and bottom-up (tabulation) patterns
"""
import sys
from functools import lru_cache
sys.setrecursionlimit(300000)
input = sys.stdin.readline

MOD = 10**9 + 7


# ════════════════════════════════════════════════════
# EXERCISE 1: Fibonacci mod MOD
# ════════════════════════════════════════════════════
def exercise1_fibonacci():
    n = int(input())
    if n <= 1:
        print(n)
        return
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, (a + b) % MOD
    print(b)


# ════════════════════════════════════════════════════
# EXERCISE 2: Climbing Stairs
# ════════════════════════════════════════════════════
def exercise2_climbing_stairs():
    n = int(input())

    # Top-down
    @lru_cache(maxsize=None)
    def ways(k):
        if k <= 1: return 1
        if k == 2: return 2
        return ways(k-1) + ways(k-2)

    print(ways(n))


# ════════════════════════════════════════════════════
# EXERCISE 3: Coin Change — Minimum Coins
# ════════════════════════════════════════════════════
def exercise3_coin_change():
    m, amount = map(int, input().split())
    coins = list(map(int, input().split()))

    # Bottom-up tabulation
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            if c <= a and dp[a - c] + 1 < dp[a]:
                dp[a] = dp[a - c] + 1

    print(dp[amount] if dp[amount] != float('inf') else -1)


# ════════════════════════════════════════════════════
# EXERCISE 4: Longest Common Subsequence (LCS)
# ════════════════════════════════════════════════════
def exercise4_lcs():
    s1 = input().strip()
    s2 = input().strip()
    n, m = len(s1), len(s2)

    # Bottom-up 2D DP
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print(dp[n][m])


# ════════════════════════════════════════════════════
# EXERCISE 5: Maximum Subarray (Kadane as DP)
# ════════════════════════════════════════════════════
def exercise5_max_subarray():
    n = int(input())
    a = list(map(int, input().split()))

    # dp[i] = max subarray sum ending at index i
    dp = a[0]
    best = a[0]
    for x in a[1:]:
        dp = max(x, dp + x)
        best = max(best, dp)
    print(best)


# ════════════════════════════════════════════════════
# EXERCISE 6: House Robber
# ════════════════════════════════════════════════════
def exercise6_house_robber():
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(a[0])
        return

    prev2, prev1 = 0, 0
    for x in a:
        curr = max(prev1, prev2 + x)
        prev2, prev1 = prev1, curr
    print(prev1)


def main():
    exercise3_coin_change()


if __name__ == "__main__":
    main()
