import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    grid = []
    for _ in range(n):
        row = list(map(int, data[idx:idx+m]))
        grid.append(row)
        idx += m
    t = int(data[idx])
    idx += 1
    queries = []
    for _ in range(t):
        px = int(data[idx])
        idx += 1
        py = int(data[idx])
        idx += 1
        qx = int(data[idx])
        idx += 1
        qy = int(data[idx])
        idx += 1
        queries.append((px, py, qx, qy))
    
    # Precompute prefix sums
    prefix = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            prefix[i][j] = grid[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
    
    for px, py, qx, qy in queries:
        # Convert to 1-based to 0-based
        px_0 = px - 1
        py_0 = py - 1
        qx_0 = qx - 1
        qy_0 = qy - 1
        # Use prefix sums to get the sum in the rectangle
        sum_rect = prefix[qx_0+1][qy_0+1] - prefix[px_0][qy_0+1] - prefix[qx_0+1][py_0] + prefix[px_0][py_0]
        print(sum_rect)

if __name__ == '__main__':
    solve()