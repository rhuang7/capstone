import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        from collections import Counter
        freq = Counter(A)
        
        # Find the greatest common divisor (GCD) of all elements
        from math import gcd
        from functools import reduce
        g = reduce(gcd, A)
        
        # The required length is the GCD
        length = g
        
        # Total number of wires is sum of (a_i / g) for all a_i
        total = sum(a // g for a in A)
        
        results.append(f"{length} {total}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()