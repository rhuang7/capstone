import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    K = int(data[1])
    A = list(map(int, data[2:2+N]))
    
    from collections import defaultdict
    freq = defaultdict(int)
    for num in A:
        freq[num] += 1
    
    # dp[i] = number of good subsequences with exactly i elements
    dp = [0] * (K + 1)
    dp[0] = 1  # empty subsequence
    
    for num, count in freq.items():
        # Make a copy to avoid overwriting during iteration
        new_dp = dp[:]
        for i in range(K, -1, -1):
            if i >= 1:
                new_dp[i] = (new_dp[i] + dp[i-1] * count) % MOD
        dp = new_dp
    
    # Sum all dp[0...K]
    result = sum(dp[:K+1]) % MOD
    print(result)

if __name__ == '__main__':
    solve()