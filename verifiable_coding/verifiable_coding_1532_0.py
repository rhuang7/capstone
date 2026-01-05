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
        max_numbers = list(map(int, input[idx:idx+N]))
        idx += N
        
        # Sort the max_numbers
        max_numbers.sort()
        
        # Check if it's possible to assign distinct numbers
        # The minimum possible max number for the i-th person (0-based) is i+1
        # So if max_numbers[i] < i+1, it's impossible
        possible = True
        for i in range(N):
            if max_numbers[i] < i + 1:
                possible = False
                break
        if not possible:
            print(0)
            continue
        
        # Now calculate the number of ways
        # We can use dynamic programming
        # dp[i][j] = number of ways to assign numbers to first i people with maximum number j
        # But since N is small (up to 50), we can use a 1D array
        dp = [0] * (max_numbers[-1] + 1)
        dp[0] = 1  # Base case: 1 way to assign nothing
        
        for i in range(N):
            # Create a new dp array for the current step
            new_dp = [0] * (max_numbers[i] + 1)
            for j in range(max_numbers[i] + 1):
                # If we don't use j, the number of ways is dp[j]
                new_dp[j] = (new_dp[j] + dp[j]) % MOD
                # If we use j, the number of ways is dp[j-1]
                if j > 0:
                    new_dp[j] = (new_dp[j] + dp[j-1]) % MOD
            dp = new_dp
        
        print(dp[max_numbers[-1]] % MOD)

if __name__ == '__main__':
    solve()