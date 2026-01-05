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
        
        # Precompute required remainders for positions 1..K
        required_remainders = [i % M for i in range(1, K+1)]
        
        # Count how many elements in A have a value that matches the required remainder for each position
        count = [0] * M
        for a in A:
            rem = a % M
            count[rem] += 1
        
        # Dynamic programming to count valid subsequences
        dp = [0] * (K + 1)
        dp[0] = 1  # Base case: one way to choose 0 elements
        
        for i in range(1, K + 1):
            for rem in range(M):
                if rem == required_remainders[i - 1]:
                    dp[i] = (dp[i] + dp[i - 1] * count[rem]) % MOD
        
        results.append(dp[K] % MOD)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()