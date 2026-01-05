import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    m = int(data[0])
    n = int(data[1])
    grid = []
    index = 2
    for _ in range(m):
        row = list(map(int, data[index:index+n]))
        grid.append(row)
        index += n

    max_score = 0

    # Try all possible combinations of row and column toggles
    # Since m and n are up to 20, 2^20 is too big, but 2^20 is manageable with bit manipulation
    # We can represent the row toggles as a bitmask of m bits, and column toggles as a bitmask of n bits
    # For each combination of row and column toggles, compute the score

    # Precompute the binary values for each row
    row_values = []
    for row in grid:
        val = 0
        for j in range(n):
            val = (val << 1) | row[j]
        row_values.append(val)

    # Try all possible row toggle combinations
    for row_mask in range(1 << m):
        # Apply row toggles
        toggled_rows = []
        for i in range(m):
            row = grid[i]
            toggled_row = []
            for j in range(n):
                if (row_mask >> i) & 1:
                    toggled_row.append(1 - row[j])
                else:
                    toggled_row.append(row[j])
            toggled_rows.append(toggled_row)

        # Try all possible column toggle combinations
        for col_mask in range(1 << n):
            score = 0
            for i in range(m):
                row = toggled_rows[i]
                val = 0
                for j in range(n):
                    if (col_mask >> j) & 1:
                        val = (val << 1) | (1 - row[j])
                    else:
                        val = (val << 1) | row[j]
                score += val
            max_score = max(max_score, score)

    print(max_score)

if __name__ == '__main__':
    solve()