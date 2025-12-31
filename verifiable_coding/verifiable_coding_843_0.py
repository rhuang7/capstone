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
        
        # dp[i][j] represents the maximum sum for the first i rows, choosing j-th element from the i-th row
        dp = [[-1] * N for _ in range(N)]
        for j in range(N):
            dp[0][j] = sorted_rows[0][j]
        
        for i in range(1, N):
            for j in range(N):
                for k in range(N):
                    if dp[i-1][k] != -1 and sorted_rows[i][j] > sorted_rows[i-1][k]:
                        if dp[i][j] == -1 or dp[i][j] < dp[i-1][k] + sorted_rows[i][j]:
                            dp[i][j] = dp[i-1][k] + sorted_rows[i][j]
        
        max_sum = -1
        for j in range(N):
            if dp[N-1][j] != -1 and dp[N-1][j] > max_sum:
                max_sum = dp[N-1][j]
        results.append(max_sum if max_sum != -1 else -1)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()