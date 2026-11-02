"""
Day 07 — Stack, Queue (deque) & Heap (heapq)
"""
import sys
import heapq
from collections import deque
input = sys.stdin.readline


# ════════════════════════════════════════════════════
# EXERCISE 1: Valid Bracket Matching
# ════════════════════════════════════════════════════
def exercise1_valid_brackets():
    s = input().strip()
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in '([{':
            stack.append(c)
        elif c in ')]}':
            if not stack or stack[-1] != pairs[c]:
                print("NO")
                return
            stack.pop()
    print("YES" if not stack else "NO")


# ════════════════════════════════════════════════════
# EXERCISE 2: Sliding Window Maximum (Monotonic Deque)
# ════════════════════════════════════════════════════
def exercise2_sliding_max():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    dq = deque()  # stores indices, decreasing values
    result = []

    for i in range(n):
        # Remove elements out of window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        # Remove smaller elements from back
        while dq and a[dq[-1]] <= a[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(a[dq[0]])

    print(*result)


# ════════════════════════════════════════════════════
# EXERCISE 3: K Largest Elements using Min-Heap
# ════════════════════════════════════════════════════
def exercise3_k_largest():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    heap = []  # min-heap of size k
    for x in a:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)

    print(*sorted(heap))


# ════════════════════════════════════════════════════
# EXERCISE 4: Stock Span (Monotonic Stack)
# ════════════════════════════════════════════════════
def exercise4_stock_span():
    n = int(input())
    prices = list(map(int, input().split()))

    stack = []  # stores indices
    span = [0] * n

    for i in range(n):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        span[i] = i + 1 if not stack else i - stack[-1]
        stack.append(i)

    print(*span)


# ════════════════════════════════════════════════════
# EXERCISE 5: Merge K Sorted Lists
# ════════════════════════════════════════════════════
def exercise5_merge_k_sorted():
    k = int(input())
    lists = []
    for _ in range(k):
        row = list(map(int, input().split()))
        lists.append(row)

    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    result = []
    while heap:
        val, li, idx = heapq.heappop(heap)
        result.append(val)
        if idx + 1 < len(lists[li]):
            heapq.heappush(heap, (lists[li][idx+1], li, idx+1))

    print(*result)


# ─── Demo: BFS using deque ───────────────────────────────────
def bfs_demo(graph, start):
    visited = set([start])
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


def main():
    exercise1_valid_brackets()


if __name__ == "__main__":
    main()
