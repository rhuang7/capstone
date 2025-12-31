import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        grid = []
        for _ in range(N):
            row = list(map(int, data[idx:idx+N]))
            grid.append(row)
            idx += N
        unsafe = False
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    # Check all 8 adjacent cells
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if dx == 0 and dy == 0:
                                continue
                            ni, nj = i + dx, j + dy
                            if 0 <= ni < N and 0 <= nj < N:
                                if grid[ni][nj] == 1:
                                    unsafe = True
                                    break
                        if unsafe:
                            break
                    if unsafe:
                        break
            if unsafe:
                break
        print("SAFE" if not unsafe else "UNSAFE")

if __name__ == '__main__':
    solve()