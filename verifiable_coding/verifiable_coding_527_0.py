import sys
import math
from collections import defaultdict

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    
    N = int(data[idx])
    idx += 1
    
    A = list(map(int, data[idx:idx+N]))
    idx += N
    
    Q = int(data[idx])
    idx += 1
    
    # Precompute primes up to 100
    primes = list(range(2, 101))
    
    # Function to get prime factors of a number
    def get_factors(x):
        factors = defaultdict(int)
        for p in primes:
            if p * p > x:
                break
            while x % p == 0:
                factors[p] += 1
                x //= p
        if x > 1:
            factors[x] += 1
        return factors
    
    # Initialize prime factor count for each element
    prime_counts = [defaultdict(int) for _ in range(N)]
    for i in range(N):
        prime_counts[i] = get_factors(A[i])
    
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
                self.tree[self.size + i] = data[i]
            # Build the tree
            for i in range(self.size - 1, 0, -1):
                for p in primes:
                    self.tree[i][p] = self.tree[2 * i][p] + self.tree[2 * i + 1][p]
        
        def update(self, pos, update):
            pos += self.size
            for p in primes:
                self.tree[pos][p] += update[p]
            pos >>= 1
            while pos >= 1:
                for p in primes:
                    self.tree[pos][p] = self.tree[2 * pos][p] + self.tree[2 * pos + 1][p]
                pos >>= 1
        
        def query(self, l, r):
            l += self.size
            r += self.size
            res = defaultdict(int)
            while l <= r:
                if l % 2 == 1:
                    for p in primes:
                        res[p] += self.tree[l][p]
                    l += 1
                if r % 2 == 0:
                    for p in primes:
                        res[p] += self.tree[r][p]
                    r -= 1
                l >>= 1
                r >>= 1
            return res
    
    st = SegmentTree(prime_counts)
    
    for _ in range(Q):
        k = int(data[idx])
        idx += 1
        if k == 1:
            l = int(data[idx]) - 1
            idx += 1
            r = int(data[idx]) - 1
            idx += 1
            factors = st.query(l, r)
            is_square = True
            for p in primes:
                if factors[p] % 2 != 0:
                    is_square = False
                    break
            print("YES" if is_square else "NO")
        else:
            i = int(data[idx]) - 1
            idx += 1
            val = int(data[idx])
            idx += 1
            # Update the value at position i
            old_factors = prime_counts[i]
            new_factors = get_factors(A[i] * val)
            # Compute the difference in factors
            diff = defaultdict(int)
            for p in primes:
                diff[p] = new_factors[p] - old_factors[p]
            st.update(i, diff)
            A[i] *= val

if __name__ == '__main__':
    solve()