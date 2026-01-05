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
        N = int(data[idx])
        M = int(data[idx+1])
        K = int(data[idx+2])
        idx += 3
        
        grid = []
        for _ in range(N):
            row = list(map(int, data[idx:idx+M]))
            grid.append(row)
            idx += M
        
        max_sum = 0
        
        # Horizontal sliding window
        for i in range(N):
            row = grid[i]
            current_sum = sum(row[:K])
            max_sum = max(max_sum, current_sum)
            for j in range(1, M - K + 1):
                current_sum = current_sum - row[j-1] + row[j+K-1]
                max_sum = max(max_sum, current_sum)
        
        # Vertical sliding window
        for j in range(M):
            col = [grid[i][j] for i in range(N)]
            current_sum = sum(col[:K])
            max_sum = max(max_sum, current_sum)
            for i in range(1, N - K + 1):
                current_sum = current_sum - col[i-1] + col[i+K-1]
                max_sum = max(max_sum, current_sum)
        
        results.append(str(max_sum))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()