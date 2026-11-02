"""
Day 26 — Advanced Graphs: Topological Sort & SCC
"""
import sys
from collections import defaultdict, deque
sys.setrecursionlimit(300000)
input = sys.stdin.readline


# ════════════════════════════════════════════════════
# TOPOLOGICAL SORT — Kahn's Algorithm (BFS-based)
# Works on DAG (Directed Acyclic Graph)
# ════════════════════════════════════════════════════
def topological_sort_kahn(graph, n):
    in_degree = [0] * (n + 1)
    for u in range(1, n + 1):
        for v in graph[u]:
            in_degree[v] += 1

    queue = deque([u for u in range(1, n + 1) if in_degree[u] == 0])
    order = []

    while queue:
        u = queue.popleft()
        order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(order) != n:
        return None   # cycle detected — not a DAG
    return order


# ════════════════════════════════════════════════════
# TOPOLOGICAL SORT — DFS-based
# ════════════════════════════════════════════════════
def topological_sort_dfs(graph, n):
    visited = [0] * (n + 1)  # 0=unvisited, 1=in-stack, 2=done
    order = []
    has_cycle = [False]

    def dfs(u):
        visited[u] = 1
        for v in graph[u]:
            if visited[v] == 1:
                has_cycle[0] = True
                return
            if visited[v] == 0:
                dfs(v)
        visited[u] = 2
        order.append(u)

    for i in range(1, n + 1):
        if visited[i] == 0:
            dfs(i)

    if has_cycle[0]: return None
    return order[::-1]


# ════════════════════════════════════════════════════
# SCC — Kosaraju's Algorithm O(V + E)
# ════════════════════════════════════════════════════
def kosaraju_scc(graph, graph_rev, n):
    visited = [False] * (n + 1)
    finish_order = []

    def dfs1(u):
        stack = [(u, 0)]
        while stack:
            node, state = stack.pop()
            if state == 0:
                if visited[node]: continue
                visited[node] = True
                stack.append((node, 1))
                for v in graph[node]:
                    if not visited[v]:
                        stack.append((v, 0))
            else:
                finish_order.append(node)

    for i in range(1, n + 1):
        if not visited[i]:
            dfs1(i)

    visited2 = [False] * (n + 1)
    sccs = []

    def dfs2(u, component):
        stack = [u]
        while stack:
            node = stack.pop()
            if visited2[node]: continue
            visited2[node] = True
            component.append(node)
            for v in graph_rev[node]:
                if not visited2[v]:
                    stack.append(v)

    for u in reversed(finish_order):
        if not visited2[u]:
            comp = []
            dfs2(u, comp)
            sccs.append(comp)

    return sccs


# ════════════════════════════════════════════════════
# EXERCISES
# ════════════════════════════════════════════════════

def exercise1_topo_sort():
    n, m = map(int, input().split())
    g = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
    order = topological_sort_kahn(g, n)
    if order:
        print(*order)
    else:
        print("CYCLE")


def exercise2_course_schedule():
    """Can you complete all courses given prerequisites?"""
    n, m = map(int, input().split())
    g = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        g[b].append(a)    # b must be taken before a
    order = topological_sort_kahn(g, n)
    print("YES" if order else "NO")


def exercise3_count_scc():
    n, m = map(int, input().split())
    g = defaultdict(list)
    g_rev = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g_rev[v].append(u)
    sccs = kosaraju_scc(g, g_rev, n)
    print(len(sccs))


def exercise4_longest_path_dag():
    """Longest path in DAG using topo sort + DP"""
    n, m = map(int, input().split())
    g = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)

    order = topological_sort_kahn(g, n)
    if not order:
        print("CYCLE"); return

    dp = [0] * (n + 1)
    for u in order:
        for v in g[u]:
            dp[v] = max(dp[v], dp[u] + 1)
    print(max(dp))


def main():
    exercise1_topo_sort()


if __name__ == "__main__":
    main()
