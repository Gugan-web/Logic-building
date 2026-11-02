"""
Day 05 — Built-ins, Comprehensions & itertools
"""
import sys
from itertools import accumulate, permutations, combinations, product
from functools import reduce
input = sys.stdin.readline


def exercise1_min_pair_sum():
    n = int(input())
    a = sorted(map(int, input().split()))
    print(a[0] + a[1])   # two smallest elements


def exercise2_frequency():
    n = int(input())
    a = list(map(int, input().split()))
    freq = {}
    for x in a:
        freq[x] = freq.get(x, 0) + 1
    for k in sorted(freq):
        print(k, freq[k])


def exercise3_all_subsets():
    n = int(input())
    a = list(map(int, input().split()))
    # Generate all 2^n subsets
    for mask in range(1 << n):
        subset = [a[i] for i in range(n) if mask & (1 << i)]
        print(subset)


def exercise4_prefix_max():
    n = int(input())
    a = list(map(int, input().split()))
    prefix_max = list(accumulate(a, max))
    print(*prefix_max)


def demo_itertools():
    # Prefix sum using accumulate
    a = [1, 2, 3, 4, 5]
    print(list(accumulate(a)))          # [1,3,6,10,15]
    print(list(accumulate(a, max)))     # [1,2,3,4,5] prefix max
    print(list(accumulate(a, lambda a,b: a*b)))  # prefix product

    # All 2-element combinations
    print(list(combinations([1,2,3,4], 2)))

    # All orderings of [1,2,3]
    print(list(permutations([1,2,3])))

    # Cartesian product (like nested for loops)
    print(list(product([0,1], repeat=3)))  # all 3-bit combos


def main():
    exercise1_min_pair_sum()


if __name__ == "__main__":
    main()
