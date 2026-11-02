"""
Day 17 — DP: LCS, LIS & Edit Distance
"""
import sys
from bisect import bisect_left
input = sys.stdin.readline


# ════════════════════════════════════════════════════
# EXERCISE 1: LCS — Longest Common Subsequence O(n*m)
# ════════════════════════════════════════════════════
def exercise1_lcs():
    s = input().strip()
    t = input().strip()
    n, m = len(s), len(t)

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Reconstruct the LCS string
    lcs = []
    i, j = n, m
    while i > 0 and j > 0:
        if s[i-1] == t[j-1]:
            lcs.append(s[i-1])
            i -= 1; j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    print(dp[n][m], ''.join(reversed(lcs)))


# ════════════════════════════════════════════════════
# EXERCISE 2: LIS — Longest Increasing Subsequence
# O(n^2) DP and O(n log n) patience sorting
# ════════════════════════════════════════════════════
def exercise2_lis():
    n = int(input())
    a = list(map(int, input().split()))

    # O(n log n) using patience sorting (tails array)
    tails = []   # tails[i] = smallest tail of all IS of length i+1
    for x in a:
        pos = bisect_left(tails, x)   # first tail >= x
        if pos == len(tails):
            tails.append(x)
        else:
            tails[pos] = x

    print(len(tails))


# ════════════════════════════════════════════════════
# EXERCISE 3: Edit Distance (Levenshtein)
# ════════════════════════════════════════════════════
def exercise3_edit_distance():
    s = input().strip()
    t = input().strip()
    n, m = len(s), len(t)

    # Space-optimized: only need two rows
    prev = list(range(m + 1))
    for i in range(1, n + 1):
        curr = [i] + [0] * m
        for j in range(1, m + 1):
            if s[i-1] == t[j-1]:
                curr[j] = prev[j-1]
            else:
                curr[j] = 1 + min(prev[j],     # delete
                                  curr[j-1],    # insert
                                  prev[j-1])    # replace
        prev = curr

    print(prev[m])


# ════════════════════════════════════════════════════
# EXERCISE 4: LDS — Longest Decreasing Subsequence
# = LIS on reversed/negated array
# ════════════════════════════════════════════════════
def exercise4_lds():
    n = int(input())
    a = list(map(int, input().split()))
    # Negate and find LIS
    neg = [-x for x in a]
    tails = []
    for x in neg:
        pos = bisect_left(tails, x)
        if pos == len(tails): tails.append(x)
        else: tails[pos] = x
    print(len(tails))


# ════════════════════════════════════════════════════
# EXERCISE 5: Number of LIS (count all LIS)
# ════════════════════════════════════════════════════
def exercise5_count_lis():
    n = int(input())
    a = list(map(int, input().split()))

    length = [1] * n  # length of LIS ending at i
    count  = [1] * n  # count of LIS of that length ending at i

    for i in range(1, n):
        for j in range(i):
            if a[j] < a[i]:
                if length[j] + 1 > length[i]:
                    length[i] = length[j] + 1
                    count[i]  = count[j]
                elif length[j] + 1 == length[i]:
                    count[i] += count[j]

    max_len = max(length)
    total = sum(count[i] for i in range(n) if length[i] == max_len)
    print(max_len, total)


def main():
    exercise2_lis()


if __name__ == "__main__":
    main()
