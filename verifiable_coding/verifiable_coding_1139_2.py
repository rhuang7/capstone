import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]

    def count_ways(s):
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(1, n):
            if s[i-1] != '0':
                dp[i+1] += dp[i]
            if s[i-1] != '0' and s[i] != '0':
                two_digit = int(s[i-1:i+1])
                if 10 <= two_digit <= 26:
                    dp[i+1] += dp[i-1]
        return dp[n]

    for s in cases:
        ways = count_ways(s)
        print('YES' if ways % 2 == 0 else 'NO')

if __name__ == '__main__':
    solve()