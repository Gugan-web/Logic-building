"""
Day 21 — Trees & Binary Trees
"""
import sys
from collections import defaultdict, deque
sys.setrecursionlimit(300000)
input = sys.stdin.readline


# ════════════════════════════════════════════════════
# Tree Node (for binary tree problems)
# ════════════════════════════════════════════════════
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ════════════════════════════════════════════════════
# Generic Tree (adjacency list)
# ════════════════════════════════════════════════════
def build_tree(n):
    """Read n-1 edges for an unrooted tree"""
    g = defaultdict(list)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    return g


# ════════════════════════════════════════════════════
# EXERCISE 1: Tree Diameter (longest path)
# Two BFS approach
# ════════════════════════════════════════════════════
def bfs_farthest(graph, src, n):
    dist = [-1] * (n + 1)
    dist[src] = 0
    queue = deque([src])
    farthest = src
    while queue:
        u = queue.popleft()
        if dist[u] > dist[farthest]:
            farthest = u
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)
    return farthest, dist[farthest]

def exercise1_diameter():
    n = int(input())
    g = build_tree(n)
    # BFS from any node to find one endpoint of diameter
    u, _ = bfs_farthest(g, 1, n)
    # BFS from that endpoint to find diameter
    _, diameter = bfs_farthest(g, u, n)
    print(diameter)


# ════════════════════════════════════════════════════
# EXERCISE 2: Height of Tree (rooted at node 1)
# ════════════════════════════════════════════════════
def exercise2_height():
    n = int(input())
    g = build_tree(n)
    depth = [-1] * (n + 1)
    depth[1] = 0
    queue = deque([1])
    max_depth = 0
    while queue:
        u = queue.popleft()
        for v in g[u]:
            if depth[v] == -1:
                depth[v] = depth[u] + 1
                max_depth = max(max_depth, depth[v])
                queue.append(v)
    print(max_depth)


# ════════════════════════════════════════════════════
# EXERCISE 3: Subtree Sizes (DFS iterative)
# ════════════════════════════════════════════════════
def exercise3_subtree_sizes():
    n = int(input())
    g = build_tree(n)
    size = [1] * (n + 1)
    parent = [0] * (n + 1)
    order = []

    # Iterative DFS to get topological order
    visited = [False] * (n + 1)
    stack = [1]
    visited[1] = True
    while stack:
        u = stack.pop()
        order.append(u)
        for v in g[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                stack.append(v)

    # Process in reverse order (leaves first)
    for u in reversed(order):
        if parent[u] != 0:
            size[parent[u]] += size[u]

    print(*size[1:])


# ════════════════════════════════════════════════════
# EXERCISE 4: LCA — Lowest Common Ancestor (binary lifting)
# ════════════════════════════════════════════════════
def exercise4_lca():
    n, q = map(int, input().split())
    g = build_tree(n)
    LOG = 18

    depth = [0] * (n + 1)
    up = [[0] * (n + 1) for _ in range(LOG)]  # up[k][v] = 2^k-th ancestor of v

    # BFS to set depth and direct parent
    visited = [False] * (n + 1)
    queue = deque([1])
    visited[1] = True
    while queue:
        u = queue.popleft()
        for v in g[u]:
            if not visited[v]:
                visited[v] = True
                depth[v] = depth[u] + 1
                up[0][v] = u
                queue.append(v)

    # Build sparse table for ancestors
    for k in range(1, LOG):
        for v in range(1, n + 1):
            up[k][v] = up[k-1][up[k-1][v]]

    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        diff = depth[u] - depth[v]
        for k in range(LOG):
            if diff >> k & 1:
                u = up[k][u]
        if u == v: return u
        for k in range(LOG - 1, -1, -1):
            if up[k][u] != up[k][v]:
                u = up[k][u]
                v = up[k][v]
        return up[0][u]

    for _ in range(q):
        u, v = map(int, input().split())
        print(lca(u, v))


def main():
    exercise1_diameter()


if __name__ == "__main__":
    main()
