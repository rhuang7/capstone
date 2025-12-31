import sys
import math

MOD = 10**9 + 7

def main():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        n, Q = int(data[idx]), int(data[idx+1])
        idx += 2
        
        # Build the tree
        adj = [[] for _ in range(n+1)]
        for _ in range(n-1):
            u = int(data[idx])
            v = int(data[idx+1])
            adj[u].append(v)
            adj[v].append(u)
            idx += 2
        
        # Process conditions
        conditions = []
        for _ in range(Q):
            u = int(data[idx])
            v = int(data[idx+1])
            x = int(data[idx+2])
            conditions.append((u, v, x))
            idx += 3
        
        # We need to find the number of valid assignments of 0/1 to edges
        # such that for each condition, the sum of weights on the path from u to v is even or odd.
        # This is a system of linear equations over GF(2)
        
        # We will represent the edges as variables and build the system of equations
        
        # Assign each edge a unique index
        edge_index = 0
        edge_to_index = {}
        for u in range(1, n+1):
            for v in adj[u]:
                if u < v:
                    edge_to_index[(u, v)] = edge_index
                    edge_index += 1
        
        # Build the system of equations
        # Each equation is of the form: sum of variables (edges on path) ≡ x (mod 2)
        # We will represent this as a matrix where each row is an equation
        
        # To solve this, we can use Gaussian elimination over GF(2)
        # We will represent the system as a matrix of size (Q x (n-1))
        # Each row is an equation, each column is a variable (edge)
        
        # We'll also need to track the rank of the system and the number of free variables
        # The number of solutions is 2^k, where k is the number of free variables
        
        # Build the matrix
        matrix = []
        for u, v, x in conditions:
            # Find the path from u to v
            # We'll use BFS to find the path
            # But since it's a tree, there's exactly one path
            # We can use DFS or BFS to find the path
            # We'll use BFS
            path = []
            visited = [False] * (n+1)
            queue = [(u, [u])]
            while queue:
                node, path_so_far = queue.pop(0)
                if node == v:
                    path = path_so_far
                    break
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append((neighbor, path_so_far + [neighbor]))
            # Now, path is the list of nodes from u to v
            # We need to find the edges on this path
            # Each consecutive pair in the path is an edge
            equation = [0] * (n-1)
            for i in range(len(path)-1):
                a, b = path[i], path[i+1]
                if a < b:
                    edge = (a, b)
                else:
                    edge = (b, a)
                equation[edge_to_index[edge]] = 1
            # The equation is sum(equation[i] * x_i) ≡ x (mod 2)
            # So we add this row to the matrix
            matrix.append(equation + [x])
        
        # Now perform Gaussian elimination over GF(2)
        rank = 0
        rows = len(matrix)
        cols = len(matrix[0]) - 1  # number of variables
        
        for col in range(cols):
            # Find a row with a 1 in this column
            pivot_row = -1
            for r in range(rank, rows):
                if matrix[r][col] == 1:
                    pivot_row = r
                    break
            if pivot_row == -1:
                continue  # no pivot, move to next column
            
            # Swap the pivot row with the current rank row
            matrix[rank], matrix[pivot_row] = matrix[pivot_row], matrix[rank]
            
            # Eliminate all other rows with a 1 in this column
            for r in range(rows):
                if r != rank and matrix[r][col] == 1:
                    # XOR the current row with the pivot row
                    for c in range(col, cols+1):
                        matrix[r][c] ^= matrix[rank][c]
            rank += 1
        
        # The number of free variables is (number of variables - rank)
        free_vars = cols - rank
        # The number of solutions is 2^free_vars
        if free_vars < 0:
            # Inconsistent system, no solution
            results.append(0)
        else:
            results.append(pow(2, free_vars, MOD))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    main()