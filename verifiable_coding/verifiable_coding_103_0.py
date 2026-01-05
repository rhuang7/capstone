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
        for i in range(n):
            row = list(map(int, data[idx:idx+m]))
            grid.append(row)
            idx += m
        # Count the number of cells that can be claimed
        # A cell can be claimed if it is unclaimed and its row and column are not already claimed
        # So we need to find the maximum number of non-attacking rooks that can be placed
        # This is equivalent to finding the maximum matching in a bipartite graph
        # But since the grid is small, we can simulate it
        # We can find the number of rows and columns that have at least one 1
        # The answer is the minimum between the number of rows with 1s and columns with 1s
        # Because each 1 in a row and column blocks that row and column
        # So the maximum number of moves is the minimum of the count of rows with 1s and columns with 1s
        row_ones = 0
        col_ones = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    row_ones += 1
                    col_ones += 1
        # But we need to count the number of rows and columns that have at least one 1
        row_has_one = [False] * n
        col_has_one = [False] * m
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    row_has_one[i] = True
                    col_has_one[j] = True
        row_count = sum(row_has_one)
        col_count = sum(col_has_one)
        max_moves = min(row_count, col_count)
        # If max_moves is even, Vivek wins; else Ashish wins
        if max_moves % 2 == 0:
            results.append("Vivek")
        else:
            results.append("Ashish")
    print("\n".join(results))

if __name__ == '__main__':
    solve()