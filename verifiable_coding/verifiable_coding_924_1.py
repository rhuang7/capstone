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
        def __init__(self, size, default_val):
            self.n = 1
            while self.n < size:
                self.n <<= 1
            self.size = self.n
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
            self.tree[node] = self.tree[2*node] + self.tree[2*node+1]

        def query_range(self, a, b, node=1, l=0, r=None):
            if r is None:
                r = self.n - 1
            self.push(node, l, r)
            if a > r or b < l:
                return 0
            if a <= l and r <= b:
                return self.tree[node]
            mid = (l + r) // 2
            left = self.query_range(a, b, 2*node, l, mid)
            right = self.query_range(a, b, 2*node+1, mid+1, r)
            return left + right

    # Initialize segment tree with empty values (represented by -1)
    # We'll use -1 to represent empty, and the actual prime factors as 1s
    # For each position, we'll store a set of prime factors of the value in that position
    # But since we only need to know if a prime factor of K is present in any position in a range,
    # we can use a binary array where 1 means the prime factor is present in that position
    # We'll use a segment tree that stores for each position whether a prime factor of K is present
    # and supports range updates and range queries

    # First, get all prime factors of K
    K_factors = get_prime_factors(K)
    prime_to_index = {p: i for i, p in enumerate(K_factors)}
    num_primes = len(K_factors)

    # For each position, we'll store a bitmask of which primes of K are present
    # But since we need to check for presence, we can use a binary array where 1 means the prime is present
    # We'll use a segment tree that stores for each position whether a prime factor of K is present
    # and supports range updates and range queries

    # Create a segment tree that stores for each position a set of primes of K that are present
    # But since we need to check for presence, we can use a binary array where 1 means the prime is present
    # We'll use a segment tree that stores for each position a bitmask of which primes of K are present
    # But since the number of primes is up to 10 (since K is up to 1e9), we can use a bitmask of 10 bits
    # So for each position, we'll store a bitmask of which primes of K are present
    # We'll use a segment tree that stores for each position a bitmask of which primes of K are present
    # and supports range updates and range queries

    # For the segment tree, each node will store a bitmask of primes of K that are present in its range
    # Initially, all positions are empty, so the bitmask is 0
    # When a range is filled with x, we get the prime factors of x and set the corresponding bits in the bitmask
    # For each query, we need to find the number of primes of K that are present in at least one position in the range
    # This is equivalent to the number of set bits in the OR of the bitmasks in the range

    # So we'll use a segment tree that stores for each position a bitmask of primes of K that are present
    # and supports range updates and range queries

    # But since the number of primes is small (up to 10), we can use a segment tree that stores for each position a bitmask of primes of K that are present
    # and supports range updates and range queries

    # So the segment tree will store for each position a bitmask of primes of K that are present
    # Initially, all positions are empty, so the bitmask is 0
    # When a range is filled with x, we get the prime factors of x and set the corresponding bits in the bitmask
    # For each query, we need to find the number of primes of K that are present in at least one position in the range
    # This is equivalent to the number of set bits in the OR of the bitmasks in the range

    # So we'll use a segment tree that stores for each position a bitmask of primes of K that are present
    # and supports range updates and range queries

    # So the segment tree will store for each position a bitmask of primes of K that are present
    # Initially, all positions are empty, so the bitmask is 0
    # When a range is filled with x, we get the prime factors of x and set the corresponding bits in the bitmask
    # For each query, we need to find the number of primes of K that are present in at least one position in the range
    # This is equivalent to the number of set bits in the OR of the bitmasks in the range

    # So the segment tree will store for each position a bitmask of primes of K that are present
    # and supports range updates and range queries

    # So the segment tree will store for each position a bitmask of primes of K that are present
    # Initially, all positions are empty, so the bitmask is 0
    # When a range is filled with x, we get the prime factors of x and set the corresponding bits in the bitmask
    # For each query, we need to find the number of primes of K that are present in at least one position in the range
    # This is equivalent to the number of set bits in the OR of the bitmasks in the range

    # So the segment tree will store for each position a bitmask of primes of K that are present
    # and supports range updates and range queries

    # Now, we can proceed to implement the segment tree

    # First, get all prime factors of K
    K_factors = get_prime_factors(K)
    prime_to_index = {p: i for i, p in enumerate(K_factors)}
    num_primes = len(K_factors)

    # Create a segment tree that stores for each position a bitmask of primes of K that are present
    # Initially, all positions are empty, so the bitmask is 0
    # The segment tree will be of size 1e5 + 2 (since r can be up to 1e5)
    # But since the array is infinite, we can use a segment tree with size 1e5 + 2
    # However, for queries with r up to 1e5, we can use a segment tree of size 1e5 + 2

    # But since the queries can have l and r up to 1e5, we can use a segment tree of size 1e5 + 2