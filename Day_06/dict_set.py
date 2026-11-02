"""
Day 06 — dict, set, Counter & defaultdict
"""
import sys
from collections import Counter, defaultdict
input = sys.stdin.readline


def exercise1_two_sum():
    """Find indices i,j where a[i]+a[j]=target"""
    n, target = map(int, input().split())
    a = list(map(int, input().split()))
    seen = {}
    for i, x in enumerate(a):
        need = target - x
        if need in seen:
            print(seen[need], i)
            return
        seen[x] = i


def exercise2_anagram():
    """Check if two strings are anagrams"""
    s1 = input().strip()
    s2 = input().strip()
    print("YES" if Counter(s1) == Counter(s2) else "NO")


def exercise3_first_non_repeat():
    """First non-repeating character"""
    s = input().strip()
    cnt = Counter(s)
    for c in s:
        if cnt[c] == 1:
            print(c)
            return
    print(-1)


def exercise4_group_anagrams():
    """Group words by anagram family"""
    n = int(input())
    words = [input().strip() for _ in range(n)]
    groups = defaultdict(list)
    for w in words:
        key = ''.join(sorted(w))
        groups[key].append(w)
    for group in groups.values():
        print(*sorted(group))


def exercise5_subarray_sum_k():
    """Count subarrays with sum exactly k using prefix sum + dict"""
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    prefix_count = defaultdict(int)
    prefix_count[0] = 1
    prefix = 0
    count = 0
    for x in a:
        prefix += x
        count += prefix_count[prefix - k]
        prefix_count[prefix] += 1
    print(count)


def main():
    exercise1_two_sum()


if __name__ == "__main__":
    main()
