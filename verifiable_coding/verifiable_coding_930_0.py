import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        N = int(input[idx])
        idx += 1
        grid = [[0] * N for _ in range(N)]
        num = 1
        for i in range(N):
            for j in range(N):
                if i == 0 and j == 0:
                    grid[i][j] = num
                    num += 1
                elif i == 0:
                    grid[i][j] = grid[i][j-1] + num
                    num += 1
                elif j == 0:
                    grid[i][j] = grid[i-1][j] + num
                    num += 1
                else:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1] - grid[i-1][j-1] + num
                    num += 1
        for row in grid:
            print(' '.join(map(str, row)))

if __name__ == '__main__':
    solve()