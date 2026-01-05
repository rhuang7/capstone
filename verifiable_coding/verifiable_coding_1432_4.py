import sys
import collections

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        matrix = []
        for _ in range(N):
            row = list(map(int, data[idx:idx+N]))
            idx += N
            matrix.append(row)
        
        # Collect all 1s in the matrix
        ones = []
        for i in range(N):
            for j in range(N):
                if matrix[i][j] == 1:
                    ones.append((i, j))
        
        # Sort the ones by row, then by column
        ones.sort()
        
        # Find the minimum bandwidth
        min_bandwidth = 0
        prev_row = -1
        prev_col = -1
        for i, j in ones:
            if i != prev_row:
                min_bandwidth = max(min_bandwidth, abs(j - prev_col))
                prev_row = i
                prev_col = j
            else:
                prev_col = j
        
        # Handle the last row
        if prev_row != -1:
            min_bandwidth = max(min_bandwidth, abs(prev_col - 0))
        
        results.append(str(min_bandwidth))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()