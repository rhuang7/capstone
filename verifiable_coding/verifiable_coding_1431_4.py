import sys
import math

MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    Ns = list(map(int, data[1:T+1]))
    
    for N in Ns:
        if N == 2:
            print(0)
            continue
        
        # Calculate the number of paths from (0,0) to (N-1,N-1)
        # Each path has exactly (2N-2) steps, and the number of paths is C(2N-2, N-1)
        # We need to count the number of paths where the number of transitions is even
        # Because each transition costs 1 coin, and initial coins are 2N, we want the number of paths where transitions < 2N
        
        # The number of transitions is equal to the number of times the path crosses the diagonal r = c
        # This is a classic problem in combinatorics, and the number of paths with even number of crossings is C(2N-2, N-1) / 2
        
        # But for large N, we need to compute this modulo MOD
        # We use Lucas theorem to compute binomial coefficients modulo MOD
        
        def comb(n, k, mod):
            if k < 0 or k > n:
                return 0
            if k == 0 or k == n:
                return 1
            # Compute C(n, k) mod mod using Lucas theorem
            res = 1
            while n > 0 or k > 0:
                ni = n % mod
                ki = k % mod
                if ki > ni:
                    return 0
                # Compute C(ni, ki) mod mod
                numerator = 1
                denominator = 1
                for i in range(ki):
                    numerator = numerator * (ni - i) % mod
                    denominator = denominator * (i + 1) % mod
                res = res * numerator * pow(denominator, mod-2, mod) % mod
                n //= mod
                k //= mod
            return res
        
        total = comb(2*N-2, N-1, MOD)
        even = total // 2
        print(even % MOD)

if __name__ == '__main__':
    solve()