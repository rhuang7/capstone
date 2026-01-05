import sys
import math
from collections import defaultdict, deque

MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        n, Q = int(data[idx]), int(data[idx+1])
        idx += 2
        
        # Build tree
        tree = defaultdict(list)
        for _ in range(n-1):
            u = int(data[idx])
            v = int(data[idx+1])
            tree[u].append(v)
            tree[v].append(u)
            idx += 2
        
        # Process queries
        conditions = []
        for _ in range(Q):
            u = int(data[idx])
            v = int(data[idx+1])
            x = int(data[idx+2])
            conditions.append((u, v, x))
            idx += 3
        
        # BFS to compute parent and depth for each node
        parent = [0] * (n + 1)
        depth = [0] * (n + 1)
        visited = [False] * (n + 1)
        q = deque()
        q.append(1)
        visited[1] = True
        while q:
            u = q.popleft()
            for v in tree[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    q.append(v)
        
        # Compute XOR from root to each node
        xor_to_node = [0] * (n + 1)
        for i in range(2, n+1):
            xor_to_node[i] = xor_to_node[parent[i]] ^ 1
        
        # For each condition, compute the XOR of the path from u to v
        # XOR of path u to v is xor_to_node[u] ^ xor_to_node[v]
        # If x is 0, the XOR must be even (0), if x is 1, it must be odd (1)
        # So for each condition, we have a constraint on the XOR of the path
        # We can model this as a system of linear equations over GF(2)
        # Each equation is: xor_path(u, v) = x
        
        # We can represent the equations as variables (edges) and equations (constraints)
        # The variables are the edges, and the equations are the constraints on the XOR of the path
        # We can use BFS to find the equations and build a system
        
        # Build equations
        equations = []
        for u, v, x in conditions:
            # XOR of path u to v is xor_to_node[u] ^ xor_to_node[v]
            # So the equation is: xor_to_node[u] ^ xor_to_node[v] ^ (sum of edges on path) = x
            # Which is equivalent to: sum of edges on path = (xor_to_node[u] ^ xor_to_node[v] ^ x)
            # We can represent this as a system of equations
            # We can use BFS to find the edges on the path from u to v
            # Then, for each edge on the path, we add it to the equation
            
            # Find the path from u to v
            path = []
            a, b = u, v
            while a != b:
                if depth[a] > depth[b]:
                    path.append(a)
                    a = parent[a]
                else:
                    path.append(b)
                    b = parent[b]
            path.append(a)
            path.reverse()
            
            # The edges on the path are between consecutive nodes in path
            edges_on_path = []
            for i in range(len(path)-1):
                u_edge = path[i]
                v_edge = path[i+1]
                if u_edge < v_edge:
                    edges_on_path.append((u_edge, v_edge))
                else:
                    edges_on_path.append((v_edge, u_edge))
            
            # The equation is: sum of edges on path = (xor_to_node[u] ^ xor_to_node[v] ^ x)
            # We can represent this as a linear equation over GF(2)
            # We can use a system of equations to solve this
            
            # For each equation, we can represent it as a row in a matrix
            # The variables are the edges (each edge is a variable)
            # The right-hand side is the value of the equation
            
            # We can represent the equations as a list of (coefficients, rhs)
            # Each coefficient is 1 if the edge is in the path, 0 otherwise
            # The rhs is (xor_to_node[u] ^ xor_to_node[v] ^ x)
            rhs = (xor_to_node[u] ^ xor_to_node[v] ^ x)
            equation = [0] * (n-1)
            for u_edge, v_edge in edges_on_path:
                # Find the index of the edge (u_edge, v_edge)
                # We can use a set to store edges
                edge_set = set()
                for i in range(n-1):
                    u_edge_i = tree[i+1][0]
                    v_edge_i = tree[i+1][1]
                    if u_edge_i < v_edge_i:
                        edge_set.add((u_edge_i, v_edge_i))
                    else:
                        edge_set.add((v_edge_i, u_edge_i))
                # Find the index of the edge (u_edge, v_edge)
                # We can use a dictionary to map edges to their index
                edge_to_index = {}
                for i in range(n-1):
                    u_edge_i = tree[i+1][0]
                    v_edge_i = tree[i+1][1]
                    if u_edge_i < v_edge_i:
                        edge = (u_edge_i, v_edge_i)
                    else:
                        edge = (v_edge_i, u_edge_i)
                    edge_to_index[edge] = i
                # Get the index of the edge
                edge = (u_edge, v_edge)
                if edge in edge_to_index:
                    equation[edge_to_index[edge]] = 1
            equations.append((equation, rhs))
        
        # Now we have a system of linear equations over GF(2)
        # We can use Gaussian elimination over GF(2) to solve this system
        
        # Number of variables is n-1
        # Number of equations is Q
        # We can represent the system as a matrix (augmented)
        # Each row is an equation: coefficients + rhs
        # We can perform Gaussian elimination
        
        # Initialize the matrix
        rows = len(equations)
        cols = n-1 + 1  # n-1 variables + 1 rhs
        
        matrix = []
        for i in range(rows):
            row = [0] * cols
            for j in range(n-1):
                row[j] = equations[i][0][j]
            row[-1] = equations[i][1]
            matrix.append(row)
        
        # Perform Gaussian elimination over GF(2)
        rank = 0
        for col in range(n-1):
            # Find pivot
            pivot = -1
            for row in range(rank, rows):
                if matrix[row][col] == 1:
                    pivot = row
                    break
            if pivot == -1:
                continue
            # Swap rows
            matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
            # Eliminate other rows
            for row in range(rows):
                if row != rank and matrix[row][col] == 1:
                    for c in range(col, n-1 + 1):
                        matrix[row][c] ^= matrix[rank][c]
            rank += 1
        
        # Now, check for inconsistencies
        # For each row, if all coefficients are 0 but rhs is 1, it's inconsistent
        for row in range(rank, rows):
            if matrix[row][n-1] == 1:
                # Inconsistent system
                results.append(0)
                break
        else:
            # The number of free variables is (n-1 - rank)
            # Each free variable can be 0 or 1, so the number of solutions is 2^(number of free variables)
            free_vars = (n-1) - rank
            if free_vars < 0:
                free_vars = 0
            results.append(pow(2, free_vars, MOD))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()