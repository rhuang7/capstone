import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N, K, M = map(int, data[idx:idx+3])
        idx += 3
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # For each position i (1-based), determine which remainder it can contribute to
        # We'll count how many numbers in A have value % M equal to r, for r in 0..M-1
        count = [0] * M
        for num in A:
            rem = num % M
            count[rem] += 1
        
        # dp[i][r] = number of ways to choose i elements with the i-th element having remainder r
        # We'll use a 1D array for space optimization
        dp = [0] * M
        dp[0] = 1  # base case: 1 way to choose 0 elements with remainder 0
        
        for i in range(1, K+1):
            new_dp = [0] * M
            for r in range(M):
                if dp[r] == 0:
                    continue
                # For the i-th position (1-based), the remainder must be (i % M)
                target_r = i % M
                # We can take any element with remainder target_r
                new_dp[target_r] = (new_dp[target_r] + dp[r] * count[target_r]) % MOD
            dp = new_dp
        
        results.append(dp[0] % MOD)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()