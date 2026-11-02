"""
Day 23 — Disjoint Set Union (DSU / Union-Find)
"""
import sys
input = sys.stdin.readline


# ════════════════════════════════════════════════════
# DSU — Core Implementation
# ════════════════════════════════════════════════════
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank   = [0] * n
        self.size   = [1] * n
        self.components = n

    def find(self, x):
        # Path compression (iterative — faster in Python)
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # path halving
            x = self.parent[x]
        return x

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return False   # already same component
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        self.size[px] += self.size[py]
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.components -= 1
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return self.size[self.find(x)]


# ════════════════════════════════════════════════════
# EXERCISE 1: Number of Connected Components
# ════════════════════════════════════════════════════
def exercise1_components():
    n, m = map(int, input().split())
    dsu = DSU(n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        dsu.union(u, v)
    print(dsu.components - 1)   # -1 for node 0 (unused)


# ════════════════════════════════════════════════════
# EXERCISE 2: Kruskal's MST (Minimum Spanning Tree)
# ════════════════════════════════════════════════════
def exercise2_kruskal():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
    edges.sort()    # sort by weight

    dsu = DSU(n + 1)
    mst_cost = 0
    mst_edges = 0

    for w, u, v in edges:
        if dsu.union(u, v):
            mst_cost += w
            mst_edges += 1
            if mst_edges == n - 1:
                break

    if mst_edges == n - 1:
        print(mst_cost)
    else:
        print("Not connected")


# ════════════════════════════════════════════════════
# EXERCISE 3: Detect Cycle using DSU
# ════════════════════════════════════════════════════
def exercise3_cycle():
    n, m = map(int, input().split())
    dsu = DSU(n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        if not dsu.union(u, v):
            print("YES")   # cycle detected
            return
    print("NO")


# ════════════════════════════════════════════════════
# EXERCISE 4: Largest Component Size
# ════════════════════════════════════════════════════
def exercise4_largest():
    n, m = map(int, input().split())
    dsu = DSU(n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        dsu.union(u, v)
    print(max(dsu.get_size(i) for i in range(1, n+1)))


# ════════════════════════════════════════════════════
# EXERCISE 5: Online Connectivity Queries
# Process "add edge" and "are u,v connected?" queries
# ════════════════════════════════════════════════════
def exercise5_online_queries():
    n, q = map(int, input().split())
    dsu = DSU(n + 1)
    for _ in range(q):
        line = input().split()
        if line[0] == 'U':
            dsu.union(int(line[1]), int(line[2]))
        else:
            print("YES" if dsu.same(int(line[1]), int(line[2])) else "NO")


def main():
    exercise2_kruskal()


if __name__ == "__main__":
    main()
