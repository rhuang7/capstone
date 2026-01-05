import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    A = list(map(int, data[1:n+1]))

    # dp[i] represents the maximum length of a valid subsequence ending at index i
    dp = [1] * n
    # xor_prev[i] represents the xor of the last two elements in the subsequence ending at i
    xor_prev = [0] * n

    for i in range(n):
        for j in range(i):
            current_xor = A[i] ^ A[j]
            if current_xor >= xor_prev[j]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    xor_prev[i] = current_xor

    print(max(dp))

if __name__ == '__main__':
    solve()