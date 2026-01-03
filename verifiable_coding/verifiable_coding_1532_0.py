import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        maxnumbers = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Sort the maxnumbers
        maxnumbers.sort()
        
        # Check if it's possible to assign distinct numbers
        # The smallest possible maximum is N (since we need N distinct numbers starting from 1)
        if maxnumbers[0] < 1 or maxnumbers[-1] < N:
            results.append(0)
            continue
        
        # Compute the number of ways
        # We use dynamic programming to count the number of ways to assign numbers
        # dp[i][j] = number of ways to assign numbers to the first i people with the maximum number j
        # We can optimize space by using a 1D array
        
        dp = [0] * (maxnumbers[-1] + 1)
        dp[0] = 1  # Base case: 1 way to assign nothing
        
        for num in maxnumbers:
            # We need to assign a number to this person, which is <= num
            # We can use the previous dp values to compute the current dp
            # We need to reverse iterate to avoid overwriting values we need
            for j in range(num, 0, -1):
                dp[j] = (dp[j] + dp[j-1]) % MOD
        
        results.append(dp[maxnumbers[-1]] if maxnumbers[-1] >= N else 0)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()