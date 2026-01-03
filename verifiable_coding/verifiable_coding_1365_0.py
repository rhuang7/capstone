import sys
MOD = 10**9 + 7

def solve():
    s = sys.stdin.buffer.read().decode().strip()
    if 'c' in s or 'k' in s:
        print(0)
        return
    
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        if s[i-1] == 'f':
            dp[i] = (dp[i-1] + dp[i-2]) % MOD
        elif s[i-1] == 'g':
            dp[i] = (dp[i-1] + dp[i-2]) % MOD
        else:
            dp[i] = dp[i-1] % MOD
    
    print(dp[n])

if __name__ == '__main__':
    solve()