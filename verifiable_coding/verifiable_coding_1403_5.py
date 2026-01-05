import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]
    
    for s in cases:
        n = len(s)
        if n == 0:
            print(0)
            continue
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(1, n):
            if s[i] != '0':
                dp[i+1] = (dp[i+1] + dp[i]) % MOD
            if i > 0 and s[i-1] != '0' and (s[i-1:i+1] == '10' or s[i-1:i+1] == '20'):
                dp[i+1] = (dp[i+1] + dp[i-1]) % MOD
        print(dp[n] % MOD)

if __name__ == '__main__':
    solve()