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
        
        # Count the number of available cells that can be claimed
        # A cell can be claimed if it is 0 and its row and column are not used
        # So we need to find the maximum number of non-conflicting cells
        # This is equivalent to finding the maximum matching in a bipartite graph
        # where one set is rows and the other is columns, and an edge exists if the cell is 0
        # The maximum matching gives the maximum number of cells that can be claimed
        # The winner is determined by whether this number is odd or even
        
        # Create a bipartite graph
        # Rows on one side, columns on the other
        # Edge exists if cell is 0
        # Find maximum matching using DFS-based approach
        
        # Initialize row and column usage
        row_used = [False] * n
        col_used = [False] * m
        
        # Function to find augmenting path
        def bpm(u, visited):
            for v in range(m):
                if not col_used[v] and grid[u][v] == 0:
                    col_used[v] = True
                    for i in range(n):
                        if not row_used[i] and grid[i][v] == 0:
                            row_used[i] = True
                            if not visited[i]:
                                visited[i] = True
                                if not bpm(i, visited):
                                    row_used[i] = False
                                    col_used[v] = False
                                    return True
                    return False
            return False
        
        # Find maximum matching
        match = 0
        row_used = [False] * n
        col_used = [False] * m
        for u in range(n):
            visited = [False] * n
            if bpm(u, visited):
                match += 1
        
        # Determine the winner
        if match % 2 == 1:
            results.append("Ashish")
        else:
            results.append("Vivek")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()