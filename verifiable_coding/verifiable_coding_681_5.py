import sys
import math

MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    K = int(data[2])
    A = list(map(int, data[3:3+N]))
    
    # Count the frequency of each number in A
    freq = [0] * (M + 1)
    for num in A:
        freq[num] += 1
    
    # Calculate the number of ways to choose how many times to apply the operation
    # The operation can be applied at most (M // K) times
    max_ops = M // K
    
    # dp[i] = number of different final arrays after i operations
    dp = [0] * (max_ops + 1)
    dp[0] = 1  # Base case: no operations, only one array
    
    for i in range(1, max_ops + 1):
        # For each number from 1 to M, calculate how many times it can be increased
        # and update the dp accordingly
        for num in range(1, M + 1):
            # How many times can this number be increased in i operations?
            # Each operation increases it by K, so it can be increased at most (i // 1) times
            # But it must be <= M
            # So the number of times it can be increased is min(i, (M - num) // K)
            max_times = min(i, (M - num) // K)
            # For each possible number of times this number can be increased, update dp
            for t in range(1, max_times + 1):
                dp[i] = (dp[i] + dp[i - t] * freq[num]) % MOD
    
    print(dp[max_ops] % MOD)

if __name__ == '__main__':
    solve()