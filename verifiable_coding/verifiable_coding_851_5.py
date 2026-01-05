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
        # Each run of the same character contributes 2 to the length (char + length)
        # The number of runs is equal to the number of transitions between different characters + 1
        # The expected number of runs for a string of length N with K distinct characters is:
        # E[r] = 1 + (N-1) * (K-1)/K
        # So the expected length is 2 * E[r]
        # But we need to consider that the string is randomly chosen from all possibilities
        # The expected number of runs is 1 + (N-1) * (K-1)/K
        # So the expected length is 2 * (1 + (N-1) * (K-1)/K)
        # However, this is only valid when K >= 2
        # For K = 1, the string is all the same character, so the length is 2
        if K == 1:
            results.append("2.0")
        else:
            expected_runs = 1 + (N - 1) * (K - 1) / K
            expected_length = 2 * expected_runs
            results.append(f"{expected_length:.10f}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()