"""
Day 16 — DP: 0/1 Knapsack & Variants
"""
import sys
input = sys.stdin.readline


# ════════════════════════════════════════════════════
# EXERCISE 1: Classic 0/1 Knapsack (1D optimized)
# ════════════════════════════════════════════════════
def exercise1_knapsack():
    n, W = map(int, input().split())
    weight = []
    value = []
    for _ in range(n):
        w, v = map(int, input().split())
        weight.append(w)
        value.append(v)

    dp = [0] * (W + 1)
    for i in range(n):
        # Reverse to ensure each item used at most once
        for w in range(W, weight[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weight[i]] + value[i])

    print(dp[W])


# ════════════════════════════════════════════════════
# EXERCISE 2: Count Subsets with Sum K
# ════════════════════════════════════════════════════
def exercise2_count_subsets():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    MOD = 10**9 + 7
    dp = [0] * (k + 1)
    dp[0] = 1  # empty subset sums to 0

    for x in a:
        for s in range(k, x - 1, -1):  # reverse!
            dp[s] = (dp[s] + dp[s - x]) % MOD

    print(dp[k])


# ════════════════════════════════════════════════════
# EXERCISE 3: Partition Equal Subset Sum
# ════════════════════════════════════════════════════
def exercise3_partition():
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)

    if total % 2 != 0:
        print("NO")
        return

    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for x in a:
        for s in range(target, x - 1, -1):
            dp[s] = dp[s] or dp[s - x]

    print("YES" if dp[target] else "NO")


# ════════════════════════════════════════════════════
# EXERCISE 4: Unbounded Coin Change — Count Ways
# ════════════════════════════════════════════════════
def exercise4_unbounded_ways():
    m, amount = map(int, input().split())
    coins = list(map(int, input().split()))

    MOD = 10**9 + 7
    dp = [0] * (amount + 1)
    dp[0] = 1  # 1 way to make 0

    for coin in coins:
        for a in range(coin, amount + 1):   # FORWARD for unbounded
            dp[a] = (dp[a] + dp[a - coin]) % MOD

    print(dp[amount])


# ════════════════════════════════════════════════════
# EXERCISE 5: Minimum Subset Sum Difference
# ════════════════════════════════════════════════════
def exercise5_min_diff():
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    half = total // 2

    dp = [False] * (half + 1)
    dp[0] = True

    for x in a:
        for s in range(half, x - 1, -1):
            dp[s] = dp[s] or dp[s - x]

    # Find the largest achievable sum <= total/2
    for s in range(half, -1, -1):
        if dp[s]:
            print(total - 2 * s)
            return


def main():
    exercise3_partition()


if __name__ == "__main__":
    main()
