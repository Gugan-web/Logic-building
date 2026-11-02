"""
Day 29 — Master Templates & Problem-Solving Patterns
All reusable code for competitive programming in one place
"""
import sys
import heapq
from math import gcd, lcm, isqrt, comb
from collections import defaultdict, Counter, deque
from itertools import accumulate
from bisect import bisect_left, bisect_right
from functools import lru_cache

input = sys.stdin.readline
sys.setrecursionlimit(300000)

MOD  = 10**9 + 7
MOD2 = 998244353
INF  = float('inf')


# ═══════════════════════════════════════════════════════════
# SECTION 1: FAST I/O
# ═══════════════════════════════════════════════════════════
def inp():   return int(input())
def inpl():  return list(map(int, input().split()))
def inps():  return input().strip()


# ═══════════════════════════════════════════════════════════
# SECTION 2: MATH UTILITIES
# ═══════════════════════════════════════════════════════════
def power(base, exp, mod=MOD): return pow(base, exp, mod)
def modinv(a, mod=MOD):        return pow(a, mod-2, mod)

def ext_gcd(a, b):
    if not a: return b, 0, 1
    g, x, y = ext_gcd(b%a, a)
    return g, y-(b//a)*x, x

def sieve(n):
    """Returns list of primes up to n"""
    is_p = bytearray([1])*(n+1)
    is_p[0] = is_p[1] = 0
    for i in range(2, isqrt(n)+1):
        if is_p[i]: is_p[i*i::i] = bytearray(len(is_p[i*i::i]))
    return [i for i in range(n+1) if is_p[i]]

def factorize(n):
    """Prime factorization: {prime: exponent}"""
    f = {}
    d = 2
    while d*d <= n:
        while n%d == 0:
            f[d] = f.get(d,0)+1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n,0)+1
    return f


# ═══════════════════════════════════════════════════════════
# SECTION 3: COMBINATORICS
# ═══════════════════════════════════════════════════════════
class Combo:
    def __init__(self, maxn, mod=MOD):
        self.mod = mod
        self.f  = [1]*(maxn+1)
        self.fi = [1]*(maxn+1)
        for i in range(1, maxn+1): self.f[i]  = self.f[i-1]*i%mod
        self.fi[maxn] = pow(self.f[maxn], mod-2, mod)
        for i in range(maxn-1,-1,-1): self.fi[i] = self.fi[i+1]*(i+1)%mod
    def C(self, n, r):
        if r<0 or r>n: return 0
        return self.f[n]*self.fi[r]%self.mod*self.fi[n-r]%self.mod
    def P(self, n, r):
        if r<0 or r>n: return 0
        return self.f[n]*self.fi[n-r]%self.mod


# ═══════════════════════════════════════════════════════════
# SECTION 4: DSU
# ═══════════════════════════════════════════════════════════
class DSU:
    def __init__(self, n):
        self.p = list(range(n)); self.sz = [1]*n; self.comp = n
    def find(self, x):
        while self.p[x]!=x: self.p[x]=self.p[self.p[x]]; x=self.p[x]
        return x
    def union(self, x, y):
        x,y = self.find(x), self.find(y)
        if x==y: return False
        if self.sz[x]<self.sz[y]: x,y=y,x
        self.p[y]=x; self.sz[x]+=self.sz[y]; self.comp-=1; return True
    def same(self, x, y): return self.find(x)==self.find(y)
    def size(self, x):    return self.sz[self.find(x)]


# ═══════════════════════════════════════════════════════════
# SECTION 5: SEGMENT TREE
# ═══════════════════════════════════════════════════════════
class SegTree:
    def __init__(self, n, func=max, default=0):
        self.n=n; self.f=func; self.d=default
        self.t=[default]*(2*n)
    def build(self, a):
        for i,v in enumerate(a): self.t[i+self.n]=v
        for i in range(self.n-1,0,-1): self.t[i]=self.f(self.t[2*i],self.t[2*i+1])
    def update(self, i, v):
        i+=self.n; self.t[i]=v
        while i>1: i>>=1; self.t[i]=self.f(self.t[2*i],self.t[2*i+1])
    def query(self, l, r):   # [l,r)
        res=self.d; l+=self.n; r+=self.n
        while l<r:
            if l&1: res=self.f(res,self.t[l]); l+=1
            if r&1: r-=1; res=self.f(res,self.t[r])
            l>>=1; r>>=1
        return res


