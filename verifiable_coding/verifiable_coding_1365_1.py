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
    
    for i in range(n):
        if s[i] == 'f':
            dp[i+1] = (dp[i+1] + dp[i]) % MOD
        elif s[i] == 'g':
            dp[i+1] = (dp[i+1] + dp[i]) % MOD
        else:
            dp[i+1] = (dp[i+1] + dp[i]) % MOD
    
    print(dp[n] % MOD)

if __name__ == '__main__':
    solve()