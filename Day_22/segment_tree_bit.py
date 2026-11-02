"""
Day 22 — Segment Tree & Fenwick Tree (BIT)
"""
import sys
input = sys.stdin.readline


# ════════════════════════════════════════════════════
# SEGMENT TREE (point update, range query)
# ════════════════════════════════════════════════════
class SegTree:
    def __init__(self, n, func=max, default=0):
        self.n = n
        self.func = func
        self.default = default
        self.tree = [default] * (2 * n)

    def build(self, arr):
        for i, v in enumerate(arr):
            self.tree[i + self.n] = v
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.func(self.tree[2*i], self.tree[2*i+1])

    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i >>= 1
            self.tree[i] = self.func(self.tree[2*i], self.tree[2*i+1])

    def query(self, l, r):  # [l, r) half-open
        res = self.default
        l += self.n; r += self.n
        while l < r:
            if l & 1: res = self.func(res, self.tree[l]); l += 1
            if r & 1: r -= 1; res = self.func(res, self.tree[r])
            l >>= 1; r >>= 1
        return res


# ════════════════════════════════════════════════════
# SEGMENT TREE WITH LAZY PROPAGATION (range update)
# ════════════════════════════════════════════════════
class LazySegTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def _push_down(self, node, l, r):
        if self.lazy[node]:
            mid = (l + r) // 2
            self.tree[2*node] += self.lazy[node] * (mid - l + 1)
            self.tree[2*node+1] += self.lazy[node] * (r - mid)
            self.lazy[2*node] += self.lazy[node]
            self.lazy[2*node+1] += self.lazy[node]
            self.lazy[node] = 0

    def update_range(self, node, l, r, ql, qr, val):
        if qr < l or r < ql: return
        if ql <= l and r <= qr:
            self.tree[node] += val * (r - l + 1)
            self.lazy[node] += val
            return
        self._push_down(node, l, r)
        mid = (l + r) // 2
        self.update_range(2*node, l, mid, ql, qr, val)
        self.update_range(2*node+1, mid+1, r, ql, qr, val)
        self.tree[node] = self.tree[2*node] + self.tree[2*node+1]

    def query_range(self, node, l, r, ql, qr):
        if qr < l or r < ql: return 0
        if ql <= l and r <= qr: return self.tree[node]
        self._push_down(node, l, r)
        mid = (l + r) // 2
        return (self.query_range(2*node, l, mid, ql, qr) +
                self.query_range(2*node+1, mid+1, r, ql, qr))


# ════════════════════════════════════════════════════
# FENWICK TREE / BIT (Binary Indexed Tree)
# Point update + prefix sum query — simpler & faster
# ════════════════════════════════════════════════════
class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, delta):  # 1-indexed
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):  # prefix sum [1..i]
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

    def range_query(self, l, r):  # [l, r] 1-indexed
        return self.query(r) - self.query(l - 1)


# ════════════════════════════════════════════════════
# EXERCISES
# ════════════════════════════════════════════════════

def exercise1_range_max():
    """Segment tree: point update + range max queries"""
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    st = SegTree(n, func=max, default=0)
    st.build(a)
    for _ in range(q):
        line = input().split()
        if line[0] == 'U':
            i, v = int(line[1])-1, int(line[2])
            st.update(i, v)
        else:
            l, r = int(line[1])-1, int(line[2])
            print(st.query(l, r))


def exercise2_bit_prefix():
    """BIT: point updates + prefix sum queries"""
    n = int(input())
    a = list(map(int, input().split()))
    bit = BIT(n)
    for i, v in enumerate(a):
        bit.update(i+1, v)

    q = int(input())
    for _ in range(q):
        line = input().split()
        if line[0] == 'U':
            i, v = int(line[1]), int(line[2])
            bit.update(i, v - a[i-1])  # delta update
            a[i-1] = v
        else:
            l, r = int(line[1]), int(line[2])
            print(bit.range_query(l, r))


def exercise3_count_inversions():
    """Count inversions using BIT"""
    n = int(input())
    a = list(map(int, input().split()))
    # Coordinate compress
    sorted_a = sorted(set(a))
    rank = {v: i+1 for i, v in enumerate(sorted_a)}

    bit = BIT(len(sorted_a))
    inversions = 0
    for x in a:
        r = rank[x]
        inversions += bit.query(len(sorted_a)) - bit.query(r)
        bit.update(r, 1)
    print(inversions)


def main():
    exercise3_count_inversions()


if __name__ == "__main__":
    main()
