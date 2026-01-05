import sys
import math
from collections import defaultdict

def factorize(n):
    factors = defaultdict(int)
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors[i] += 1
            n //= i
        i += 1
    if n > 1:
        factors[n] += 1
    return factors

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    
    N = int(data[idx])
    idx += 1
    
    A = []
    for _ in range(N):
        A.append(int(data[idx]))
        idx += 1
    
    Q = int(data[idx])
    idx += 1
    
    # Precompute prime factors for all numbers up to 1000000
    max_val = 1000000
    primes = []
    is_prime = [True] * (max_val + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, max_val + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, max_val + 1, i):
                is_prime[j] = False
    
    # Precompute prime factors for each number in A
    prime_factors = []
    for num in A:
        factors = defaultdict(int)
        n = num
        for p in primes:
            if p * p > n:
                break
            while n % p == 0:
                factors[p] += 1
                n //= p
        if n > 1:
            factors[n] += 1
        prime_factors.append(factors)
    
    # Segment tree for maintaining the product's prime factors
    class SegmentTree:
        def __init__(self, data):
            self.n = len(data)
            self.tree = [defaultdict(int) for _ in range(4 * self.n)]
            self.build(0, 0, self.n - 1, data)
        
        def build(self, node, l, r, data):
            if l == r:
                self.tree[node] = data[l].copy()
            else:
                mid = (l + r) // 2
                self.build(2*node+1, l, mid, data)
                self.build(2*node+2, mid+1, r, data)
                for p in self.tree[2*node+1]:
                    self.tree[node][p] += self.tree[2*node+1][p]
                for p in self.tree[2*node+2]:
                    self.tree[node][p] += self.tree[2*node+2][p]
        
        def update(self, node, l, r, idx, val):
            if l == r:
                self.tree[node] = val.copy()
            else:
                mid = (l + r) // 2
                if idx <= mid:
                    self.update(2*node+1, l, mid, idx, val)
                else:
                    self.update(2*node+2, mid+1, r, idx, val)
                for p in self.tree[2*node+1]:
                    self.tree[node][p] += self.tree[2*node+1][p]
                for p in self.tree[2*node+2]:
                    self.tree[node][p] += self.tree[2*node+2][p]
        
        def query(self, node, l, r, ql, qr):
            if qr < l or ql > r:
                return defaultdict(int)
            if ql <= l and r <= qr:
                return self.tree[node].copy()
            mid = (l + r) // 2
            left = self.query(2*node+1, l, mid, ql, qr)
            right = self.query(2*node+2, mid+1, r, ql, qr)
            for p in left:
                right[p] += left[p]
            return right
    
    st = SegmentTree(prime_factors)
    
    for _ in range(Q):
        k = int(data[idx])
        idx += 1
        if k == 1:
            l = int(data[idx]) - 1
            idx += 1
            r = int(data[idx]) - 1
            idx += 1
            res = st.query(0, 0, N-1, l, r)
            is_square = True
            for p in res:
                if res[p] % 2 != 0:
                    is_square = False
                    break
            print("YES" if is_square else "NO")
        else:
            i = int(data[idx]) - 1
            idx += 1
            val = int(data[idx])
            idx += 1
            # Factorize the value to update the segment tree
            factors = factorize(val)
            # Update the prime factors at position i
            new_factors = defaultdict(int)
            for p in prime_factors[i]:
                new_factors[p] = prime_factors[i][p]
            for p in factors:
                new_factors[p] += factors[p]
            st.update(0, 0, N-1, i, new_factors)
    
if __name__ == '__main__':
    solve()