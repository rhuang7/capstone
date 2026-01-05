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
        
        # For each position i (1-based), we need A[i-1] % M == i % M
        # So we group elements by their (value % M) and their position (i % M)
        # We'll count how many elements satisfy A[i-1] % M == r for each r
        # Then, for each r, we can choose some elements to form a subsequence
        
        # We'll use dynamic programming to count the number of valid subsequences
        # dp[k][r] = number of ways to form a subsequence of length k ending with a value that has remainder r
        # We'll use a 2D array where dp[k][r] is the count
        
        # Since M can be up to 100*K, and K can be up to 10^4, we need a way to handle this efficiently
        # We'll use a list of dictionaries, where dp[k] is a dictionary mapping remainders to counts
        
        dp = [{} for _ in range(K+1)]
        # For subsequences of length 0, there is 1 way (empty subsequence)
        dp[0][0] = 1
        
        for i in range(N):
            val = A[i]
            rem = val % M
            pos_rem = (i+1) % M  # since the position is 1-based
            if rem != pos_rem:
                continue
            # For each possible subsequence length, we can add this element to it
            for k in range(K, 0, -1):
                for r in dp[k-1]:
                    count = dp[k-1][r]
                    if r not in dp[k]:
                        dp[k][r] = 0
                    dp[k][r] = (dp[k][r] + count) % MOD
        
        # The answer is the sum of all ways to form a subsequence of length K
        ans = sum(dp[K].values()) % MOD
        results.append(ans)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()