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
        # Count the number of available cells that can be chosen
        # A cell can be chosen if it is 0 and its row and column are not used
        # We can model this as a bipartite graph matching problem
        # But since the game is turn-based and both players play optimally, the winner is determined by the parity of the maximum number of non-conflicting cells
        # We can find the maximum number of non-conflicting cells by finding the maximum matching in a bipartite graph
        # However, since the grid is small (n, m <= 50), we can use a greedy approach
        # We can find the maximum number of non-conflicting cells by selecting cells in such a way that no two selected cells share a row or column
        # We can model this as a bipartite graph where one set is rows and the other is columns
        # An edge exists between row i and column j if the cell (i, j) is 0
        # The maximum matching in this graph gives the maximum number of non-conflicting cells
        # The winner is determined by whether this number is even or odd
        # If the number is even, Vivek wins; if odd, Ashish wins
        # So we need to find the maximum number of non-conflicting cells
        # We can model this as a bipartite graph and find the maximum matching
        # We can use the standard maximum bipartite matching algorithm
        # Let's build the bipartite graph
        # Rows are on one side, columns on the other
        # For each cell (i, j) that is 0, add an edge between row i and column j
        # Then find the maximum matching
        # The size of the maximum matching is the maximum number of non-conflicting cells
        # The winner is determined by whether this number is even or odd
        # So we need to find the maximum matching
        # Let's implement the standard DFS-based maximum bipartite matching algorithm
        # Create a graph where rows are on one side, columns on the other
        # For each row, we can connect to columns where the cell is 0
        # Now find the maximum matching
        # The maximum matching size is the maximum number of non-conflicting cells
        # The winner is determined by whether this number is even or odd
        # If it is even, Vivek wins; if odd, Ashish wins
        # So let's proceed
        # Create adjacency list for rows to columns
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    graph[i].append(j)
        # Now find maximum bipartite matching
        # We'll use the standard DFS-based approach
        # We'll use a visited array and a match_to array for columns
        match_to = [-1] * m
        def bpm(u, visited):
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    if match_to[v] == -1 or bpm(match_to[v], visited):
                        match_to[v] = u
                        return True
            return False
        result = 0
        for u in range(n):
            visited = [False] * m
            if bpm(u, visited):
                result += 1
        # Now determine the winner
        if result % 2 == 1:
            results.append("Ashish")
        else:
            results.append("Vivek")
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()