# ═══════════════════════════════════════════════════════════
# SECTION 6: BIT / FENWICK TREE
# ═══════════════════════════════════════════════════════════
class BIT:
    def __init__(self, n): self.n=n; self.t=[0]*(n+1)
    def update(self, i, d):
        while i<=self.n: self.t[i]+=d; i+=i&(-i)
    def query(self, i):
        s=0
        while i>0: s+=self.t[i]; i-=i&(-i)
        return s
    def range(self, l, r): return self.query(r)-self.query(l-1)


# ═══════════════════════════════════════════════════════════
# SECTION 7: GRAPH ALGORITHMS
# ═══════════════════════════════════════════════════════════
def dijkstra(graph, src, n):
    dist=[INF]*(n+1); dist[src]=0; h=[(0,src)]
    while h:
        d,u=heapq.heappop(h)
        if d>dist[u]: continue
        for v,w in graph[u]:
            if dist[u]+w<dist[v]: dist[v]=dist[u]+w; heapq.heappush(h,(dist[v],v))
    return dist

def bfs(graph, src, n):
    dist=[-1]*(n+1); dist[src]=0; q=deque([src])
    while q:
        u=q.popleft()
        for v in graph[u]:
            if dist[v]==-1: dist[v]=dist[u]+1; q.append(v)
    return dist

def topo_sort(graph, n):
    ind=[0]*(n+1)
    for u in range(1,n+1):
        for v in graph[u]: ind[v]+=1
    q=deque([u for u in range(1,n+1) if not ind[u]]); order=[]
    while q:
        u=q.popleft(); order.append(u)
        for v in graph[u]:
            ind[v]-=1
            if not ind[v]: q.append(v)
    return order if len(order)==n else None


# ═══════════════════════════════════════════════════════════
# SECTION 8: STRING ALGORITHMS
# ═══════════════════════════════════════════════════════════
def z_function(s):
    n=len(s); z=[0]*n; l=r=0
    for i in range(1,n):
        if i<r: z[i]=min(r-i,z[i-l])
        while i+z[i]<n and s[z[i]]==s[i+z[i]]: z[i]+=1
        if i+z[i]>r: l,r=i,i+z[i]
    return z

def kmp_search(text, pattern):
    if not pattern: return []
    c=pattern+'#'+text; z=z_function(c); m=len(pattern)
    return [i-m-1 for i in range(m+1,len(c)) if z[i]==m]


# ═══════════════════════════════════════════════════════════
# SECTION 9: BINARY SEARCH HELPERS
# ═══════════════════════════════════════════════════════════
def bs_min(lo, hi, feasible):
    """Minimum x in [lo,hi] where feasible(x) is True"""
    res=hi
    while lo<=hi:
        mid=(lo+hi)//2
        if feasible(mid): res=mid; hi=mid-1
        else: lo=mid+1
    return res

def bs_max(lo, hi, feasible):
    """Maximum x in [lo,hi] where feasible(x) is True"""
    res=lo
    while lo<=hi:
        mid=(lo+hi)//2
        if feasible(mid): res=mid; lo=mid+1
        else: hi=mid-1
    return res


# ═══════════════════════════════════════════════════════════
# SECTION 10: PROBLEM PATTERNS CHEAT SHEET
# ═══════════════════════════════════════════════════════════
"""
PATTERN RECOGNITION:

Count subarrays with sum = k         → prefix sum + dict
Range queries (static)               → prefix sum
Range queries (update + query)       → Segment Tree / BIT
Connectivity queries                 → DSU
Shortest path (unweighted)           → BFS
Shortest path (weighted, no neg)     → Dijkstra
Minimum spanning tree                → Kruskal (DSU) or Prim
Order of tasks with dependencies     → Topological Sort
All pairs shortest path              → Floyd-Warshall O(V^3)
Find pattern in string               → Z-function / KMP
Minimize maximum / Maximize minimum  → Binary Search on Answer
Overlapping subproblems              → Dynamic Programming
Local optimum → Global optimum       → Greedy
"""


def solve():
    pass   # Write solution using templates above


def main():
    t = 1
    # t = inp()
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
