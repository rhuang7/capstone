import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]

    for s in cases:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(1, n):
            if s[i-1] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i-1]
            if i >= 2:
                two_digit = int(s[i-2:i])
                if 10 <= two_digit <= 26:
                    dp[i] += dp[i-2]
        if dp[n] % 2 == 0:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()