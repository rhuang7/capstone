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
        grid = []
        for _ in range(n):
            row = list(map(int, data[idx:idx+m]))
            grid.append(row)
            idx += m
        # Find the number of available cells that can be claimed
        # A cell can be claimed if it is 0 and its row and column are not used
        used_rows = set()
        used_cols = set()
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    if i not in used_rows and j not in used_cols:
                        count += 1
                        used_rows.add(i)
                        used_cols.add(j)
        # Determine the winner based on the count
        if count % 2 == 1:
            results.append("Ashish")
        else:
            results.append("Vivek")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()