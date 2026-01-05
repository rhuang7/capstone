import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    m = int(input[0])
    n = int(input[1])
    grid = []
    idx = 2
    for _ in range(m):
        row = list(map(int, input[idx:idx+n]))
        grid.append(row)
        idx += n

    max_score = 0

    # Try all possible combinations of row and column toggles
    # Since m and n are up to 20, 2^20 is about 1 million, which is manageable
    for row_mask in range(1 << m):
        for col_mask in range(1 << n):
            score = 0
            for i in range(m):
                for j in range(n):
                    # Check if row i is toggled
                    if (row_mask >> i) & 1:
                        grid[i][j] = 1 - grid[i][j]
                    # Check if column j is toggled
                    if (col_mask >> j) & 1:
                        grid[i][j] = 1 - grid[i][j]
                    # Calculate the binary value of the row
                    score += grid[i][j] * (1 << (n - 1 - j))
                # Reset the grid after processing each row
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j] if (row_mask >> i) & 1 else grid[i][j]
            max_score = max(max_score, score)

    print(max_score)

if __name__ == '__main__':
    solve()