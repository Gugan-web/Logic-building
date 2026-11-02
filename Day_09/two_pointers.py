"""
Day 09 — Two Pointers & Sliding Window
"""
import sys
from collections import defaultdict
input = sys.stdin.readline


def exercise1_two_sum_sorted():
    n, target = map(int, input().split())
    a = list(map(int, input().split()))
    idx = list(range(n))
    idx.sort(key=lambda i: a[i])  # sort indices by value

    lo, hi = 0, n - 1
    while lo < hi:
        s = a[idx[lo]] + a[idx[hi]]
        if s == target:
            i, j = sorted([idx[lo], idx[hi]])
            print(i, j)
            return
        elif s < target:
            lo += 1
        else:
            hi -= 1
    print(-1)


def exercise2_kadane():
    """Maximum subarray sum (Kadane's algorithm)"""
    n = int(input())
    a = list(map(int, input().split()))
    best = curr = a[0]
    for x in a[1:]:
        curr = max(x, curr + x)
        best = max(best, curr)
    print(best)


def exercise3_min_window_substring():
    """Minimum window substring containing all chars of t"""
    s = input().strip()
    t = input().strip()

    need = defaultdict(int)
    for c in t:
        need[c] += 1
    have = defaultdict(int)

    formed = 0
    required = len(need)
    lo = 0
    min_len = float('inf')
    result = ""

    for hi, c in enumerate(s):
        have[c] += 1
        if c in need and have[c] == need[c]:
            formed += 1
        while formed == required:
            if hi - lo + 1 < min_len:
                min_len = hi - lo + 1
                result = s[lo:hi+1]
            lc = s[lo]
            have[lc] -= 1
            if lc in need and have[lc] < need[lc]:
                formed -= 1
            lo += 1

    print(result if result else "")


def exercise4_longest_subarray_sum_k():
    """Longest subarray with sum <= k (non-negative array)"""
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    lo = 0
    window_sum = 0
    best = 0
    for hi in range(n):
        window_sum += a[hi]
        while window_sum > k:
            window_sum -= a[lo]
            lo += 1
        best = max(best, hi - lo + 1)
    print(best)


def exercise5_three_sum():
    """All unique triplets summing to 0"""
    n = int(input())
    a = sorted(map(int, input().split()))
    result = []
    for i in range(n - 2):
        if i > 0 and a[i] == a[i-1]:
            continue
        lo, hi = i + 1, n - 1
        while lo < hi:
            s = a[i] + a[lo] + a[hi]
            if s == 0:
                result.append((a[i], a[lo], a[hi]))
                while lo < hi and a[lo] == a[lo+1]: lo += 1
                while lo < hi and a[hi] == a[hi-1]: hi -= 1
                lo += 1; hi -= 1
            elif s < 0:
                lo += 1
            else:
                hi -= 1
    for t in result:
        print(*t)


def main():
    exercise2_kadane()


if __name__ == "__main__":
    main()
