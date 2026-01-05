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
                c1 = grid[i][j]
                c2 = grid[i][j+1]
                c3 = grid[i+1][j]
                c4 = grid[i+1][j+1]
                if c1 == c2 == c3 == c4:
                    count += 1
        results.append(str(count))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()