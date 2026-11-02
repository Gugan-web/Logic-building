"""
Day 01 — Fast I/O & All Input/Output Patterns
Run: python solution.py < input.txt
"""

import sys
input = sys.stdin.readline   # ALWAYS override this!


# ════════════════════════════════════════════════════
# PATTERN 1: Single value
# ════════════════════════════════════════════════════
def pattern_single():
    n = int(input())
    print(n * 2)


# ════════════════════════════════════════════════════
# PATTERN 2: Two integers on one line
# ════════════════════════════════════════════════════
def pattern_two_ints():
    a, b = map(int, input().split())
    print(a + b)


# ════════════════════════════════════════════════════
# PATTERN 3: n integers as a list
# ════════════════════════════════════════════════════
def pattern_list():
    n = int(input())
    a = list(map(int, input().split()))
    print(sum(a))


# ════════════════════════════════════════════════════
# PATTERN 4: Multiple test cases
# ════════════════════════════════════════════════════
def pattern_multitest():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        results.append(str(sum(a)))
    print('\n'.join(results))   # batch output = faster


# ════════════════════════════════════════════════════
# PATTERN 5: Read entire input at once (FASTEST)
# ════════════════════════════════════════════════════
def pattern_bulk_read():
    data = sys.stdin.read().split()
    idx = 0

    def rd():
        nonlocal idx
        idx += 1
        return data[idx - 1]

    t = int(rd())
    for _ in range(t):
        n = int(rd())
        a = [int(rd()) for _ in range(n)]
        print(sum(a))


# ════════════════════════════════════════════════════
# PATTERN 6: 2D Grid input
# ════════════════════════════════════════════════════
def pattern_grid():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    # Print row sums
    for row in grid:
        print(sum(row))


# ════════════════════════════════════════════════════
# PATTERN 7: Character grid
# ════════════════════════════════════════════════════
def pattern_char_grid():
    n = int(input())
    grid = [input().strip() for _ in range(n)]
    # Count '#' characters
    count = sum(row.count('#') for row in grid)
    print(count)


# ════════════════════════════════════════════════════
# PATTERN 8: YES / NO output
# ════════════════════════════════════════════════════
def pattern_yesno():
    a, b = map(int, input().split())
    print("YES" if a > b else "NO")


# ════════════════════════════════════════════════════
# PATTERN 9: Float output with precision
# ════════════════════════════════════════════════════
def pattern_float():
    a, b = map(float, input().split())
    print(f"{a / b:.9f}")


# ════════════════════════════════════════════════════
# EXERCISE SOLUTIONS
# ════════════════════════════════════════════════════

def exercise1():
    """Read a, b → print sum"""
    a, b = map(int, input().split())
    print(a + b)


def exercise2():
    """t test cases, each: n numbers → print sum"""
    t = int(input())
    out = []
    for _ in range(t):
        a = list(map(int, input().split()))
        out.append(str(sum(a)))
    sys.stdout.write('\n'.join(out) + '\n')


def exercise3():
    """3x3 grid → print row sums"""
    grid = [list(map(int, input().split())) for _ in range(3)]
    for row in grid:
        print(sum(row))


def main():
    exercise1()
    # exercise2()
    # exercise3()
    # pattern_grid()


if __name__ == "__main__":
    main()
