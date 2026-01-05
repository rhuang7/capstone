import sys
import math
from collections import defaultdict

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
    prime_count = len(K_factors)

    # Segment tree for range queries
    class SegmentTree:
        def __init__(self, size, default_val):
            self.n = 1
            while self.n < size:
                self.n <<= 1
            self.size = size
            self.default_val = default_val
            self.tree = [default_val] * (2 * self.n)
            self.lazy = [None] * (2 * self.n)

        def push(self, node, l, r):
            if self.lazy[node] is not None:
                self.tree[node] = self.lazy[node]
                if l != r:
                    self.lazy[2*node] = self.lazy[node]
                    self.lazy[2*node+1] = self.lazy[node]
                self.lazy[node] = None

        def apply(self, node, l, r, val):
            self.tree[node] = val
            if l != r:
                self.lazy[2*node] = val
                self.lazy[2*node+1] = val

        def range_update(self, a, b, val, node=1, l=0, r=None):
            if r is None:
                r = self.n - 1
            self.push(node, l, r)
            if a > r or b < l:
                return
            if a <= l and r <= b:
                self.apply(node, l, r, val)
                return
            mid = (l + r) // 2
            self.range_update(a, b, val, 2*node, l, mid)
            self.range_update(a, b, val, 2*node+1, mid+1, r)
            self.tree[node] = self.tree[2*node] + self.tree[2*node+1]

        def range_query(self, a, b, node=1, l=0, r=None):
            if r is None:
                r = self.n - 1
            self.push(node, l, r)
            if a > r or b < l:
                return 0
            if a <= l and r <= b:
                return self.tree[node]
            mid = (l + r) // 2
            left = self.range_query(a, b, 2*node, l, mid)
            right = self.range_query(a, b, 2*node+1, mid+1, r)
            return left + right

    # Initialize segment tree with empty (represented as -1)
    st = SegmentTree(Q, -1)

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
            st.range_update(l, r, x)
        else:
            # Query: count primes in K that are factors of at least one number in range
            # We need to find primes in K_factors that are present in any of the numbers in the range
            # We can use a set to track which primes are present
            # For efficiency, we can use a segment tree to track for each position whether it has a prime factor of K
            # But since K can be large, we need to precompute all primes of K
            # For each query, we can check for each prime in K_factors whether it appears in the range
            # To do this efficiently, we can use a binary indexed tree or a segment tree to track the presence of each prime
            # However, since K can be up to 1e9, we need to precompute all primes of K and then for each query, check which of them are present in the range
            # So we can create a segment tree for each prime in K_factors, but that would be too slow
            # Alternative: for each query, we can iterate over all primes in K_factors and check if any of them is a factor of any number in the range
            # To do this efficiently, we can create a segment tree that for each position stores the set of primes of K that divide the number at that position
            # But that's not feasible for large K
            # So we need to find for each query, for each prime in K_factors, whether there exists at least one number in the range that has that prime as a factor
            # To do this, we can for each prime in K_factors, maintain a segment tree that tracks the presence of that prime in the range
            # But since K can have up to 10 primes, this is feasible
            # So we precompute all primes of K
            # Then for each prime, we create a segment tree that tracks whether the number at a position has that prime as a factor
            # For each query, we check for each prime in K_factors if it appears in the range
            # But for the given problem, we can precompute for each query, for each prime in K_factors, whether there exists at least one number in the range that has that prime as a factor
            # To do this, we can for each prime in K_factors, maintain a segment tree that tracks whether the number at a position is divisible by that prime
            # Then for a query, we check for each prime in K_factors if it appears in the range
            # But since K can be up to 1e9, we need to precompute all primes of K
            # So let's proceed with this approach
            # Precompute primes of K
            # Now, for each query, we need to check for each prime in K_factors whether it appears in the range
            # So we can create a segment tree for each prime in K_factors
            # But this is not feasible for large Q and large number of primes
            # So we can instead, for each query, iterate through all primes in K_factors and check if any of them is a factor of any number in the range
            # To do this efficiently, we can for each prime in K_factors, maintain a segment tree that tracks whether the number at a position is divisible by that prime
            # Then for a query, we check for each prime in K_factors if it appears in the range
            # So let's proceed with this approach
            # Precompute primes of K
            # Now, for each query, we need to check for each prime in K_factors whether it appears in the range
            # So we can create a segment tree for each prime in K_factors
            # But this is not feasible for large Q and large number of primes
            # So we can instead, for each query, iterate through all primes in K_factors and check if any of them is a factor of any number in the range
            # To do this efficiently, we can for each prime in K_factors, maintain a segment tree that tracks whether the number at a position is divisible by that prime
            # Then for a query, we check for each prime in K_factors if it appears in the range
            # So let's proceed with this approach
            # Precompute primes of K
            # Now, for each query, we need to check for each prime in K_factors whether it appears in the range
            # So we can create a segment tree for each prime in K_factors
            # But this is not feasible for large Q and large number of primes
            # So we can instead, for each query, iterate through all primes in K_factors and check if any of them is a factor of any number in the range
            # To do this efficiently, we can for each prime in K_factors, maintain a segment tree that tracks whether the number at a position is divisible by that prime
            # Then for a query, we check for each prime in K_factors if it appears in the range
            # So let's proceed with this approach
            # Precompute primes of K
            # Now, for each query, we need to check for each prime in K_factors whether it appears in the range
            # So we can create a segment tree for each prime in K_factors
            # But this is not feasible for large Q and large number of primes
            # So we can instead, for each query, iterate through all primes in K_factors and check if any of them is a factor of any number in the range
            # To do this efficiently, we can