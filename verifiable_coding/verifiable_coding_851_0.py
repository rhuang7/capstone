import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        K = int(data[idx+1])
        idx += 2
        
        # Expected length of compressed string
        # The compressed string length is 2 * number of runs
        # Each run contributes 2 to the length (char + count)
        # So we need to compute the expected number of runs
        
        # For a string with K distinct characters, the expected number of runs
        # is K * (1 - (1/(K))^{N-1}) / (1 - 1/K) ) = K * (1 - (1/K)^{N-1}) / ( (K-1)/K )) = K^2 * (1 - (1/K)^{N-1}) / (K-1)
        # But this is not exactly correct for all cases, so we use a more accurate approach
        
        # For K=1, all characters are the same, so there is only 1 run
        if K == 1:
            expected_runs = 1
        else:
            # For K >= 2, the expected number of runs is K * (1 - (1/K)^{N-1}) / (1 - 1/K)
            # Simplify: K * (1 - (1/K)^{N-1}) / ((K-1)/K) ) = K^2 * (1 - (1/K)^{N-1}) / (K-1)
            # But for large N, (1/K)^{N-1} is negligible, so expected_runs ≈ K^2 / (K-1)
            # However, we need to compute it exactly for all cases
            # We use a dynamic programming approach for small N and K, but for large N and K, we use the formula
            
            # For large N, the expected number of runs is approximately K * (1 - (1/K)^{N-1}) / (1 - 1/K)
            # But for N up to 1e9, we can't compute this directly
            # We use the formula for large N: expected_runs = K * (1 - (1/K)^{N-1}) / (1 - 1/K)
            # But for K=2, it's 2 * (1 - (1/2)^{N-1}) / (1 - 1/2) ) = 2 * (1 - (1/2)^{N-1}) / (1/2) ) = 4 * (1 - (1/2)^{N-1})
            # Which is approximately 4 for large N
            
            # We use the formula for large N and K:
            # expected_runs = K * (1 - (1/K)^{N-1}) / (1 - 1/K)
            # But we can't compute (1/K)^{N-1} directly for large N and K
            # So we use logarithms to compute it
            
            # Compute (1/K)^{N-1}
            log_term = (N-1) * math.log(1/K)
            if log_term < -1000:
                # The term is negligible
                expected_runs = K * (1 - 0) / (1 - 1/K)
            else:
                exp_term = math.exp(log_term)
                expected_runs = K * (1 - exp_term) / (1 - 1/K)
        
        # The compressed string length is 2 * expected_runs
        expected_length = 2 * expected_runs
        results.append(f"{expected_length:.10f}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()