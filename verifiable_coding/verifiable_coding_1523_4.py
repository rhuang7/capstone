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
    
    # dp[i] = maximum earnings up to the i-th match
    dp = [0] * (N + 1)
    dp[0] = 0
    dp[1] = fees[0]
    
    for i in range(2, N + 1):
        # If we play the i-th match, we cannot play the (i-1)-th match
        # So take the maximum of dp[i-2] + fees[i-1]
        # If we don't play the i-th match, take dp[i-1]
        dp[i] = max(dp[i-2] + fees[i-1], dp[i-1])
    
    print(dp[N])

if __name__ == '__main__':
    solve()