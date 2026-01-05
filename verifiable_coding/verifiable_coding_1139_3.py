import sys

def solve():
    import sys
    sys.setrecursionlimit(10000)
    T = int(sys.stdin.buffer.readline())
    for _ in range(T):
        S = sys.stdin.buffer.readline().decode().strip()
        n = len(S)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(1, n):
            if S[i-1:i+1] == '0':
                continue
            dp[i+1] += dp[i]
            if S[i+1] != '0':
                if int(S[i:i+2]) <= 26:
                    dp[i+2] += dp[i]
        if dp[n] % 2 == 0:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()