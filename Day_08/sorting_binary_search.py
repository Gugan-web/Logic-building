"""
Day 08 — Sorting & Binary Search (bisect)
"""
import sys
from bisect import bisect_left, bisect_right, insort
from collections import Counter
input = sys.stdin.readline


def binary_search(a, target):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == target:   return mid
        elif a[mid] < target:  lo = mid + 1
        else:                  hi = mid - 1
    return -1


def lower_bound(a, x):
    """First index i such that a[i] >= x"""
    return bisect_left(a, x)


def upper_bound(a, x):
    """First index i such that a[i] > x"""
    return bisect_right(a, x)


def exercise1_search():
    n = int(input())
    a = list(map(int, input().split()))
    target = int(input())
    print(binary_search(sorted(a), target))


def exercise2_count_range():
    n = int(input())
    a = sorted(map(int, input().split()))
    L, R = map(int, input().split())
    print(bisect_right(a, R) - bisect_left(a, L))


def exercise3_insert_position():
    n = int(input())
    a = sorted(map(int, input().split()))
    x = int(input())
    print(bisect_left(a, x))


def exercise4_sort_by_frequency():
    n = int(input())
    a = list(map(int, input().split()))
    freq = Counter(a)
    a.sort(key=lambda x: (-freq[x], x))
    print(*a)


def exercise5_merge_sort_inversions():
    """Count inversions using modified merge sort"""
    def merge_count(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        left, lc = merge_count(arr[:mid])
        right, rc = merge_count(arr[mid:])
        merged, mc = [], 0
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i]); i += 1
            else:
                merged.append(right[j]); j += 1
                mc += len(left) - i  # all remaining left are > right[j]
        merged.extend(left[i:]); merged.extend(right[j:])
        return merged, lc + rc + mc

    n = int(input())
    a = list(map(int, input().split()))
    _, inv = merge_count(a)
    print(inv)


def main():
    exercise2_count_range()


if __name__ == "__main__":
    main()
