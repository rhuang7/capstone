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
        
        # Build the tree
        adj = [[] for _ in range(n+1)]
        for _ in range(n-1):
            u = int(data[idx])
            v = int(data[idx+1])
            adj[u].append(v)
            adj[v].append(u)
            idx += 2
        
        # Process queries
        conditions = []
        for _ in range(Q):
            u = int(data[idx])
            v = int(data[idx+1])
            x = int(data[idx+2])
            conditions.append((u, v, x))
            idx += 3
        
        # Perform BFS to compute parity from root
        # We'll use 1 as the root
        # We'll compute for each node the parity from root
        # Then, for each condition, we'll check if the parity of the path is correct
        # The parity of the path from u to v is (parity[u] + parity[v]) % 2
        # So for each condition, we have (parity[u] + parity[v]) % 2 == x
        # We can model this as a system of equations over GF(2)
        
        # Let's perform BFS to compute parity from root
        from collections import deque
        parity = [0] * (n + 1)
        visited = [False] * (n + 1)
        q = deque()
        q.append(1)
        visited[1] = True
        parent = [0] * (n + 1)
        
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    parity[v] = parity[u] ^ 1
                    q.append(v)
        
        # Now, for each condition, we have (parity[u] + parity[v]) % 2 == x
        # Which is equivalent to (parity[u] + parity[v]) % 2 == x
        # We can model this as equations of the form parity[u] + parity[v] = x (mod 2)
        
        # We'll use a system of equations to find the number of solutions
        # Each equation is of the form a * x + b * y = c (mod 2)
        # We can represent this as a system of linear equations over GF(2)
        # We'll use Gaussian elimination over GF(2)
        
        # Let's create a matrix for the system
        # Each row represents an equation
        # Each column represents a variable (parity of a node)
        # The last column is the right-hand side
        
        # But since the parity of a node is determined by its path from root, we can model the equations
        # as equations between nodes, and the variables are the edges
        # However, since the parity of a node is determined by the sum of the edges on the path from root,
        # we can model the equations as equations between nodes
        
        # Let's collect all the equations
        equations = []
        for u, v, x in conditions:
            # The parity of the path from u to v is (parity[u] + parity[v]) % 2
            # So (parity[u] + parity[v]) % 2 == x
            # Which is equivalent to parity[u] + parity[v] = x (mod 2)
            equations.append((u, v, x))
        
        # Now, we need to find the number of solutions to this system of equations
        # Each equation is of the form parity[u] + parity[v] = x (mod 2)
        # But parity[u] is determined by the path from root, which is fixed
        # So, we can treat the equations as constraints on the parity of nodes
        
        # Let's build the system of equations as a matrix over GF(2)
        # Each equation is a row in the matrix
        # Each variable is the parity of a node (but since parity is determined by the path from root, it's not a variable)
        # So we need to find the number of solutions to the system of equations
        
        # We can model this as a system of equations over GF(2)
        # Let's build a matrix where each row is an equation
        # Each equation is of the form a1 * x1 + a2 * x2 + ... + an * xn = b (mod 2)
        # But since the parity of a node is fixed, we can treat the equations as constraints on the parity of nodes
        
        # Let's collect the equations as constraints between nodes
        # We can represent the equations as a graph where each edge represents an equation
        # But since the equations are between nodes, we can model this as a graph and find the number of solutions
        
        # We can use a union-find data structure with parity information to solve this
        # Each node has a parent and a parity (relative to the parent)
        # We can use a DSU with parity to check for contradictions and count the number of solutions
        
        # Let's implement DSU with parity
        parent = list(range(n + 1))
        rank = [1] * (n + 1)
        parity = [0] * (n + 1)  # parity[i] is the parity of the path from i to parent[i]
        
        def find(u):
            if parent[u] != u:
                orig_parent = parent[u]
                parent[u] = find(orig_parent)
                parity[u] ^= parity[orig_parent]
            return parent[u]
        
        def union(u, v, x):
            # x is the parity of the path from u to v
            # So, parity[u] ^ parity[v] = x
            # Which means parity[u] ^ parity[v] ^ x = 0
            # So, we need to check if u and v are in the same set
            # If they are, we check if the current parity matches the required parity
            # If not, there is a contradiction
            # If they are not, we merge the sets
            root_u = find(u)
            root_v = find(v)
            if root_u == root_v:
                # Check if the current parity matches the required parity
                if (parity[u] ^ parity[v]) != x:
                    return False
                return True
            else:
                # Merge the smaller tree into the larger tree
                if rank[root_u] < rank[root_v]:
                    parent[root_u] = root_v
                    parity[root_u] = parity[u] ^ parity[v] ^ x
                else:
                    parent[root_v] = root_u
                    parity[root_v] = parity[u] ^ parity[v] ^ x
                    if rank[root_u] == rank[root_v]:
                        rank[root_u] += 1
                return True
        
        # Process the equations
        for u, v, x in equations:
            if not union(u, v, x):
                # There is a contradiction, no solution
                results.append(0)
                break
        else:
            # No contradictions, count the number of solutions
            # The number of solutions is 2^k, where k is the number of independent variables
            # The independent variables are the edges that are not constrained by any equation
            # But since the parity of each node is determined by the path from root, we can count the number of free variables
            # The free variables are the edges that are not part of any equation
            # However, since the equations are between nodes, we can count the number of connected components in the graph formed by the equations
            # Each connected component contributes 1 degree of freedom
            # The number of free variables is (number of connected components) - 1
            # But since the equations are between nodes, the number of connected components is the number of connected components in the graph formed by the equations
            # However, since the tree is connected, the equations may form a connected graph
            # So, the number of free variables is (n - 1 - (number of equations)) + (number of connected components in the equations graph)
            # But this is complicated, so we can use the DSU to count the number of connected components
            # The number of connected components in the DSU is the number of roots
            # So, we can count the number of roots in the DSU
            # The number of free variables is (number of roots) - 1
            # But since the tree is connected, the DSU will have one root
            # So the number of free variables is 0
            # However, this is not correct, since some edges may not be part of any equation
            # So, the number of free variables is the number of edges not involved in any equation
            # But how to count that?
            # We can count the number of edges not involved in any equation
            # But how?
            # We can build a set of edges that are part of any equation
            # Then, the number of free variables is (n - 1