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
        # The number of runs is equal to the number of transitions between different characters + 1
        # The expected number of runs for a string with K distinct characters is (K-1) * (N / K) + 1
        # But since the string is randomly chosen, the expected number of runs is (K-1) * (N / K) + 1
        # Each run contributes 2 to the length, so total expected length is 2 * expected number of runs
        # However, this is only true if K >= 2
        # For K = 1, all characters are the same, so the compressed length is 2
        if K == 1:
            results.append("2.0")
        else:
            # Expected number of runs = (K-1) * (N / K) + 1
            # But this is not accurate for large N and K
            # We use a different approach based on the number of transitions
            # The expected number of transitions between different characters is (N-1) * (1 - (1/K)^2)
            # So the expected number of runs is (N-1) * (1 - (1/K)^2) + 1
            # Each run contributes 2 to the length, so total expected length is 2 * (N-1) * (1 - (1/K)^2) + 2
            expected_runs = (N - 1) * (1 - (1 / (K ** 2))) + 1
            expected_length = 2 * expected_runs
            results.append(f"{expected_length:.10f}")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()