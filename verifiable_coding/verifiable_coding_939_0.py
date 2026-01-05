import sys
import math

MOD = 10**9 + 7

def count_lucky_numbers(n):
    dp = [[0] * 2 for _ in range(11)]
    dp[0][0] = 1
    for i in range(1, 11):
        for j in range(2):
            if j == 0:
                dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % MOD
            else:
                dp[i][1] = (dp[i-1][0] + dp[i-1][1]) % MOD
    return dp[n][1]

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    for _ in range(T):
        L = data[idx]
        R = data[idx+1]
        idx += 2
        L = int(L)
        R = int(R)
        res = 0
        for i in range(1, 11):
            count = count_lucky_numbers(i)
            res = (res + count) % MOD
        print(res)

if __name__ == '__main__':
    solve()