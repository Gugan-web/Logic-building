"""
Day 19 — Graph Theory: BFS & DFS
"""
import sys
from collections import deque, defaultdict
sys.setrecursionlimit(300000)
input = sys.stdin.readline


def build_graph(n, m, directed=False):
    g = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        if not directed:
            g[v].append(u)
    return g


# ════════════════════════════════════════════════════
# BFS — Breadth First Search
# ════════════════════════════════════════════════════
def bfs(graph, start, n):
    dist = [-1] * (n + 1)
    dist[start] = 0
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    return dist


# ════════════════════════════════════════════════════
# DFS — iterative (avoids recursion limit)
# ════════════════════════════════════════════════════
def dfs_iterative(graph, start, n):
    visited = [False] * (n + 1)
    stack = [start]
    order = []
    while stack:
        node = stack.pop()
        if visited[node]: continue
        visited[node] = True
        order.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                stack.append(neighbor)
    return order


# DFS — recursive
def dfs_recursive(graph, node, visited, order):
    visited[node] = True
    order.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs_recursive(graph, neighbor, visited, order)


# ════════════════════════════════════════════════════
# EXERCISE 1: Shortest Path (unweighted) using BFS
# ════════════════════════════════════════════════════
def exercise1_shortest_path():
    n, m = map(int, input().split())
    g = build_graph(n, m)
    src, dst = map(int, input().split())
    dist = bfs(g, src, n)
    print(dist[dst])   # -1 if not reachable


# ════════════════════════════════════════════════════
# EXERCISE 2: Count Connected Components
# ════════════════════════════════════════════════════
def exercise2_connected_components():
    n, m = map(int, input().split())
    g = build_graph(n, m)
    visited = [False] * (n + 1)
    count = 0
    for start in range(1, n + 1):
        if not visited[start]:
            count += 1
            dfs_iterative(g, start, n)
            # Mark all reachable as visited
            for node in dfs_iterative(g, start, n):
                visited[node] = True
    print(count)


# ════════════════════════════════════════════════════
# EXERCISE 3: Bipartite Check (2-coloring via BFS)
# ════════════════════════════════════════════════════
def exercise3_bipartite():
    n, m = map(int, input().split())
    g = build_graph(n, m)
    color = [-1] * (n + 1)

    def bfs_color(start):
        color[start] = 0
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for nb in g[node]:
                if color[nb] == -1:
                    color[nb] = 1 - color[node]
                    queue.append(nb)
                elif color[nb] == color[node]:
                    return False  # same color = not bipartite
        return True

    for i in range(1, n + 1):
        if color[i] == -1:
            if not bfs_color(i):
                print("NO")
                return
    print("YES")


# ════════════════════════════════════════════════════
# EXERCISE 4: Cycle Detection (undirected graph)
# ════════════════════════════════════════════════════
def exercise4_has_cycle():
    n, m = map(int, input().split())
    g = build_graph(n, m)
    visited = [False] * (n + 1)

    def dfs(node, parent):
        visited[node] = True
        for nb in g[node]:
            if not visited[nb]:
                if dfs(nb, node):
                    return True
            elif nb != parent:
                return True  # back edge = cycle
        return False

    for i in range(1, n + 1):
        if not visited[i] and dfs(i, -1):
            print("YES")
            return
    print("NO")


# ════════════════════════════════════════════════════
# EXERCISE 5: Flood Fill (grid BFS)
# ════════════════════════════════════════════════════
def exercise5_flood_fill():
    n, m = map(int, input().split())
    grid = [list(input().strip()) for _ in range(n)]
    sr, sc = map(int, input().split())
    target = grid[sr][sc]

    visited = [[False]*m for _ in range(n)]
    queue = deque([(sr, sc)])
    visited[sr][sc] = True
    count = 0
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]

    while queue:
        r, c = queue.popleft()
        count += 1
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0<=nr<n and 0<=nc<m and not visited[nr][nc] and grid[nr][nc] == target:
                visited[nr][nc] = True
                queue.append((nr, nc))

    print(count)


def main():
    exercise3_bipartite()


if __name__ == "__main__":
    main()
