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
        # dp[i][j] = max(dp[i-1][k] for k < j) + A[i][j]
        # We'll use a list to keep track of the maximum values for previous row
        prev_max = [-1] * N
        for i in range(N):
            curr_max = [-1] * N
            for j in range(N):
                # Find the maximum value in prev_max for indices < j
                max_prev = -1
                if prev_max[j] != -1:
                    max_prev = prev_max[j]
                if i == 0:
                    # First row, can choose any element
                    curr_max[j] = sorted_rows[i][j]
                else:
                    # Find the maximum value in prev_max for indices < j
                    if j > 0:
                        max_prev = max(prev_max[:j])
                    curr_max[j] = max_prev + sorted_rows[i][j]
            prev_max = curr_max
        
        # Find the maximum value in the last row
        result = max(prev_max)
        results.append(result if result != -1 else -1)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()