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
        row = list(map(int, data[idx:idx + m]))
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
    prefix = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            prefix[i][j] = grid[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]
    
    for px, py, qx, qy in queries:
        res = prefix[qx][qy] - prefix[px - 1][qy] - prefix[qx][py - 1] + prefix[px - 1][py - 1]
        print(res)

if __name__ == '__main__':
    solve()