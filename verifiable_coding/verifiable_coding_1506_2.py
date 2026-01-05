import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1
    
    matrix = []
    for _ in range(N):
        row = data[idx]
        idx += 1
        matrix.append([int(c) for c in row])
    
    Q = int(data[idx])
    idx += 1
    
    queries = []
    for _ in range(Q):
        x1 = int(data[idx])
        idx += 1
        y1 = int(data[idx])
        idx += 1
        x2 = int(data[idx])
        idx += 1
        y2 = int(data[idx])
        idx += 1
        queries.append((x1, y1, x2, y2))
    
    # Create a 2D array to track the number of flips
    flip = [[0] * (M + 1) for _ in range(N + 1)]
    
    for x1, y1, x2, y2 in queries:
        flip[x1][y1] += 1
        flip[x2 + 1][y1] -= 1
        flip[x1][y2 + 1] -= 1
        flip[x2 + 1][y2 + 1] += 1
    
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            flip[i][j] += flip[i - 1][j]
            flip[i][j] += flip[i][j - 1]
            flip[i][j] -= flip[i - 1][j - 1]
    
    for i in range(N):
        for j in range(M):
            matrix[i][j] = 1 - matrix[i][j] if flip[i + 1][j + 1] % 2 else matrix[i][j]
    
    for row in matrix:
        print(''.join(map(str, row)))

if __name__ == '__main__':
    solve()