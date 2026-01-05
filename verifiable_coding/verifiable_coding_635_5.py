import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    K = int(data[1])
    A = list(map(int, data[2:2+N]))
    
    from collections import Counter
    freq = Counter(A)
    
    # dp[i] = number of good subsequences of length i
    dp = [0] * (K + 1)
    dp[0] = 1  # empty subsequence
    
    for num in freq:
        count = freq[num]
        # We need to update dp in reverse to avoid overcounting
        for i in range(K, -1, -1):
            if i >= 1:
                dp[i] = (dp[i] + dp[i-1] * count) % MOD
    
    # Sum all good subsequences of length at most K
    result = sum(dp[0:K+1]) % MOD
    print(result)

if __name__ == '__main__':
    solve()