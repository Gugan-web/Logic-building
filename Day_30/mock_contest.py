"""
Day 30 — Full Mock Contest & Capstone Practice Set
A complete simulated 5-problem contest (Div. 2/Div. 3 style) with detailed editorials,
solutions, and local verification tests.

Problems:
- Problem A: Divisibility Permutation (Rating ~800) - Math & Greedy
- Problem B: Balanced Subsegment XOR (Rating ~1100) - Prefix XOR & Hash Map
- Problem C: Factory Pipeline Capacity (Rating ~1300) - Binary Search on Answer
- Problem D: Network Reconstruction (Rating ~1500) - Minimum Spanning Tree / DSU
- Problem E: Maximum Score Tree Partition (Rating ~1700) - Tree DP / Subtree Aggregations
"""

import sys
from collections import defaultdict, deque
import heapq

# Fast I/O Setup
input = sys.stdin.readline


# ═══════════════════════════════════════════════════════════════
# PROBLEM A: Divisibility Permutation (~800 Rating)
# ═══════════════════════════════════════════════════════════════
"""
Problem Statement:
You are given an integer n. Construct a permutation p of length n such that
for every i from 1 to n, (p[i] + i) is NOT divisible by 2 (i.e. p[i] + i is odd).
If no such permutation exists, output -1.

Constraints:
1 <= t <= 10^4
1 <= n <= 10^5
Sum of n over test cases <= 2 * 10^5

Editorial:
For p[i] + i to be odd, one of p[i] and i must be odd, and the other must be even.
- If i is odd, p[i] must be even.
- If i is even, p[i] must be odd.
This requires that the count of odd positions equals the count of even positions,
which is ONLY possible if n is even!
If n is odd, the number of odd positions is (n+1)//2, but the number of available
even numbers is only n//2. By Pigeonhole Principle, no solution exists for odd n.
For even n: swap adjacent pairs (1 with 2, 3 with 4, ..., i with i+1).
Then at odd i, p[i] = i + 1 (even). At even i+1, p[i+1] = i (odd).
Time Complexity: O(n)
Space Complexity: O(n)
"""

def solve_problem_a(n: int):
    if n % 2 != 0:
        return [-1]
    # Swap adjacent elements: 2, 1, 4, 3, 6, 5, ...
    res = []
    for i in range(1, n + 1, 2):
        res.append(i + 1)
        res.append(i)
    return res


# ═══════════════════════════════════════════════════════════════
# PROBLEM B: Balanced Subsegment XOR (~1100 Rating)
# ═══════════════════════════════════════════════════════════════
"""
Problem Statement:
Given an array of n integers a[1..n] and an integer k.
Find the number of contiguous subarrays whose bitwise XOR sum equals k.

Constraints:
1 <= n <= 2 * 10^5
0 <= a[i], k <= 10^9

Editorial:
Let P[i] = a[1] ^ a[2] ^ ... ^ a[i] be the prefix XOR array, with P[0] = 0.
The XOR sum of subarray a[l..r] is P[r] ^ P[l - 1].
We want:
    P[r] ^ P[l - 1] = k
    <=> P[l - 1] = P[r] ^ k   (by XOR property: A ^ B = C <=> A = B ^ C)

So for each index r (1 <= r <= n), the number of valid left endpoints l is the
number of times the value (P[r] ^ k) has appeared as a prefix XOR prior to r.
We maintain a frequency hash map of prefix XOR values seen so far.
Time Complexity: O(n)
Space Complexity: O(n)
"""

def solve_problem_b(arr: list, k: int) -> int:
    prefix_count = defaultdict(int)
    prefix_count[0] = 1  # Base case: empty prefix has XOR 0
    
    current_xor = 0
    ans = 0
    for x in arr:
        current_xor ^= x
        target = current_xor ^ k
        ans += prefix_count[target]
        prefix_count[current_xor] += 1
        
    return ans


