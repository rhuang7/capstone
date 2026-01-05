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
        # Count the number of available cells that can be claimed
        # A cell can be claimed if it is 0 and its row and column are not used
        # So we need to find the maximum number of non-conflicting cells
        # This is equivalent to finding the maximum matching in a bipartite graph
        # where one set is rows and the other is columns, and an edge exists if the cell is 0
        # The maximum matching will give the maximum number of cells that can be claimed
        # The winner is determined by whether this number is odd or even
        # So we need to find the maximum matching
        # We can model this as a bipartite graph and use a standard maximum bipartite matching algorithm
        # Let's create a bipartite graph where rows are on one side and columns on the other
        # and an edge exists between row i and column j if grid[i][j] == 0
        # Then find the maximum matching
        # Let's implement the standard DFS-based maximum bipartite matching algorithm
        # Create a graph
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    graph[i].append(j)
        # Now find maximum matching
        match_to = [-1] * m  # match_to[j] = i if column j is matched to row i
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
        # If the number of matched cells is odd, Ashish wins, else Vivek
        if result % 2 == 1:
            results.append("Ashish")
        else:
            results.append("Vivek")
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()