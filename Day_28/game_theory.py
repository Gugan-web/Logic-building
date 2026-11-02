"""
Day 28 — Game Theory: Nim & Sprague-Grundy
"""
import sys
input = sys.stdin.readline


# ════════════════════════════════════════════════════
# NIM GAME
# Multiple piles, players take any number from one pile
# First player wins iff XOR of all pile sizes != 0
# ════════════════════════════════════════════════════
def nim(piles):
    xor_sum = 0
    for p in piles:
        xor_sum ^= p
    return "First" if xor_sum != 0 else "Second"


# ════════════════════════════════════════════════════
# SPRAGUE-GRUNDY THEOREM
# Every impartial game position has a Grundy number (nimber)
# Grundy(pos) = mex({Grundy(next_pos) for all moves})
# Combined game Grundy = XOR of individual Grundy numbers
# ════════════════════════════════════════════════════
def mex(reachable):
    """Minimum Excludant: smallest non-negative integer not in set"""
    s = set(reachable)
    i = 0
    while i in s:
        i += 1
    return i


def compute_grundy(n, moves):
    """
    Compute Grundy values for positions 0..n
    moves: list of valid move sizes (e.g., [1, 3, 5] for Nim with those choices)
    """
    grundy = [0] * (n + 1)
    for i in range(1, n + 1):
        reachable = set()
        for m in moves:
            if i - m >= 0:
                reachable.add(grundy[i - m])
        grundy[i] = mex(reachable)
    return grundy


# ════════════════════════════════════════════════════
# EXERCISE 1: Basic Nim
# ════════════════════════════════════════════════════
def exercise1_nim():
    n = int(input())
    piles = list(map(int, input().split()))
    print(nim(piles))


# ════════════════════════════════════════════════════
# EXERCISE 2: Nim with Move Restrictions
# Can only take 1, 2, or 3 stones per turn
# ════════════════════════════════════════════════════
def exercise2_restricted_nim():
    n = int(input())
    piles = list(map(int, input().split()))
    moves = [1, 2, 3]
    max_pile = max(piles)
    grundy = compute_grundy(max_pile, moves)
    xor_sum = 0
    for p in piles:
        xor_sum ^= grundy[p]
    print("First" if xor_sum != 0 else "Second")


# ════════════════════════════════════════════════════
# EXERCISE 3: Staircase Nim
# Piles on stairs 0..n, move stones from stair i to stair i-1
# First player wins iff XOR of odd-indexed stairs != 0
# ════════════════════════════════════════════════════
def exercise3_staircase_nim():
    n = int(input())
    piles = list(map(int, input().split()))
    # Only odd-indexed stairs matter
    xor_sum = 0
    for i in range(1, n, 2):   # stairs 1, 3, 5, ...
        xor_sum ^= piles[i]
    print("First" if xor_sum != 0 else "Second")


# ════════════════════════════════════════════════════
# EXERCISE 4: Coin Row Game (DP-based game theory)
# Two players alternately pick from left or right end of row
# Both play optimally; who has higher score?
# ════════════════════════════════════════════════════
def exercise4_coin_row():
    n = int(input())
    coins = list(map(int, input().split()))

    # dp[i][j] = max coins first player can get from coins[i..j]
    dp = [[0]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = coins[i]

    for length in range(2, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            # Pick left or pick right
            # After first player picks, second player plays optimally on remaining
            pick_left  = coins[i] + (dp[i+2][j] if i+2<=j else 0)
            pick_right = coins[j] + (dp[i][j-2] if i<=j-2 else 0)
            dp[i][j] = max(pick_left, pick_right)

    first_score = dp[0][n-1]
    second_score = sum(coins) - first_score
    if first_score > second_score:
        print("First", first_score)
    elif second_score > first_score:
        print("Second", second_score)
    else:
        print("Tie", first_score)


def main():
    exercise1_nim()


if __name__ == "__main__":
    main()