# ═══════════════════════════════════════════════════════════════
# PROBLEM C: Factory Pipeline Capacity (~1300 Rating)
# ═══════════════════════════════════════════════════════════════
"""
Problem Statement:
A factory has n machines. Machine i can process 1 unit of product in time[i] seconds.
All machines operate simultaneously and independently.
Find the minimum time needed to produce at least t units of product in total.

Constraints:
1 <= n <= 2 * 10^5
1 <= t <= 10^9
1 <= time[i] <= 10^9

Editorial:
Let f(M) be the total number of products processed in M seconds.
In M seconds, machine i produces floor(M / time[i]) items.
Total products = sum(M // time[i] for each i).
Notice f(M) is monotonically non-decreasing with respect to M:
If M1 <= M2, then f(M1) <= f(M2).
Hence, this is a classic "Binary Search on Answer":
- Lower bound low = 1
- Upper bound high = min(time) * t <= 10^18
Check condition: sum(mid // x for x in time) >= t
Time Complexity: O(n * log(min(time) * t))
Space Complexity: O(1)
"""

def solve_problem_c(machines: list, t: int) -> int:
    low = 1
    high = min(machines) * t
    ans = high
    
    while low <= high:
        mid = (low + high) // 2
        
        # Calculate total products made in 'mid' time
        total = 0
        for m in machines:
            total += mid // m
            if total >= t:  # Early break optimization
                break
                
        if total >= t:
            ans = mid
            high = mid - 1  # Try to achieve with less time
        else:
            low = mid + 1   # Need more time
            
    return ans


# ═══════════════════════════════════════════════════════════════
# PROBLEM D: Network Reconstruction (~1500 Rating)
# ═══════════════════════════════════════════════════════════════
"""
Problem Statement:
There are n cities and m bi-directional candidate roads. Road i connects city u_i
and city v_i with maintenance cost w_i.
Find the minimum total cost to make all n cities mutually reachable.
If it is impossible to connect all cities, output -1.

Constraints:
1 <= n <= 10^5
1 <= m <= 2 * 10^5
1 <= w_i <= 10^9

Editorial:
This is the Minimum Spanning Tree (MST) problem.
We use Kruskal's Algorithm with Disjoint Set Union (DSU):
1. Sort all edges in non-decreasing order of cost w_i.
2. Initialize DSU with n isolated sets.
3. Iterate through sorted edges. If endpoints u and v are in different sets,
   union them and add w_i to total cost.
4. Stop when n - 1 edges have been added (or after checking all edges).
5. If the number of connected components remaining > 1 (i.e. edges added < n - 1), return -1.
Time Complexity: O(m log m)
Space Complexity: O(n + m)
"""

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        self.components = n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            if self.rank[root_i] == self.rank[root_j]:
                self.rank[root_i] += 1
            self.components -= 1
            return True
        return False


def solve_problem_d(n: int, edges: list) -> int:
    # edges: list of (w, u, v)
    edges.sort(key=lambda x: x[0])
    dsu = DSU(n)
    
    total_cost = 0
    edges_used = 0
    
    for w, u, v in edges:
        if dsu.union(u, v):
            total_cost += w
            edges_used += 1
            if edges_used == n - 1:
                break
                
    if edges_used == n - 1:
        return total_cost
    return -1


# ═══════════════════════════════════════════════════════════════
# PROBLEM E: Maximum Score Tree Partition (~1700 Rating)
# ═══════════════════════════════════════════════════════════════
"""
Problem Statement:
You are given a tree with n nodes rooted at node 1. Each node u has an integer weight val[u].
You may select an independent set of nodes (no two adjacent nodes may both be selected).
Find the maximum possible total weight of selected nodes.

Constraints:
1 <= n <= 2 * 10^5
-10^9 <= val[u] <= 10^9

Editorial:
This is the Maximum Weight Independent Set on a Tree (Tree DP).
For each node u:
- dp[u][0]: max weight in subtree of u if node u is NOT selected.
- dp[u][1]: max weight in subtree of u if node u IS selected.

Transitions for each child v of u:
- If u is NOT selected: child v can be either selected or not selected.
    dp[u][0] += max(dp[v][0], dp[v][1])
- If u IS selected: child v CANNOT be selected (must take dp[v][0]).
    dp[u][1] += dp[v][0]
Base case:
    dp[u][0] = 0
    dp[u][1] = val[u]
Answer: max(dp[1][0], dp[1][1])

To prevent recursion limit issues in deep Python call stacks, an iterative
post-order traversal via DFS with node stack is used.
Time Complexity: O(n)
Space Complexity: O(n)
"""

