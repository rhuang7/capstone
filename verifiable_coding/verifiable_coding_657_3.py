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
    from itertools import product

    for row_toggle in product([0, 1], repeat=m):
        for col_toggle in product([0, 1], repeat=n):
            score = 0
            for i in range(m):
                for j in range(n):
                    if row_toggle[i] == 1:
                        grid[i][j] = 1 - grid[i][j]
                    if col_toggle[j] == 1:
                        grid[i][j] = 1 - grid[i][j]
                    # Calculate the binary value of the row
                    score += grid[i][j] * (1 << (n - 1 - j))
            max_score = max(max_score, score)
            # Revert the changes for next iteration
            for i in range(m):
                if row_toggle[i] == 1:
                    grid[i][j] = 1 - grid[i][j]
                if col_toggle[j] == 1:
                    grid[i][j] = 1 - grid[i][j]

    print(max_score)

if __name__ == '__main__':
    solve()