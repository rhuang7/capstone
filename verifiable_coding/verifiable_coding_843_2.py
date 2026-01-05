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
                # Find the maximum value in dp[i-1][k] where k < j
                max_prev = -1
                for k in range(j):
                    if dp[i-1][k] > max_prev:
                        max_prev = dp[i-1][k]
                if max_prev != -1:
                    dp[i][j] = max_prev + sorted_rows[i][j]
        
        # Find the maximum value in dp[N-1][*]
        max_sum = -1
        for j in range(N):
            if dp[N-1][j] > max_sum:
                max_sum = dp[N-1][j]
        
        results.append(str(max_sum) if max_sum != -1 else "-1")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()