import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    M = int(data[idx])
    idx += 1
    N = int(data[idx])
    idx += 1
    
    grid = []
    for _ in range(M):
        row = list(map(int, data[idx:idx+N]))
        grid.append(row)
        idx += N
    
    C = int(data[idx])
    idx += 1
    
    # Precompute prefix sums
    prefix = [[0]*(N+1) for _ in range(M+1)]
    for i in range(1, M+1):
        for j in range(1, N+1):
            prefix[i][j] = grid[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
    
    output = []
    for _ in range(C):
        x1 = int(data[idx])
        idx += 1
        y1 = int(data[idx])
        idx += 1
        x2 = int(data[idx])
        idx += 1
        y2 = int(data[idx])
        idx += 1
        
        total = prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1]
        output.append(str(total))
    
    print('\n'.join(output))

if __name__ == '__main__':
    solve()