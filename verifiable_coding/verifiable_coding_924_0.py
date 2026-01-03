import sys
import math
from collections import defaultdict, deque

def get_prime_factors(n):
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    i = 3
    max_factor = math.isqrt(n) + 1
    while i <= max_factor and n > 1:
        while n % i == 0:
            factors.add(i)
            n //= i
            max_factor = math.isqrt(n) + 1
        i += 2
    if n > 1:
        factors.add(n)
    return factors

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    K = int(data[idx])
    idx += 1
    Q = int(data[idx])
    idx += 1

    K_factors = get_prime_factors(K)
    prime_to_index = {p: i for i, p in enumerate(K_factors)}
    num_primes = len(K_factors)

    # Segment tree for range queries
    class SegmentTree:
        def __init__(self, size):
            self.n = 1
            while self.n < size:
                self.n <<= 1
            self.size = self.n
            self.tree = [set() for _ in range(2 * self.n)]
            self.lazy = [None] * (2 * self.n)

        def push(self, node, l, r):
            if self.lazy[node] is not None:
                self.tree[node] = self.tree[node].union(self.lazy[node])
                if l != r:
                    self.lazy[2*node] = self.lazy[node].copy()
                    self.lazy[2*node+1] = self.lazy[node].copy()
                self.lazy[node] = None

        def apply(self, node, l, r, val):
            self.tree[node].add(val)
            if l != r:
                self.lazy[2*node] = self.lazy[2*node].copy() if self.lazy[2*node] is not None else set()
                self.lazy[2*node].add(val)
                self.lazy[2*node+1] = self.lazy[2*node+1].copy() if self.lazy[2*node+1] is not None else set()
                self.lazy[2*node+1].add(val)

        def update_range(self, a, b, val, node=1, l=0, r=None):
            if r is None:
                r = self.n - 1
            self.push(node, l, r)
            if a > r or b < l:
                return
            if a <= l and r <= b:
                self.apply(node, l, r, val)
                return
            mid = (l + r) // 2
            self.update_range(a, b, val, 2*node, l, mid)
            self.update_range(a, b, val, 2*node+1, mid+1, r)
            self.tree[node] = self.tree[2*node].union(self.tree[2*node+1])

        def query_range(self, a, b, node=1, l=0, r=None):
            if r is None:
                r = self.n - 1
            self.push(node, l, r)
            if a > r or b < l:
                return set()
            if a <= l and r <= b:
                return self.tree[node]
            mid = (l + r) // 2
            left = self.query_range(a, b, 2*node, l, mid)
            right = self.query_range(a, b, 2*node+1, mid+1, r)
            return left.union(right)

    st = SegmentTree(10**5 + 2)

    for _ in range(Q):
        query_type = data[idx]
        idx += 1
        l = int(data[idx]) - 1
        idx += 1
        r = int(data[idx]) - 1
        idx += 1
        if query_type == '!':
            x = int(data[idx])
            idx += 1
            st.update_range(l, r, x)
        else:
            primes_in_range = st.query_range(l, r)
            result = 0
            for p in K_factors:
                if p in primes_in_range:
                    result += 1
            print(result)