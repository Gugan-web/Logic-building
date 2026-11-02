"""
Day 27 — Binary Search on Answer
"""
import sys
input = sys.stdin.readline


# ════════════════════════════════════════════════════
# BINARY SEARCH ON ANSWER TEMPLATE
# ════════════════════════════════════════════════════
# When: answer is monotonic (if X works, all Y > X also work or don't work)
# Strategy: binary search on the answer space, check feasibility with a function

def binary_search_answer(lo, hi, feasible):
    """Find minimum value in [lo, hi] where feasible(mid) is True"""
    result = hi
    while lo <= hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            result = mid
            hi = mid - 1   # try smaller
        else:
            lo = mid + 1
    return result


# ════════════════════════════════════════════════════
# EXERCISE 1: Koko Eating Bananas
# Min eating speed k such that Koko can eat all piles in h hours
# ════════════════════════════════════════════════════
def exercise1_koko():
    n, h = map(int, input().split())
    piles = list(map(int, input().split()))

    def feasible(speed):
        hours = sum((p + speed - 1) // speed for p in piles)
        return hours <= h

    lo, hi = 1, max(piles)
    print(binary_search_answer(lo, hi, feasible))


# ════════════════════════════════════════════════════
# EXERCISE 2: Allocate Minimum Pages
# Divide n books among m students, minimize max pages assigned
# ════════════════════════════════════════════════════
def exercise2_min_pages():
    n, m = map(int, input().split())
    books = list(map(int, input().split()))

    def feasible(limit):
        students = 1
        current = 0
        for b in books:
            if b > limit: return False  # single book too large
            if current + b > limit:
                students += 1
                current = b
            else:
                current += b
        return students <= m

    lo, hi = max(books), sum(books)
    print(binary_search_answer(lo, hi, feasible))


# ════════════════════════════════════════════════════
# EXERCISE 3: Aggressive Cows
# Place k cows in n stalls (given positions), maximize minimum distance
# ════════════════════════════════════════════════════
def exercise3_aggressive_cows():
    n, k = map(int, input().split())
    stalls = sorted(map(int, input().split()))

    def feasible(min_dist):
        cows = 1
        last = stalls[0]
        for i in range(1, n):
            if stalls[i] - last >= min_dist:
                cows += 1
                last = stalls[i]
                if cows == k: return True
        return cows >= k

    lo, hi = 1, stalls[-1] - stalls[0]
    # Find maximum feasible distance (reverse: feasible = True = try larger)
    result = lo
    while lo <= hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            result = mid
            lo = mid + 1
        else:
            hi = mid - 1
    print(result)


# ════════════════════════════════════════════════════
# EXERCISE 4: Smallest Divisor (minimize max division result)
# Find minimum divisor d such that sum(ceil(a[i]/d)) <= threshold
# ════════════════════════════════════════════════════
def exercise4_smallest_divisor():
    n, threshold = map(int, input().split())
    a = list(map(int, input().split()))

    def feasible(d):
        return sum((x + d - 1) // d for x in a) <= threshold

    lo, hi = 1, max(a)
    print(binary_search_answer(lo, hi, feasible))


# ════════════════════════════════════════════════════
# EXERCISE 5: Find nth Root (binary search on floats)
# ════════════════════════════════════════════════════
def exercise5_nth_root():
    n, target = map(int, input().split())
    lo, hi = 0.0, max(target, 1.0)
    for _ in range(100):   # enough iterations for precision
        mid = (lo + hi) / 2
        if mid**n < target:
            lo = mid
        else:
            hi = mid
    print(f"{lo:.9f}")


def main():
    exercise2_min_pages()


if __name__ == "__main__":
    main()
