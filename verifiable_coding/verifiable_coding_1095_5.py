import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    shelf = list(map(int, data[1:]))

    # Find the longest increasing subsequence (LIS) that is already in order
    # The minimum number of moves is N - length of LIS
    # Because each element not in the LIS needs to be moved

    # Initialize dp array for LIS
    dp = [1] * N
    for i in range(N):
        for j in range(i):
            if shelf[j] < shelf[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(N - max(dp))

if __name__ == '__main__':
    solve()