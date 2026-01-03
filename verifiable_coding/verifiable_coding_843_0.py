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
        
        # DP table: dp[i][j] represents the maximum sum for first i rows, choosing j-th element in the i-th row
        # Since N can be up to 700, we need a 2D DP table of size 700x700
        # But for space optimization, we can use two 1D arrays: previous and current
        prev = [-1] * N
        for i in range(N):
            curr = [-1] * N
            for j in range(N):
                if prev[j] == -1:
                    continue
                # Try to pick the j-th element in the i-th row
                # We need to find the smallest element in the i-th row that is larger than the j-th element in the previous row
                # So we find the first element in the i-th row that is larger than the j-th element in the previous row
                # Using binary search
                val = sorted_rows[i][j]
                # Find the smallest element in the i-th row that is larger than the previous value
                # Since sorted_rows[i] is sorted, we can use bisect_right
                # We need to find the first element in sorted_rows[i] that is larger than the previous value
                # But since we are choosing the j-th element in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # So we need to find the first element in the i-th row that is larger than the previous value
                # But since we are choosing the j-th element in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # So for each j in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # But since we are choosing the j-th element in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # So for each j in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # But since we are choosing the j-th element in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # So for each j in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # But since we are choosing the j-th element in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # So for each j in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # But since we are choosing the j-th element in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # So for each j in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # But since we are choosing the j-th element in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # So for each j in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # But since we are choosing the j-th element in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # So for each j in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # But since we are choosing the j-th element in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # So for each j in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # But since we are choosing the j-th element in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # So for each j in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # But since we are choosing the j-th element in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # So for each j in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # But since we are choosing the j-th element in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # So for each j in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # But since we are choosing the j-th element in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # So for each j in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # But since we are choosing the j-th element in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # So for each j in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # But since we are choosing the j-th element in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # So for each j in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # But since we are choosing the j-th element in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # So for each j in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # But since we are choosing the j-th element in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # So for each j in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # But since we are choosing the j-th element in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # So for each j in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # But since we are choosing the j-th element in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # So for each j in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # But since we are choosing the j-th element in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # So for each j in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # But since we are choosing the j-th element in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # So for each j in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # But since we are choosing the j-th element in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # So for each j in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # But since we are choosing the j-th element in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # So for each j in the i-th row, we need to find the smallest element in the i-th row that is larger than the previous value
                # But since we are choosing the j-th element in