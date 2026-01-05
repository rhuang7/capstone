import sys
import math

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
        M = int(data[idx+1])
        idx += 2
        p = list(map(int, data[idx:idx+M]))
        idx += M
        
        # For each p_i, compute the maximum number of times it can be used
        # To kill a sorcerer, the position must be in the current set of living sorcerers
        # The position is determined by (k * N + (p_i - 1)) % N, where k is the number of times the operation has been performed
        # We need to find the maximum k such that (k * N + (p_i - 1)) % N != 0 (not yourself)
        # So we need to find the maximum k such that (k * N + (p_i - 1)) % N != 0
        # This is equivalent to finding the maximum k such that k * N + (p_i - 1) is not divisible by N
        # Which is equivalent to finding the maximum k such that (p_i - 1) % N != 0
        # So for each p_i, the maximum number of times it can be used is floor((N - 1) / gcd(p_i, N))
        # But since we can use the same spell multiple times, we need to find the maximum number of times a spell can be used
        # The maximum number of times a spell can be used is floor((N - 1) / gcd(p_i, N))
        # So for each p_i, compute the maximum number of times it can be used
        # Then take the maximum over all p_i
        
        max_k = 0
        for pi in p:
            g = math.gcd(pi, N)
            if g == 0:
                continue
            # The maximum number of times this spell can be used is floor((N - 1) / g)
            max_k = max(max_k, (N - 1) // g)
        
        results.append(str(max_k))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()