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
        # If count is 0, Vivek wins
        # Else, if count is odd, Ashish wins, else Vivek
        if count == 0:
            results.append("Vivek")
        else:
            if count % 2 == 1:
                results.append("Ashish")
            else:
                results.append("Vivek")
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()