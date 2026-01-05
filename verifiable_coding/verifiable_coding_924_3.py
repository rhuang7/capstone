import sys
import math
from sys import stdin
from collections import defaultdict

def get_prime_factors(n):
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    i = 3
    max_factor = int(math.sqrt(n)) + 1
    while i <= max_factor and n > 1:
        while n % i == 0:
            factors.add(i)
            n //= i
            max_factor = int(math.sqrt(n)) + 1
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
    prime_set = set()
    for p in K_factors:
        prime_set.add(p)

    # For each query, we need to track which primes are present in the range
    # We'll use a segment tree to track the primes in ranges
    # But for efficiency, we can use a binary indexed tree (Fenwick Tree) for range updates and point queries
    # However, since we need range queries, we'll use a segment tree with lazy propagation

    class SegmentTree:
        def __init__(self, size):
            self.n = 1
            while self.n < size:
                self.n <<= 1
            self.tree = [set() for _ in range(2 * self.n)]
            self.lazy = [None for _ in range(2 * self.n)]

        def push(self, node, l, r):
            if self.lazy[node] is not None:
                self.tree[node] = self.lazy[node].copy()
                if l != r:
                    self.lazy[2 * node] = self.lazy[node].copy()
                    self.lazy[2 * node + 1] = self.lazy[node].copy()
                self.lazy[node] = None

        def update_range(self, a, b, val, node, l, r):
            self.push(node, l, r)
            if a > r or b < l:
                return
            if a <= l and r <= b:
                self.lazy[node] = val
                self.push(node, l, r)
                return
            mid = (l + r) // 2
            self.update_range(a, b, val, 2 * node, l, mid)
            self.update_range(a, b, val, 2 * node + 1, mid + 1, r)
            self.tree[node] = self.tree[2 * node].union(self.tree[2 * node + 1])

        def query_range(self, a, b, node, l, r):
            self.push(node, l, r)
            if a > r or b < l:
                return set()
            if a <= l and r <= b:
                return self.tree[node]
            mid = (l + r) // 2
            left = self.query_range(a, b, 2 * node, l, mid)
            right = self.query_range(a, b, 2 * node + 1, mid + 1, r)
            return left.union(right)

    max_size = 10**5 + 2
    st = SegmentTree(max_size)

    for _ in range(Q):
        query_type = data[idx]
        idx += 1
        l = int(data[idx])
        idx += 1
        r = int(data[idx])
        idx += 1
        if query_type == '!':
            x = int(data[idx])
            idx += 1
            # Get prime factors of x
            x_factors = get_prime_factors(x)
            st.update_range(l, r, x_factors, 1, 1, max_size)
        else:
            primes_in_range = st.query_range(l, r, 1, 1, max_size)
            count = 0
            for p in K_factors:
                if p in primes_in_range:
                    count += 1
            print(count)

if __name__ == '__main__':
    solve()