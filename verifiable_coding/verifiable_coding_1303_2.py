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
        N = int(data[idx])
        K = int(data[idx+1])
        M = int(data[idx+2])
        idx += 3
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # For each position i (1-based), we compute the required remainder
        # rem[i] = i % M
        rem = [i % M for i in range(1, K+1)]
        
        # Count how many elements in A have value % M equal to rem[i]
        # We'll use a list of counts for each remainder
        cnt = [0] * M
        for num in A:
            r = num % M
            cnt[r] += 1
        
        # Now, we need to compute the number of ways to choose one element from each remainder group
        # We'll use dynamic programming to compute the number of ways
        dp = [0] * (K+1)
        dp[0] = 1
        for i in range(1, K+1):
            for r in range(M):
                if rem[i-1] == r:
                    dp[i] = (dp[i] + dp[i-1] * cnt[r]) % MOD
        
        results.append(dp[K])
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()