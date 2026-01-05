import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(input[idx])
        M = int(input[idx+1])
        idx += 2
        grid = []
        for _ in range(N):
            grid.append(input[idx])
            idx += 1
        count = 0
        for i in range(N - 1):
            for j in range(M - 1):
                color = grid[i][j]
                if grid[i][j] == grid[i][j+1] == grid[i+1][j] == grid[i+1][j+1] == color:
                    count += 1
        results.append(str(count))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()