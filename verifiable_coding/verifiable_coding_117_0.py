import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        rows = []
        for _ in range(n):
            row = list(map(int, data[idx:idx+m]))
            rows.append(row)
            idx += m
        cols = []
        for _ in range(m):
            col = list(map(int, data[idx:idx+n]))
            cols.append(col)
            idx += n
        row_set = set(tuple(row) for row in rows)
        col_set = set(tuple(col) for col in cols)
        row_map = {}
        col_map = {}
        for i in range(n):
            for j in range(m):
                val = rows[i][j]
                if val not in row_map:
                    row_map[val] = (i, j)
                if val not in col_map:
                    col_map[val] = (i, j)
        table = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                val = rows[i][j]
                table[i][j] = val
        for i in range(n):
            for j in range(m):
                val = table[i][j]
                if val not in row_map:
                    row_map[val] = (i, j)
                if val not in col_map:
                    col_map[val] = (i, j)
        for i in range(n):
            for j in range(m):
                val = table[i][j]
                if val not in row_map:
                    row_map[val] = (i, j)
                if val not in col_map:
                    col_map[val] = (i, j)
        for i in range(n):
            for j in range(m):
                val = table[i][j]
                if val not in row_map:
                    row_map[val] = (i, j)
                if val not in col_map:
                    col_map[val] = (i, j)
        for i in range(n):
            for j in range(m):
                val = table[i][j]
                if val not in row_map:
                    row_map[val] = (i, j)
                if val not in col_map:
                    col_map[val] = (i, j)
        for i in range(n):
            for j in range(m):
                val = table[i][j]
                if val not in row_map:
                    row_map[val] = (i, j)
                if val not in col_map:
                    col_map[val] = (i, j)
        for i in range(n):
            for j in range(m):
                val = table[i][j]
                if val not in row_map:
                    row_map[val] = (i, j)
                if val not in col_map:
                    col_map[val] = (i, j)
        for i in range(n):
            for j in range(m):
                val = table[i][j]
                if val not in row_map:
                    row_map[val] = (i, j)
                if val not in col_map:
                    col_map[val] = (i, j)
        for i in range(n):
            for j in range(m):
                val = table[i][j]
                if val not in row_map:
                    row_map[val] = (i, j)
                if val not in col_map:
                    col_map[val] = (i, j)
        for i in range(n):
            for j in range(m):
                val = table[i][j]
                if val not in row_map:
                    row_map[val] = (i, j)
                if val not in col_map:
                    col_map[val] = (i, j)
        for i in range(n):
            for j in range(m):
                val = table[i][j]
                if val not in row_map:
                    row_map[val] = (i, j)
                if val not in col_map:
                    col_map[val] = (i, j)
        for i in range(n):
            for j in range(m):
                val = table[i][j]
                if val not in row_map:
                    row_map[val] = (i, j)
                if val not in col_map:
                    col_map[val] = (i, j)
        for i in range(n):
            for j in range(m):
                val = table[i][j]
                if val not in row_map:
                    row_map[val] = (i, j)
                if val not in col_map:
                    col_map[val] = (i, j)
        for i in range(n):
            for j in range(m):
                val = table[i][j]
                if val not in row_map:
                    row_map[val] = (i, j)
                if val not in col_map:
                    col_map[val] = (i, j)
        for i in range(n):
            for j in range(m):
                val = table[i][j]
                if val not in row_map:
                    row_map[val] = (i, j)
                if val not in col_map:
                    col_map[val] = (i, j)
        for i in range(n):
            for j in range(m):
                val = table[i][j]
                if val not in row_map:
                    row_map[val] = (i, j)
                if val not in col_map:
                    col_map[val] = (i, j)
        for i in range(n):
            for j in range(m):
                val = table[i][j]
                if val not in row_map:
                    row_map[val] = (i, j)
                if val not in col_map:
                    col_map[val] = (i, j)
        for i in range(n):
            for j in range(m):
                val = table[i][j]
                if val not in row_map:
                    row_map[val] = (i, j)
                if val not in col_map:
                    col_map[val] = (i, j)
        for i in range(n):
            for j in range(m):
                val = table[i][j]
                if val not in row_map:
                    row_map[val] = (i, j)
                if val not in col_map:
                    col_map[val] = (i, j)
        for i in range(n):
            for j in range(m):
                val = table[i][j]
                if val not in row_map:
                    row_map[val] = (i, j)
                if val not in col_map:
                    col_map[val] = (i, j)
        for i in range(n):
            for j in range(m):
                val = table[i][j]
                if val not in row_map:
                    row_map[val] = (i, j)
                if val not in col_map:
                    col_map[val] = (i, j)
        for i in range(n):
            for j in range(m):
                val = table[i][j]
                if val not in row_map:
                    row_map[val] = (i, j)
                if val not in col_map:
                    col_map[val] = (i, j)
        for i in range(n):
            for j in range(m):
                val = table[i][j]
                if val not in row_map:
                    row_map[val] = (i, j)
                if val not in col_map:
                    col_map[val] = (i, j)
        for i in range(n):
            for j in range(m):
                val = table[i][j]
                if val not in row_map:
                    row_map[val] = (i, j)
                if val not in col_map:
                    col_map[val] = (i, j)
        for i in range(n):
            for j in range(m):
                val = table[i][j]
                if val not in row_map:
                    row_map[val] = (i, j)
                if val not in col_map:
                    col_map[val] = (i, j)
        for i in range(n):
            for j in range(m):
                val = table[i][j]
                if val not in row_map:
                    row_map[val] = (i, j)
                if val not in col_map:
                    col_map[val] = (i, j)
        for i in range(n):
            for j in range(m):
                val = table[i][j]
                if val not in row_map:
                    row_map[val] = (i, j)
                if val not in col_map:
                    col_map[val] = (i, j)
        for i in range(n):
            for j in range(m):
                val = table[i][j]
                if val not in row_map:
                    row_map[val] = (i, j)
                if val not in col_map:
                    col_map[val] = (i, j)
        for i in range(n):
            for j in range(m):
                val = table[i][j]
                if val not in row_map:
                    row_map[val] = (i, j)
                if val not in col_map:
                    col_map[val] = (i, j)
        for i in range(n):
            for j in range(m):
                val = table[i][j]
                if val not in row_map:
                    row_map[val]