import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # We need to compute the maximum and minimum possible values of the expression
        # after optimal play by both players
        # Since the players alternate, starting with Vanja, the first player (Vanja) wants to maximize |V|
        # and the second player (Miksi) wants to minimize |V|
        
        # We use dynamic programming to track the possible values
        # dp[i][0] = maximum value achievable with i elements and current player to move
        # dp[i][1] = minimum value achievable with i elements and current player to move
        
        # Initialize dp
        dp = [[0] * 2 for _ in range(N + 1)]
        
        # Base case: 0 elements, value is 0
        dp[0][0] = 0
        dp[0][1] = 0
        
        for i in range(1, N + 1):
            # Current player is Vanja (if i is odd) or Miksi (if i is even)
            # For each possible value, we consider adding or subtracting the next bit
            # We track the max and min possible values
            if i % 2 == 1:
                # Vanja's turn: maximize the value
                dp[i][0] = max(dp[i-1][0] + A[i-1], dp[i-1][1] + A[i-1])
                dp[i][1] = max(dp[i-1][0] - A[i-1], dp[i-1][1] - A[i-1])
            else:
                # Miksi's turn: minimize the value
                dp[i][0] = min(dp[i-1][0] + A[i-1], dp[i-1][1] + A[i-1])
                dp[i][1] = min(dp[i-1][0] - A[i-1], dp[i-1][1] - A[i-1])
        
        # The final value is either dp[N][0] or dp[N][1], depending on the player
        # Since Vanja starts, the last move is made by Miksi if N is even, or Vanja if N is odd
        # So the final value is dp[N][0] if N is even, else dp[N][1]
        if N % 2 == 1:
            final_val = dp[N][1]
        else:
            final_val = dp[N][0]
        
        if abs(final_val) >= K:
            results.append(1)
        else:
            results.append(2)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()