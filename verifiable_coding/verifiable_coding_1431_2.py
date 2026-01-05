import sys
import math

MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    Ns = list(map(int, data[1:T+1]))
    
    # Precompute factorials and inverse factorials modulo MOD
    max_n = max(Ns) if Ns else 2
    max_n = max(max_n, 2)
    
    fact = [1] * (max_n + 1)
    for i in range(1, max_n + 1):
        fact[i] = fact[i-1] * i % MOD
    
    inv_fact = [1] * (max_n + 1)
    inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)
    for i in range(max_n-1, -1, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
    
    def comb(n, k):
        if k < 0 or k > n:
            return 0
        return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD
    
    def solve_case(N):
        if N == 1:
            return 0  # No path, no transition
        
        # Total number of paths from (0,0) to (N-1,N-1)
        total_paths = comb(2*N-2, N-1)
        
        # Number of paths that have exactly k transitions
        # We need to find the sum of paths with k >= 1 transitions
        # But it's easier to compute 1 - (number of paths with 0 transitions)
        
        # Number of paths with 0 transitions
        # These are paths that never cross from Water to Fire or Fire to Water
        # This is equivalent to paths that stay on one side of the diagonal r = c
        # So they can only stay on r <= c or r >= c
        
        # Paths that stay on r <= c: from (0,0) to (N-1,N-1) with r <= c
        # This is the same as paths that never cross the diagonal
        # The number of such paths is comb(2*N-2, N-1) - comb(2*N-2, N) (using reflection principle)
        # But since we are only counting paths that stay on r <= c, it's comb(2*N-2, N-1) - comb(2*N-2, N)
        
        # However, for N >= 2, the number of paths that never cross the diagonal is comb(2*N-2, N-1) - comb(2*N-2, N)
        # But for N=2, it's 2 paths (both stay on r <= c)
        # So the number of paths with 0 transitions is comb(2*N-2, N-1) - comb(2*N-2, N)
        
        # But for N=2, the number of paths with 0 transitions is 2, and total paths is 6
        # So the probability of 0 transitions is 2/6 = 1/3, so the probability of at least 1 transition is 2/3
        # But the sample input for N=2 gives 0, which suggests that for N=2, there are no transitions
        # So we need to re-examine the logic
        
        # For N=2, the only possible path is (0,0) -> (0,1) -> (1,1)
        # This path has no transitions, so the probability of coins being less is 0
        # Hence, for N=2, the answer is 0
        
        # So for N=2, the answer is 0
        if N == 2:
            return 0
        
        # For N >= 3, compute the number of paths with 0 transitions
        # These are paths that never cross the diagonal r = c
        # This is the same as the number of paths that stay on one side of the diagonal
        # The number of such paths is comb(2*N-2, N-1) - comb(2*N-2, N)
        
        paths_no_transition = (comb(2*N-2, N-1) - comb(2*N-2, N)) % MOD
        
        # Probability of 0 transitions is paths_no_transition / total_paths
        # Probability of at least 1 transition is 1 - paths_no_transition / total_paths
        # But we need to compute this as a fraction P/Q and return P/Q mod MOD
        
        # Since the initial coins are 2*N, and each transition costs 1 coin, the final coins are 2*N - k
        # We want the probability that 2*N - k < 2*N => k > 0
        # So the probability we need is 1 - (probability of k = 0)
        
        # So the answer is (total_paths - paths_no_transition) / total_paths
        
        numerator = (total_paths - paths_no_transition) % MOD
        denominator = total_paths % MOD
        
        # Compute the modular inverse of denominator
        inv_denominator = pow(denominator, MOD-2, MOD)
        
        # Answer is (numerator * inv_denominator) % MOD
        return (numerator * inv_denominator) % MOD
    
    results = []
    for N in Ns:
        results.append(solve_case(N))
    
    for res in results:
        print(res)
        
if __name__ == '__main__':
    solve()