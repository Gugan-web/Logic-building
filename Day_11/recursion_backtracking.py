"""
Day 11 — Recursion & Backtracking
"""
import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline


# ════════════════════════════════════════════════════
# BACKTRACKING TEMPLATE
# ════════════════════════════════════════════════════
def backtrack(state, choices):
    if is_solution(state):
        record(state)
        return
    for choice in choices:
        if is_valid(state, choice):
            make_choice(state, choice)
            backtrack(state, choices)
            undo_choice(state, choice)


# ════════════════════════════════════════════════════
# EXERCISE 1: All Permutations
# ════════════════════════════════════════════════════
def exercise1_permutations():
    n = int(input())
    a = list(map(int, input().split()))
    result = []

    def backtrack(path, used):
        if len(path) == n:
            result.append(path[:])
            return
        for i in range(n):
            if not used[i]:
                used[i] = True
                path.append(a[i])
                backtrack(path, used)
                path.pop()
                used[i] = False

    backtrack([], [False]*n)
    for p in result:
        print(*p)


# ════════════════════════════════════════════════════
# EXERCISE 2: N-Queens
# ════════════════════════════════════════════════════
def exercise2_nqueens():
    n = int(input())
    count = [0]

    def backtrack(row, cols, diag1, diag2):
        if row == n:
            count[0] += 1
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            cols.add(col); diag1.add(row-col); diag2.add(row+col)
            backtrack(row+1, cols, diag1, diag2)
            cols.remove(col); diag1.remove(row-col); diag2.remove(row+col)

    backtrack(0, set(), set(), set())
    print(count[0])


# ════════════════════════════════════════════════════
# EXERCISE 3: Subsets (Power Set)
# ════════════════════════════════════════════════════
def exercise3_subsets():
    n = int(input())
    a = list(map(int, input().split()))
    result = []

    def backtrack(idx, path):
        result.append(path[:])
        for i in range(idx, n):
            path.append(a[i])
            backtrack(i+1, path)
            path.pop()

    backtrack(0, [])
    for s in result:
        print(*s) if s else print("empty")


# ════════════════════════════════════════════════════
# EXERCISE 4: Generate Balanced Parentheses
# ════════════════════════════════════════════════════
def exercise4_parentheses():
    n = int(input())  # n pairs of parentheses
    result = []

    def backtrack(s, open_cnt, close_cnt):
        if len(s) == 2 * n:
            result.append(s)
            return
        if open_cnt < n:
            backtrack(s + '(', open_cnt+1, close_cnt)
        if close_cnt < open_cnt:
            backtrack(s + ')', open_cnt, close_cnt+1)

    backtrack('', 0, 0)
    for s in result:
        print(s)


# ════════════════════════════════════════════════════
# EXERCISE 5: Sum Combination (Subset Sum)
# ════════════════════════════════════════════════════
def exercise5_subset_sum():
    n, target = map(int, input().split())
    a = list(map(int, input().split()))
    found = [False]

    def backtrack(idx, remaining):
        if remaining == 0:
            found[0] = True
            return
        if remaining < 0 or idx == n:
            return
        backtrack(idx+1, remaining - a[idx])  # include a[idx]
        backtrack(idx+1, remaining)            # exclude a[idx]

    backtrack(0, target)
    print("YES" if found[0] else "NO")


def main():
    exercise2_nqueens()


if __name__ == "__main__":
    main()
