import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        K = int(data[index+1])
        index += 2
        
        # Expected length of compressed string
        # Each run of the same character contributes 2 to the length (char + count)
        # So the expected length is 2 * number of runs
        # The number of runs is equal to the number of transitions between different characters + 1
        # For a string with K distinct characters, the expected number of transitions is (K-1) * (N-1) / N
        # So the expected number of runs is (K-1) * (N-1) / N + 1
        # Hence, expected length is 2 * ((K-1) * (N-1) / N + 1)
        
        # But this formula is not correct for all cases. We need to use dynamic programming.
        # However, for large N and K, we need an efficient way.
        
        # The correct formula for expected number of runs is:
        # E[r] = 1 + (K-1) * (N-1) / N
        # So the expected length is 2 * E[r]
        
        # But this is only valid for K >= 1
        if K == 1:
            # All characters are the same, so only 1 run
            results.append("2.0")
        else:
            # Expected number of runs is 1 + (K-1) * (N-1) / N
            # So expected length is 2 * (1 + (K-1) * (N-1) / N)
            expected_runs = 1 + (K - 1) * (N - 1) / N
            expected_length = 2 * expected_runs
            results.append(f"{expected_length:.10f}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()