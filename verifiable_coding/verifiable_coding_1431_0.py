import sys
import math

MOD = 10**9 + 7

def main():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    N_list = list(map(int, data[1:T+1]))
    
    for N in N_list:
        if N == 2:
            print(0)
            continue
        
        # Calculate the number of paths from (0,0) to (N-1,N-1)
        # Each path is a sequence of N-1 right and N-1 down moves
        # Total paths = C(2N-2, N-1)
        # But we need to count only those paths that cross from Water to Fire or vice versa
        
        # The number of paths that cross from Water to Fire or vice versa is equal to
        # the number of paths that cross the diagonal (r = c) an odd number of times
        # This is given by the Catalan numbers formula
        # But we need to find the probability that the number of transitions is greater than 2*N
        
        # The number of paths that cross the diagonal an odd number of times is C(2N-2, N-1) - C(2N-2, N-2)
        # The number of paths that cross the diagonal an even number of times is C(2N-2, N-1) + C(2N-2, N-2)
        
        # The number of paths that cross the diagonal an odd number of times is equal to the number of paths that have an odd number of transitions
        # So the probability is (C(2N-2, N-1) - C(2N-2, N-2)) / C(2N-2, N-1)
        
        # But we need to compute this modulo MOD
        
        # Precompute factorials and inverse factorials up to 2*1e9
        # But since N can be up to 1e9, we need a way to compute combinations modulo MOD
        
        # Use Lucas theorem to compute combinations modulo MOD
        
        def comb(n, k):
            if k < 0 or k > n:
                return 0
            res = 1
            for i in range(k):
                res = res * (n - i) % MOD
                res = res * pow(i + 1, MOD-2, MOD) % MOD
            return res
        
        c1 = comb(2*N-2, N-1)
        c2 = comb(2*N-2, N-2)
        numerator = (c1 - c2) % MOD
        denominator = c1
        # Compute inverse of denominator
        inv_denominator = pow(denominator, MOD-2, MOD)
        result = (numerator * inv_denominator) % MOD
        print(result)

if __name__ == '__main__':
    main()