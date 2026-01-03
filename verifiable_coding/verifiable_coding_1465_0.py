import sys
import math

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
        tree = [[] for _ in range(n+1)]
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
        
        # Use BFS to find parent and depth for each node
        parent = [0]*(n+1)
        depth = [0]*(n+1)
        visited = [False]*(n+1)
        from collections import deque
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
        
        # Build equations
        # Each edge is between parent and child
        # For each condition, we need to find the XOR of the path from u to v
        # We can represent the path as the XOR from root to u XOR root to v
        # So we need to find the XOR from root to each node
        # Let's compute that
        xor_to_root = [0]*(n+1)
        visited = [False]*(n+1)
        q = deque()
        q.append(1)
        visited[1] = True
        while q:
            u = q.popleft()
            for v in tree[u]:
                if not visited[v]:
                    visited[v] = True
                    xor_to_root[v] = xor_to_root[u] ^ 1
                    q.append(v)
        
        # Now, for each condition (u, v, x), the XOR of the path from u to v is xor_to_root[u] ^ xor_to_root[v]
        # We need this XOR to be 0 if x is 0, 1 if x is 1
        # So the equation is: xor_to_root[u] ^ xor_to_root[v] == x
        # Which can be rewritten as: xor_to_root[u] ^ xor_to_root[v] ^ x == 0
        # This is a linear equation in GF(2)
        # We need to form a system of linear equations over GF(2)
        # The variables are the edges, which can be represented as the XOR from parent to child
        # For each edge between parent and child, we can represent it as a variable
        # So, for each node (except root), we have an edge from parent to node
        # Let's assign variables to edges
        # Let's create a list of variables, where variable[i] is the edge from parent[i] to i
        # Then, for each condition, we can find the XOR of the path from u to v
        # Which is the XOR of the variables along the path
        # So, we can represent this as a linear equation in GF(2)
        # We need to find the number of solutions to this system of equations
        # The number of solutions is 2^(number of free variables)
        # So, we need to find the rank of the system and the number of free variables
        
        # Let's create the system of equations
        # Each equation is a row in a matrix
        # Each variable is a column in the matrix
        # The variables are the edges from parent to child
        # So, for each node i (except root), we have a variable
        # So, total variables is n-1
        # Let's create a list of variables, where variable[i] is the edge from parent[i] to i
        # So, for each node i (except root), variable[i] is the edge between parent[i] and i
        # Now, for each condition (u, v, x), we need to find the XOR of the path from u to v
        # Which is the XOR of the variables along the path from u to v
        # So, we can represent this as a linear equation
        # Let's find the XOR of the path from u to v
        # This can be done by finding the XOR of the path from root to u and root to v
        # So, the XOR of the path from u to v is xor_to_root[u] ^ xor_to_root[v]
        # So, the equation is: xor_to_root[u] ^ xor_to_root[v] ^ x == 0
        # Which is equivalent to: xor_to_root[u] ^ xor_to_root[v] == x
        # This is a linear equation in GF(2)
        # So, for each condition, we can create an equation
        # Now, we need to build the system of equations and find the number of solutions
        
        # Let's create a list of equations
        # Each equation is a list of coefficients (0 or 1), and a constant (0 or 1)
        # The coefficients represent the variables in the equation
        # The constant is the right-hand side of the equation
        # We can represent this as a matrix, where each row is an equation
        
        # Let's create a list of equations
        equations = []
        # Also, we need to find the variables (edges) that are involved in each equation
        # For each condition (u, v, x), we need to find the path from u to v and create an equation
        # Let's find the path from u to v
        # We can find the LCA (lowest common ancestor) of u and v
        # Then, the path from u to v is u to LCA, then LCA to v
        # But for the purpose of building the equations, we can just find the XOR of the path
        # Which is xor_to_root[u] ^ xor_to_root[v]
        # So, the equation is: xor_to_root[u] ^ xor_to_root[v] == x
        # Which is equivalent to: xor_to_root[u] ^ xor_to_root[v] ^ x == 0
        # So, we can represent this as a linear equation
        
        # Now, let's create the equations
        for u, v, x in conditions:
            # The XOR of the path from u to v is xor_to_root[u] ^ xor_to_root[v]
            # The equation is: xor_to_root[u] ^ xor_to_root[v] == x
            # Which is equivalent to: xor_to_root[u] ^ xor_to_root[v] ^ x == 0
            # So, we need to create an equation with coefficients for the variables
            # The variables are the edges from parent to child
            # So, we need to find the path from u to v and find which edges are involved
            # For each edge in the path, we have a variable
            # Let's find the path from u to v
            # We can do this by finding the LCA of u and v
            # But for this problem, we can find the path by moving up from u and v to their common ancestor
            # Let's find the path from u to v
            # We can do this by moving up from u and v until they meet
            # Let's find the path
            path_u = []
            path_v = []
            # Move u up to root
            while u != 1:
                path_u.append(u)
                u = parent[u]
            # Move v up to root
            while v != 1:
                path_v.append(v)
                v = parent[v]
            # Now, find the common ancestor
            # We can reverse the path_v and compare with path_u
            # Let's find the LCA
            lca = 1
            for i in range(len(path_u)):
                if path_u[i] in path_v:
                    lca = path_u[i]
                    break
            # Now, the path from u to v is u to lca, then lca to v
            # But for the purpose of building the equations, we need to find which edges are in the path
            # So, for each node in the path from u to lca, we have an edge from parent to node
            # Similarly for the path from v to lca
            # So, for the path from u to lca, we can add the edges
            # For the path from v to lca, we can add the edges
            # So, the total edges in the path are the edges from u to lca and from v to lca
            # But since lca is the common ancestor, we can find the edges in the path
            # Let's find the edges in the path from u to v
            # We can do this by traversing from