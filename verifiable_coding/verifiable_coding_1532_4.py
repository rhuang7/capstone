import sys
MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N = int(input[idx])
        idx += 1
        maxnumbers = list(map(int, input[idx:idx+N]))
        idx += N
        
        maxnumber = max(maxnumbers)
        if maxnumber < N:
            print(0)
            continue
        
        # Sort the maxnumbers
        maxnumbers.sort()
        
        # Compute the number of valid permutations
        # We use dynamic programming to count the number of ways
        # dp[i][j] = number of ways to assign numbers to first i people with j being the maximum number used
        dp = [ [0]*(maxnumber+2) for _ in range(N+1) ]
        dp[0][0] = 1
        
        for i in range(1, N+1):
            for j in range(maxnumber+1):
                # If the current maxnumber is less than the previous maxnumber, it's invalid
                if j < maxnumbers[i-1]:
                    continue
                # We can either take a number less than j or equal to j
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % MOD
        
        print(dp[N][maxnumber] % MOD)

if __name__ == '__main__':
    solve()