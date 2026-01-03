import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    K = int(data[1])
    
    # dp[i][j] represents the number of non-increasing arrays of length j
    # using the first i numbers (1 to i)
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    
    # Base case: arrays of length 0
    for i in range(N + 1):
        dp[i][0] = 1
    
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            # Case 1: the last element is i
            dp[i][j] = dp[i-1][j-1]
            # Case 2: the last element is less than i
            dp[i][j] += dp[i][j-1]
            dp[i][j] %= MOD
    
    print(dp[N][K])

if __name__ == '__main__':
    solve()