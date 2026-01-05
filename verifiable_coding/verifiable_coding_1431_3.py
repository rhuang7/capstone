import sys
import math

MOD = 10**9 + 7

def main():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    Ns = list(map(int, data[1:T+1]))
    
    for N in Ns:
        if N == 2:
            print(0)
            continue
        
        # Calculate the number of paths from (0,0) to (N-1,N-1)
        # Each path has exactly (2N-2) steps, so there are C(2N-2, N-1) paths
        # The number of transitions is the number of times the path crosses the diagonal
        # We need to count the number of paths that cross the diagonal an odd number of times
        
        # The number of paths that cross the diagonal an odd number of times is C(2N-2, N-1) / 2
        # But this is only valid for N >= 3
        
        # Calculate C(2N-2, N-1) mod MOD
        # Using Lucas theorem for large N
        
        def comb(n, k, mod):
            if k < 0 or k > n:
                return 0
            numerator = 1
            for i in range(k):
                numerator = numerator * (n - i) % mod
            denominator = 1
            for i in range(k):
                denominator = denominator * (i + 1) % mod
            return numerator * pow(denominator, mod-2, mod)
        
        total = comb(2*N-2, N-1, MOD)
        prob = (total // 2) % MOD
        print(prob)

if __name__ == '__main__':
    main()