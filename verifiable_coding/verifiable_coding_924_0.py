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
    num_primes = len(K_factors)

    # Initialize segment tree
    class SegmentTree:
        def __init__(self, size):
            self.N = 1
            while self.N < size:
                self.N <<= 1
            self.tree = [set() for _ in range(2 * self.N)]
        
        def update(self, l, r, x, node, node_l, node_r):
            if r < node_l or l > node_r:
                return
            if l <= node_l and node_r <= r:
                self.tree[node].add(x)
                return
            mid = (node_l + node_r) // 2
            self.update(l, r, x, 2 * node, node_l, mid)
            self.update(l, r, x, 2 * node + 1, mid + 1, node_r)
            self.tree[node] = self.tree[2 * node] | self.tree[2 * node + 1]
        
        def query(self, l, r, node, node_l, node_r):
            if r < node_l or l > node_r:
                return set()
            if l <= node_l and node_r <= r:
                return self.tree[node]
            mid = (node_l + node_r) // 2
            left = self.query(l, r, 2 * node, node_l, mid)
            right = self.query(l, r, 2 * node + 1, mid + 1, node_r)
            return left | right

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
            st.update(l, r, x, 1, 1, st.N)
        else:
            res = st.query(l, r, 1, 1, st.N)
            count = 0
            for p in K_factors:
                if p in res:
                    count += 1
            print(count)

if __name__ == '__main__':
    solve()