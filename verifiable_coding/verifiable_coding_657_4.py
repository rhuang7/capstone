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
    # Since m and n are up to 20, 2^20 is about a million, which is manageable
    from itertools import product

    for row_toggle in product([0, 1], repeat=m):
        for col_toggle in product([0, 1], repeat=n):
            score = 0
            for i in range(m):
                for j in range(n):
                    val = grid[i][j]
                    if row_toggle[i]:
                        val = 1 - val
                    if col_toggle[j]:
                        val = 1 - val
                    score += val * (1 << (n - 1 - j))
            max_score = max(max_score, score)

    print(max_score)

if __name__ == '__main__':
    solve()