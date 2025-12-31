import sys
import math

MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    Ns = list(map(int, data[1:T+1]))
    
    results = []
    
    for N in Ns:
        if N == 2:
            results.append(0)
            continue
        
        # Calculate the number of paths from (0,0) to (N-1,N-1)
        # Each path consists of (N-1) right moves and (N-1) down moves
        # Total paths = C(2N-2, N-1)
        # We need to count the number of paths that cross from Water to Fire or Fire to Water
        
        # The number of paths that cross from Water to Fire or Fire to Water is equal to the number of paths that cross the diagonal
        # This is given by the Catalan numbers
        # The number of such paths is C(2N-2, N-1) - C(2N-2, N-2)
        # Which is the (N-1)th Catalan number multiplied by 2
        
        # However, we need to compute the probability that the number of transitions is greater than 2N - 2N = 0
        # So we need the number of paths with at least one transition
        
        # The number of paths with at least one transition is equal to the total number of paths minus the number of paths that never cross the diagonal
        
        # The number of paths that never cross the diagonal is the (N-1)th Catalan number
        # So the number of paths with at least one transition is C(2N-2, N-1) - C(2N-2, N-2)
        
        # But we need to compute this modulo MOD
        # We can precompute factorials and inverse factorials up to 2*1e9, but that's not feasible
        # So we need to find a formula for the Catalan number
        
        # The Catalan number C(n) = C(2n, n) / (n+1)
        # So the number of paths with at least one transition is C(2n-2, n-1) - C(2n-2, n-2)
        # Which is equal to C(2n-2, n-1) * (1 - 1/n)
        
        # So the probability is (C(2n-2, n-1) * (1 - 1/n)) / C(2n-2, n-1)
        # Which simplifies to (1 - 1/n) = (n-1)/n
        
        # So the probability is (n-1)/n
        
        # But we need to compute this modulo MOD
        # So the answer is (n-1) * inv(n) mod MOD
        
        # Compute (n-1) * inv(n) mod MOD
        inv_n = pow(N, MOD-2, MOD)
        ans = ((N-1) * inv_n) % MOD
        results.append(ans)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()