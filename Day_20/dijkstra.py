"""
Day 20 — Shortest Path: Dijkstra & Multi-Source BFS
"""
import sys
import heapq
from collections import defaultdict, deque
input = sys.stdin.readline
INF = float('inf')


def build_weighted_graph(n, m, directed=False):
    g = defaultdict(list)
    for _ in range(m):
        u, v, w = map(int, input().split())
        g[u].append((v, w))
        if not directed:
            g[v].append((u, w))
    return g


# ════════════════════════════════════════════════════
# Dijkstra's Algorithm — O((V + E) log V)
# Single-source shortest path (non-negative weights)
# ════════════════════════════════════════════════════
def dijkstra(graph, src, n):
    dist = [INF] * (n + 1)
    dist[src] = 0
    heap = [(0, src)]   # (distance, node)

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue    # outdated entry — skip
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    return dist


# ════════════════════════════════════════════════════
# 0-1 BFS — when edge weights are only 0 or 1
# Use deque: weight=0 → appendleft, weight=1 → append
# ════════════════════════════════════════════════════
def bfs_01(graph, src, n):
    dist = [INF] * (n + 1)
    dist[src] = 0
    dq = deque([src])

    while dq:
        u = dq.popleft()
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if w == 0:
                    dq.appendleft(v)
                else:
                    dq.append(v)
    return dist


# ════════════════════════════════════════════════════
# EXERCISE 1: Single-Source Shortest Path with Dijkstra
# ════════════════════════════════════════════════════
def exercise1_dijkstra():
    n, m = map(int, input().split())
    g = build_weighted_graph(n, m)
    src = int(input())
    dist = dijkstra(g, src, n)
    print(*[d if d != INF else -1 for d in dist[1:]])


# ════════════════════════════════════════════════════
# EXERCISE 2: Shortest Path Between Two Nodes
# ════════════════════════════════════════════════════
def exercise2_src_to_dst():
    n, m = map(int, input().split())
    g = build_weighted_graph(n, m)
    src, dst = map(int, input().split())
    dist = dijkstra(g, src, n)
    print(dist[dst] if dist[dst] != INF else -1)


# ════════════════════════════════════════════════════
# EXERCISE 3: Multi-Source BFS (shortest dist from ANY source)
# ════════════════════════════════════════════════════
def exercise3_multisource_bfs():
    n, m, k = map(int, input().split())
    sources = list(map(int, input().split()))
    g = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v); g[v].append(u)

    dist = [-1] * (n + 1)
    queue = deque()
    for s in sources:
        dist[s] = 0
        queue.append(s)

    while queue:
        u = queue.popleft()
        for v in g[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)

    print(*dist[1:])


# ════════════════════════════════════════════════════
# EXERCISE 4: Reconstruct Shortest Path
# ════════════════════════════════════════════════════
def exercise4_reconstruct():
    n, m = map(int, input().split())
    g = build_weighted_graph(n, m)
    src, dst = map(int, input().split())

    dist = [INF] * (n + 1)
    prev = [-1] * (n + 1)
    dist[src] = 0
    heap = [(0, src)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]: continue
        for v, w in g[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(heap, (dist[v], v))

    if dist[dst] == INF:
        print(-1)
        return

    # Reconstruct path
    path = []
    cur = dst
    while cur != -1:
        path.append(cur)
        cur = prev[cur]
    print(*reversed(path))


def main():
    exercise1_dijkstra()


if __name__ == "__main__":
    main()