def solve_problem_e(n: int, val: list, adj: list) -> int:
    # val is 1-indexed (val[0] is dummy)
    dp0 = [0] * (n + 1)
    dp1 = [0] * (n + 1)
    
    # Iterative post-order traversal using parent array and BFS/DFS order
    parent = [0] * (n + 1)
    order = []
    stack = [1]
    visited = [False] * (n + 1)
    visited[1] = True
    
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                stack.append(v)
                
    # Process from leaves up to root (reverse topological order)
    for u in reversed(order):
        dp1[u] = val[u]
        dp0[u] = 0
        for v in adj[u]:
            if v != parent[u]:
                dp0[u] += max(dp0[v], dp1[v])
                dp1[u] += dp0[v]
                
    return max(dp0[1], dp1[1])


# ═══════════════════════════════════════════════════════════════
# SELF-TESTING SUITE
# ═══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("=" * 60)
    print("DAY 30: MOCK CONTEST TEST SUITE")
    print("=" * 60)

    # Test Problem A
    print("\n--- Problem A: Divisibility Permutation ---")
    res_a4 = solve_problem_a(4)
    print(f"n = 4 -> {res_a4}")
    assert res_a4 == [2, 1, 4, 3], "Failed Problem A test (even)"
    res_a3 = solve_problem_a(3)
    print(f"n = 3 -> {res_a3}")
    assert res_a3 == [-1], "Failed Problem A test (odd)"
    print("Problem A Passed!")

    # Test Problem B
    print("\n--- Problem B: Balanced Subsegment XOR ---")
    arr_b = [4, 2, 2, 6, 4]
    k_b = 6
    ans_b = solve_problem_b(arr_b, k_b)
    print(f"arr = {arr_b}, k = {k_b} -> count = {ans_b}")
    assert ans_b == 4, f"Expected 4, got {ans_b}"
    print("Problem B Passed!")

    # Test Problem C
    print("\n--- Problem C: Factory Pipeline Capacity ---")
    machines_c = [2, 3, 7]
    t_c = 7
    ans_c = solve_problem_c(machines_c, t_c)
    print(f"machines = {machines_c}, t = {t_c} -> min time = {ans_c}")
    assert ans_c == 8, f"Expected 8, got {ans_c}"
    print("Problem C Passed!")

    # Test Problem D
    print("\n--- Problem D: Network Reconstruction ---")
    # 4 cities, edges: (cost, u, v)
    edges_d = [
        (1, 1, 2),
        (3, 1, 3),
        (2, 2, 3),
        (5, 3, 4),
        (7, 2, 4)
    ]
    ans_d = solve_problem_d(4, edges_d)
    print(f"n = 4, edges = {edges_d} -> MST cost = {ans_d}")
    assert ans_d == 8, f"Expected 8 (edges 1-2=1, 2-3=2, 3-4=5), got {ans_d}"
    print("Problem D Passed!")

    # Test Problem E
    print("\n--- Problem E: Maximum Score Tree Partition ---")
    # Tree: 1-2, 1-3, 2-4, 2-5
    # Weights: node 1=5, 2=2, 3=8, 4=4, 5=9
    n_e = 5
    val_e = [0, 5, 2, 8, 4, 9]
    adj_e = defaultdict(list)
    edges_e = [(1, 2), (1, 3), (2, 4), (2, 5)]
    for u, v in edges_e:
        adj_e[u].append(v)
        adj_e[v].append(u)
    ans_e = solve_problem_e(n_e, val_e, adj_e)
    print(f"n = {n_e}, weights = {val_e[1:]} -> Max independent set = {ans_e}")
    # Choosing 1 (5), 4 (4), 5 (9) = 18. Or 3 (8), 4 (4), 5 (9) = 21. Choosing 3 (8) and 1 (5) cannot be chosen together? 1 and 3 are adjacent!
    # Valid: {3, 4, 5, 1} ? 1 is adjacent to 3, so {3, 4, 5} gives 8 + 4 + 9 = 21.
    assert ans_e == 21, f"Expected 21, got {ans_e}"
    print("Problem E Passed!")

    print("\n" + "=" * 60)
    print("ALL MOCK CONTEST PROBLEMS PASSED SUCCESSFULLY!")
    print("=" * 60)
