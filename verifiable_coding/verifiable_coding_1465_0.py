import sys
import math

MOD = 10**9 + 7

def main():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        n, Q = int(data[idx]), int(data[idx+1])
        idx += 2
        edges = [[] for _ in range(n+1)]
        for _ in range(n-1):
            u = int(data[idx])
            v = int(data[idx+1])
            edges[u].append(v)
            edges[v].append(u)
            idx += 2
        conditions = []
        for _ in range(Q):
            u = int(data[idx])
            v = int(data[idx+1])
            x = int(data[idx+2])
            conditions.append((u, v, x))
            idx += 3
        
        # Build the tree and find the number of connected components
        # Since it's a tree, it's connected, so we can choose a root and perform BFS/DFS
        # We'll use BFS to assign parent and depth for each node
        parent = [0]*(n+1)
        depth = [0]*(n+1)
        visited = [False]*(n+1)
        from collections import deque
        q = deque()
        q.append(1)
        visited[1] = True
        while q:
            u = q.popleft()
            for v in edges[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    q.append(v)
        
        # Build the path between u and v
        # For each condition, find the LCA and build the path
        # We'll use the parent array to find the path
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            # Bring u to the same depth as v
            while depth[u] > depth[v]:
                u = parent[u]
            # Now find LCA
            while u != v:
                u = parent[u]
                v = parent[v]
            return u
        
        # For each condition, find the path from u to v
        # We'll store the path as a list of edges
        # We'll also store the parity (even/odd) required for the path
        # The parity is determined by the sum of the edge weights
        # We'll use a system of equations to represent the constraints
        # Each edge can be 0 or 1, so we have variables x_e for each edge
        # The constraints are sum(x_e for e in path) ≡ x (mod 2)
        # We'll represent this as a system of linear equations mod 2
        # The number of variables is the number of edges (n-1)
        # The number of equations is Q
        # We'll use Gaussian elimination mod 2 to solve the system
        # The answer is 2^(number of free variables)
        
        # Build the system of equations
        # Each equation is a row in the matrix
        # Each column corresponds to an edge
        # We'll assign each edge an index
        # We'll build the adjacency list with edge indices
        edge_index = {}
        edge_count = 0
        for u in range(1, n+1):
            for v in edges[u]:
                if u < v:
                    edge_index[(u, v)] = edge_count
                    edge_count += 1
        
        # Build the matrix
        matrix = []
        for u, v, x in conditions:
            # Find the path from u to v
            l = lca(u, v)
            path = []
            # Go from u to l
            a = u
            while a != l:
                b = parent[a]
                path.append((a, b))
                a = b
            # Go from v to l
            a = v
            while a != l:
                b = parent[a]
                path.append((a, b))
                a = b
            # Reverse the path to get from u to v
            path = path[::-1]
            # For each edge in the path, add its index to the equation
            # The equation is sum(x_e for e in path) ≡ x (mod 2)
            row = [0]*(edge_count)
            for a, b in path:
                if a < b:
                    idx = edge_index[(a, b)]
                else:
                    idx = edge_index[(b, a)]
                row[idx] = 1
            # The right-hand side is x
            matrix.append(row + [x])
        
        # Perform Gaussian elimination mod 2
        rank = 0
        for col in range(edge_count):
            # Find a pivot row
            pivot = -1
            for r in range(rank, len(matrix)):
                if matrix[r][col] == 1:
                    pivot = r
                    break
            if pivot == -1:
                continue
            # Swap rows
            matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
            # Eliminate this column in other rows
            for r in range(len(matrix)):
                if r != rank and matrix[r][col] == 1:
                    for c in range(col, edge_count+1):
                        matrix[r][c] ^= matrix[rank][c]
            rank += 1
        
        # The number of free variables is (number of variables - rank)
        # The answer is 2^free_vars mod MOD
        free_vars = edge_count - rank
        ans = pow(2, free_vars, MOD)
        print(ans)

if __name__ == '__main__':
    main()