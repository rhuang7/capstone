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
    primes = []
    is_prime = [True] * 101
    is_prime[0] = is_prime[1] = False
    for i in range(2, 101):
        if is_prime[i]:
            primes.append(i)
            for j in range(i*i, 101, i):
                is_prime[j] = False
    
    # Function to factorize a number
    def factorize(x):
        factors = defaultdict(int)
        for p in primes:
            while x % p == 0:
                factors[p] += 1
                x //= p
        return factors
    
    # Initialize prime factors for each element
    prime_factors = [factorize(x) for x in A]
    
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
                for p in self.tree[2 * i]:
                    self.tree[i][p] += self.tree[2 * i][p]
                for p in self.tree[2 * i + 1]:
                    self.tree[i][p] += self.tree[2 * i + 1][p]
        
        def update(self, pos, new_factors):
            pos += self.size
            self.tree[pos] = new_factors
            pos >>= 1
            while pos >= 1:
                for p in self.tree[2 * pos]:
                    self.tree[pos][p] += self.tree[2 * pos][p]
                for p in self.tree[2 * pos + 1]:
                    self.tree[pos][p] += self.tree[2 * pos + 1][p]
                pos >>= 1
        
        def query(self, l, r):
            res = defaultdict(int)
            l += self.size
            r += self.size
            while l <= r:
                if l % 2 == 1:
                    for p in self.tree[l]:
                        res[p] += self.tree[l][p]
                    l += 1
                if r % 2 == 0:
                    for p in self.tree[r]:
                        res[p] += self.tree[r][p]
                    r -= 1
                l >>= 1
                r >>= 1
            return res
    
    st = SegmentTree(prime_factors)
    
    output = []
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
            for p in factors:
                if factors[p] % 2 != 0:
                    is_square = False
                    break
            output.append("YES" if is_square else "NO")
        else:
            i = int(data[idx]) - 1
            idx += 1
            val = int(data[idx])
            idx += 1
            # Factorize the value to be multiplied
            val_factors = factorize(val)
            # Update the prime factors at position i
            new_factors = defaultdict(int, prime_factors[i])
            for p in val_factors:
                new_factors[p] += val_factors[p]
            st.update(i, new_factors)
    
    print("\n".join(output))