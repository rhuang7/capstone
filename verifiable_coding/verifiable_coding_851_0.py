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
        # The compressed string has 2 * (number of runs) elements
        # The number of runs is between 1 and N (if all characters are different)
        # So the expected length is 2 * E[number of runs]
        
        # For a string of length N with up to K distinct characters, the expected number of runs is:
        # E[r] = 1 + (N-1) * (1 - (1/K))  # Because each new character has a (K-1)/K chance of being different from the previous one
        # But this is only valid when K >= 2, and for K=1, the number of runs is 1
        
        if K == 1:
            expected_runs = 1
        else:
            expected_runs = 1 + (N - 1) * (1 - (1 / K))
        
        expected_length = 2 * expected_runs
        results.append(f"{expected_length:.10f}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()