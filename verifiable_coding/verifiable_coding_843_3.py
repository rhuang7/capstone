import sys
import bisect

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
        A = []
        for _ in range(N):
            row = list(map(int, data[idx:idx+N]))
            idx += N
            A.append(row)
        
        # Preprocess each row to sort it
        sorted_rows = []
        for row in A:
            sorted_row = sorted(row)
            sorted_rows.append(sorted_row)
        
        # dp[i][j] = maximum sum for first i rows, choosing j-th element in i-th row
        dp = [[-1] * N for _ in range(N)]
        
        # Initialize first row
        for j in range(N):
            dp[0][j] = sorted_rows[0][j]
        
        # Fill dp table
        for i in range(1, N):
            for j in range(N):
                # Find the best previous element that is less than current element
                # We need to find the largest value in dp[i-1][k] where sorted_rows[i-1][k] < sorted_rows[i][j]
                # Use binary search for efficiency
                current_val = sorted_rows[i][j]
                # Find the largest k where sorted_rows[i-1][k] < current_val
                k = bisect.bisect_left(sorted_rows[i-1], current_val) - 1
                if k >= 0:
                    dp[i][j] = current_val + dp[i-1][k]
                else:
                    dp[i][j] = -1
        
        # Find the maximum value in the last row
        max_sum = max(dp[N-1])
        results.append(max_sum if max_sum != -1 else -1)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()