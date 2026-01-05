import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    fees = list(map(int, data[1:N+1]))
    
    if N == 0:
        print(0)
        return
    
    # dp[i] represents the maximum earnings up to the i-th match
    dp = [0] * (N + 1)
    # dp[i] can be either:
    # 1. fees[i-1] + dp[i-2] (play this match)
    # 2. dp[i-1] (skip this match)
    for i in range(1, N + 1):
        dp[i] = max(fees[i-1] + (dp[i-2] if i >= 2 else 0), dp[i-1])
    
    print(dp[N])

if __name__ == '__main__':
    solve()