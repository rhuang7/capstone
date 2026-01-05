import sys
import math
from collections import defaultdict, deque

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
        
        def update(self, pos, value):
            pos += self.n
            self.tree[pos].add(value)
            pos >>= 1
            while pos >= 1:
                self.tree[pos] = self.tree[2 * pos] | self.tree[2 * pos + 1]
                pos >>= 1
        
        def query(self, l, r):
            res = set()
            l += self.n
            r += self.n
            while l <= r:
                if l % 2 == 1:
                    res |= self.tree[l]
                    l += 1
                if r % 2 == 0:
                    res |= self.tree[r]
                    r -= 1
                l >>= 1
                r >>= 1
            return res

    st = SegmentTree(10**5 + 2)

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
            for i in range(l, r + 1):
                st.update(i, x)
        else:
            primes_in_range = st.query(l, r)
            count = 0
            for p in K_factors:
                if p in primes_in_range:
                    count += 1
            print(count)

if __name__ == '__main__':
    solve()