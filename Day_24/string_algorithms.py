"""
Day 24 — String Algorithms: KMP & Z-Function
"""
import sys
input = sys.stdin.readline


# ════════════════════════════════════════════════════
# Z-FUNCTION — O(n)
# z[i] = length of longest prefix of s that matches s[i..]
# z[0] = 0 by convention
# ════════════════════════════════════════════════════
def z_function(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z


# ════════════════════════════════════════════════════
# KMP — Knuth-Morris-Pratt — O(n + m)
# Failure function: fail[i] = longest proper prefix = suffix of p[:i+1]
# ════════════════════════════════════════════════════
def kmp_failure(pattern):
    m = len(pattern)
    fail = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = fail[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        fail[i] = j
    return fail


def kmp_search(text, pattern):
    """Return all starting indices of pattern in text"""
    if not pattern: return []
    combined = pattern + '#' + text   # '#' must not appear in text/pattern
    z = z_function(combined)
    m = len(pattern)
    result = []
    for i in range(m + 1, len(combined)):
        if z[i] == m:
            result.append(i - m - 1)   # index in text
    return result


# ════════════════════════════════════════════════════
# EXERCISES
# ════════════════════════════════════════════════════

def exercise1_pattern_search():
    """Find all occurrences of pattern in text"""
    text    = input().strip()
    pattern = input().strip()
    positions = kmp_search(text, pattern)
    print(len(positions))
    if positions:
        print(*[p + 1 for p in positions])  # 1-indexed


def exercise2_shortest_period():
    """Find shortest period of a string using Z or KMP failure function"""
    s = input().strip()
    n = len(s)
    fail = kmp_failure(s)
    period = n - fail[-1]
    if n % period == 0:
        print(period)
    else:
        print(n)  # no proper period, period is whole string


def exercise3_count_distinct_substrings():
    """Count distinct substrings using Z-function (simple approach)"""
    s = input().strip()
    n = len(s)
    # Number of distinct substrings = n*(n+1)/2 - sum(max z values for each suffix)
    total = n * (n + 1) // 2
    for i in range(1, n):
        z = z_function(s[i:] + '#' + s)
        total -= max(z[len(s)-i+1:len(s)-i+1+i] or [0])
    # Simple O(n^2) alternative: use set
    substrings = set()
    for i in range(n):
        for j in range(i+1, n+1):
            substrings.add(s[i:j])
    print(len(substrings))


def exercise4_string_rotation():
    """Check if s2 is a rotation of s1"""
    s1 = input().strip()
    s2 = input().strip()
    if len(s1) != len(s2):
        print("NO")
        return
    # s2 is rotation of s1 iff s2 is substring of s1+s1
    combined = s1 + s1
    positions = kmp_search(combined, s2)
    print("YES" if positions else "NO")


def exercise5_longest_palindromic_prefix():
    """Find longest palindromic prefix using z-function"""
    s = input().strip()
    # Combine s with reversed s: "s#rev_s"
    combined = s + '#' + s[::-1]
    z = z_function(combined)
    n = len(s)
    # Find longest prefix of s equal to suffix of rev_s
    best = 0
    for i in range(n + 1, 2 * n + 1):
        pos_in_s = (2*n + 1) - i  # how far from end of rev_s
        length = z[i]
        if pos_in_s == length:    # prefix matches suffix at right position
            best = max(best, length)
    print(best)


def main():
    exercise1_pattern_search()


if __name__ == "__main__":
    main()
