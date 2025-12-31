import sys
import math
from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0

    N = int(data[idx])
    idx += 1

    A = list(map(int, data[idx:idx+N]))
    idx += N

    Q = int(data[idx])
    idx += 1

    queries = []
    for _ in range(Q):
        k = int(data[idx])
        if k == 1:
            l = int(data[idx+1])
            r = int(data[idx+2])
            queries.append((k, l, r))
            idx += 3
        else:
            i = int(data[idx+1])
            val = int(data[idx+2])
            queries.append((k, i, val))
            idx += 3

    # Precompute primes up to 100
    primes = list(range(2, 101))
    prime_factors = [{} for _ in range(101)]
    for p in primes:
        for multiple in range(p, 101, p):
            prime_factors[multiple][p] = 1

    # Function to get prime factors of a number
    def get_prime_factors(x):
        factors = {}
        for p in primes:
            if x == 1:
                break
            if p > x:
                break
            if x % p == 0:
                count = 0
                while x % p == 0:
                    x //= p
                    count += 1
                factors[p] = count
        return factors

    # Initialize prime counts for each element
    prime_counts = [defaultdict(int) for _ in range(N)]
    for i in range(N):
        factors = get_prime_factors(A[i])
        for p, cnt in factors.items():
            prime_counts[i][p] = cnt

    # Segment tree for range queries
    class SegmentTree:
        def __init__(self, data):
            self.n = len(data)
            self.size = 1
            while self.size < self.n:
                self.size <<= 1
            self.tree = [defaultdict(int) for _ in range(2 * self.size)]
            # Fill leaves
            for i in range(self.n):
                for p, cnt in data[i].items():
                    self.tree[self.size + i][p] = cnt
            # Build the tree
            for i in range(self.size - 1, 0, -1):
                for p in self.tree[2 * i]:
                    self.tree[i][p] += self.tree[2 * i][p]
                for p in self.tree[2 * i + 1]:
                    self.tree[i][p] += self.tree[2 * i + 1][p]

        def update(self, pos, new_factors):
            pos += self.size
            for p, cnt in new_factors.items():
                self.tree[pos][p] = cnt
            pos >>= 1
            while pos >= 1:
                for p in self.tree[2 * pos]:
                    self.tree[pos][p] += self.tree[2 * pos][p]
                for p in self.tree[2 * pos + 1]:
                    self.tree[pos][p] += self.tree[2 * pos + 1][p]
                pos >>= 1

        def query(self, l, r):
            l += self.size
            r += self.size
            res = defaultdict(int)
            while l <= r:
                if l % 2 == 1:
                    for p, cnt in self.tree[l].items():
                        res[p] += cnt
                    l += 1
                if r % 2 == 0:
                    for p, cnt in self.tree[r].items():
                        res[p] += cnt
                    r -= 1
                l >>= 1
                r >>= 1
            return res

    # Build the segment tree
    st = SegmentTree(prime_counts)

    # Process queries
    output = []
    for query in queries:
        if query[0] == 1:
            l = query[1] - 1
            r = query[2] - 1
            factors = st.query(l, r)
            is_square = True
            for p in factors:
                if factors[p] % 2 != 0:
                    is_square = False
                    break
            output.append("YES" if is_square else "NO")
        else:
            i = query[1] - 1
            val = query[2]
            # Update the value at index i
            old_val = A[i]
            new_val = old_val * val
            A[i] = new_val
            # Get prime factors of new_val
            new_factors = get_prime_factors(new_val)
            # Update the segment tree
            st.update(i, new_factors)

    print("\n".join(output))