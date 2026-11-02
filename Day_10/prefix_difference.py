"""
Day 10 — Prefix Sums & Difference Arrays
"""
import sys
from itertools import accumulate
from collections import defaultdict
input = sys.stdin.readline


def exercise1_range_sum():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    prefix = [0] + list(accumulate(a))

    out = []
    for _ in range(q):
        l, r = map(int, input().split())
        out.append(str(prefix[r+1] - prefix[l]))
    print('\n'.join(out))


def exercise2_subarray_sum_k():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = defaultdict(int)
    cnt[0] = 1
    prefix = 0
    answer = 0
    for x in a:
        prefix += x
        answer += cnt[prefix - k]
        cnt[prefix] += 1
    print(answer)


def exercise3_range_add_point_query():
    n, m = map(int, input().split())
    diff = [0] * (n + 2)

    for _ in range(m):
        line = input().split()
        if line[0] == 'A':   # Add v to [l, r]
            l, r, v = int(line[1]), int(line[2]), int(line[3])
            diff[l] += v
            diff[r+1] -= v
        else:                 # Query index i
            i = int(line[1])
            print(sum(diff[:i+1]))


def exercise4_2d_prefix():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    ps = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            ps[i][j] = a[i-1][j-1] + ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1]

    def query(r1, c1, r2, c2):
        return ps[r2+1][c2+1] - ps[r1][c2+1] - ps[r2+1][c1] + ps[r1][c1]

    q = int(input())
    out = []
    for _ in range(q):
        r1, c1, r2, c2 = map(int, input().split())
        out.append(str(query(r1, c1, r2, c2)))
    print('\n'.join(out))


def exercise5_equilibrium_index():
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    left = 0
    for i in range(n):
        right = total - left - a[i]
        if left == right:
            print(i)
            return
        left += a[i]
    print(-1)


def main():
    exercise1_range_sum()


if __name__ == "__main__":
    main()
