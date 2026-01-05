import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    m = int(data[0])
    n = int(data[1])
    grid = []
    idx = 2
    for _ in range(m):
        row = list(map(int, data[idx:idx+n]))
        grid.append(row)
        idx += n

    max_score = 0

    # Try all possible combinations of row and column toggles
    # Since m and n are up to 20, 2^20 is manageable
    for row_toggle in range(1 << m):
        for col_toggle in range(1 << n):
            score = 0
            # Apply row toggles
            for i in range(m):
                if row_toggle & (1 << i):
                    for j in range(n):
                        grid[i][j] = 1 - grid[i][j]
            # Apply column toggles
            for j in range(n):
                if col_toggle & (1 << j):
                    for i in range(m):
                        grid[i][j] = 1 - grid[i][j]
            # Calculate score
            for i in range(m):
                num = 0
                for j in range(n):
                    num = (num << 1) | grid[i][j]
                score += num
            # Reset grid
            for i in range(m):
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j] if (row_toggle & (1 << i)) or (col_toggle & (1 << j)) else grid[i][j]
            max_score = max(max_score, score)

    print(max_score)

if __name__ == '__main__':
    solve()