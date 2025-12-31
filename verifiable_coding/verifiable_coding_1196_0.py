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
            for j in range(M - K + 1):
                current_sum = sum(row[j:j+K])
                if current_sum > max_sum:
                    max_sum = current_sum
        
        # Vertical sliding window
        for j in range(M):
            col = [grid[i][j] for i in range(N)]
            for i in range(N - K + 1):
                current_sum = sum(col[i:i+K])
                if current_sum > max_sum:
                    max_sum = current_sum
        
        results.append(str(max_sum))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()