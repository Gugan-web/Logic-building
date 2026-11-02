"""
Day 12 — Greedy Algorithms
"""
import sys
import heapq
input = sys.stdin.readline


def exercise1_coin_change_greedy():
    """Greedy coin change with standard denominations [1,5,10,25]"""
    n = int(input())
    coins = [25, 10, 5, 1]
    count = 0
    for c in coins:
        count += n // c
        n %= c
    print(count)


def exercise2_activity_selection():
    """Max non-overlapping intervals (sort by end time)"""
    n = int(input())
    intervals = [tuple(map(int, input().split())) for _ in range(n)]
    intervals.sort(key=lambda x: x[1])  # sort by end time
    count, last_end = 0, float('-inf')
    for start, end in intervals:
        if start >= last_end:
            count += 1
            last_end = end
    print(count)


def exercise3_min_platforms():
    """Minimum platforms for train scheduling"""
    n = int(input())
    arrivals = list(map(int, input().split()))
    departures = list(map(int, input().split()))
    arrivals.sort()
    departures.sort()
    platforms = 0
    max_platforms = 0
    i = j = 0
    while i < n:
        if arrivals[i] <= departures[j]:
            platforms += 1
            max_platforms = max(max_platforms, platforms)
            i += 1
        else:
            platforms -= 1
            j += 1
    print(max_platforms)


def exercise4_jump_game():
    """Can you reach the last index?"""
    n = int(input())
    a = list(map(int, input().split()))
    max_reach = 0
    for i in range(n):
        if i > max_reach:
            print("NO")
            return
        max_reach = max(max_reach, i + a[i])
    print("YES")


def exercise5_fractional_knapsack():
    """Maximize value with fractional items"""
    n, capacity = map(int, input().split())
    items = []
    for _ in range(n):
        w, v = map(int, input().split())
        items.append((v/w, w, v))   # (value per unit weight, weight, value)

    items.sort(reverse=True)        # greedy: best ratio first
    total_value = 0.0

    for ratio, w, v in items:
        if capacity >= w:
            total_value += v
            capacity -= w
        else:
            total_value += ratio * capacity
            break

    print(f"{total_value:.6f}")


def main():
    exercise2_activity_selection()


if __name__ == "__main__":
    main()
