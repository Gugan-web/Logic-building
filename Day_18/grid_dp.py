"""
Day 18 — DP: Grid & 2D Problems
"""
import sys
input = sys.stdin.readline

MOD = 10**9 + 7


# ════════════════════════════════════════════════════
# EXERCISE 1: Unique Paths in Grid
# Count paths from top-left to bottom-right (only right/down moves)
# ════════════════════════════════════════════════════
def exercise1_unique_paths():
    n, m = map(int, input().split())
    dp = [[1] * m for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD
    print(dp[n-1][m-1])


# ════════════════════════════════════════════════════
# EXERCISE 2: Min Cost Path
# ════════════════════════════════════════════════════
def exercise2_min_cost():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    dp = [[float('inf')] * m for _ in range(n)]
    dp[0][0] = grid[0][0]

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0: continue
            from_top  = dp[i-1][j] if i > 0 else float('inf')
            from_left = dp[i][j-1] if j > 0 else float('inf')
            dp[i][j] = grid[i][j] + min(from_top, from_left)

    print(dp[n-1][m-1])


# ════════════════════════════════════════════════════
# EXERCISE 3: Triangle Path (top to bottom, min sum)
# ════════════════════════════════════════════════════
def exercise3_triangle():
    n = int(input())
    tri = [list(map(int, input().split())) for _ in range(n)]

    # Bottom-up
    dp = tri[n-1][:]
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            dp[j] = tri[i][j] + min(dp[j], dp[j+1])

    print(dp[0])


# ════════════════════════════════════════════════════
# EXERCISE 4: Maximal Square of 1s
# ════════════════════════════════════════════════════
def exercise4_maximal_square():
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]

    dp = [[0]*m for _ in range(n)]
    best = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1':
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                best = max(best, dp[i][j])

    print(best * best)  # area


# ════════════════════════════════════════════════════
# EXERCISE 5: Dungeon (min health to reach bottom-right)
# ════════════════════════════════════════════════════
def exercise5_dungeon():
    n, m = map(int, input().split())
    dungeon = [list(map(int, input().split())) for _ in range(n)]

    dp = [[0]*m for _ in range(n)]
    dp[n-1][m-1] = max(1 - dungeon[n-1][m-1], 1)

    for j in range(m-2, -1, -1):
        dp[n-1][j] = max(dp[n-1][j+1] - dungeon[n-1][j], 1)
    for i in range(n-2, -1, -1):
        dp[i][m-1] = max(dp[i+1][m-1] - dungeon[i][m-1], 1)

    for i in range(n-2, -1, -1):
        for j in range(m-2, -1, -1):
            need = min(dp[i+1][j], dp[i][j+1])
            dp[i][j] = max(need - dungeon[i][j], 1)

    print(dp[0][0])


def main():
    exercise1_unique_paths()


if __name__ == "__main__":
    main()
