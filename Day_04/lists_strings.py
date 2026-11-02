"""
Day 04 — Lists & Strings
"""
import sys
from collections import Counter
input = sys.stdin.readline


# ════════════════════════════════════════════════════
# EXERCISE 1: Rotate Array Left by k
# ════════════════════════════════════════════════════
def exercise1():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    k %= n  # handle k >= n
    print(*a[k:] + a[:k])


# ════════════════════════════════════════════════════
# EXERCISE 2: Palindrome Check
# ════════════════════════════════════════════════════
def exercise2():
    s = input().strip().lower()
    s = ''.join(c for c in s if c.isalnum())
    print("YES" if s == s[::-1] else "NO")


# ════════════════════════════════════════════════════
# EXERCISE 3: Most Frequent Element
# ════════════════════════════════════════════════════
def exercise3():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = Counter(a)
    print(cnt.most_common(1)[0][0])


# ════════════════════════════════════════════════════
# EXERCISE 4: String Compression
# ════════════════════════════════════════════════════
def exercise4():
    s = input().strip()
    result = []
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        result.append(s[i] + str(j - i))
        i = j
    print(''.join(result))


# ════════════════════════════════════════════════════
# EXERCISE 5: 2D Grid Maximum
# ════════════════════════════════════════════════════
def exercise5():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(max(grid[i][j] for i in range(n) for j in range(m)))


# ─── Utility demos ───────────────────────────────────────────

def list_tricks():
    a = [3, 1, 4, 1, 5, 9, 2, 6]
    print(sorted(a))                     # ascending
    print(sorted(a, reverse=True))       # descending
    print(sorted(a, key=lambda x: -x))  # same as reverse=True

    # Prefix max
    prefix_max = []
    curr_max = float('-inf')
    for x in a:
        curr_max = max(curr_max, x)
        prefix_max.append(curr_max)
    print(prefix_max)


def string_tricks():
    s = "Hello World"
    print(s[::-1])               # reverse
    print(s.count('l'))          # count occurrences
    print('|'.join(s.split()))   # "Hello|World"
    print(sorted(s.lower()))     # sort characters
    print(set(s.lower()) - {' '})  # unique chars (excluding space)


def main():
    exercise1()


if __name__ == "__main__":
    main()
