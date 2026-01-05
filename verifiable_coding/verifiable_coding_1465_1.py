import sys
import math
MOD = 10**9 + 7

def solve():
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
        
        # Build the tree and find parent relationships
        parent = [0]*(n+1)
        visited = [False]*(n+1)
        stack = [1]
        visited[1] = True
        while stack:
            u = stack.pop()
            for v in edges[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    stack.append(v)
        
        # Build the path from u to v
        def get_path(u, v):
            path = []
            while u != v:
                path.append(u)
                u = parent[u]
            path.append(v)
            return path[::-1]
        
        # Build the system of equations
        # Let x_i be the weight of edge between parent[i] and i
        # For each condition (u, v, x), the sum of x_i along the path from u to v must be equal to x
        # We can represent this as a system of linear equations over GF(2)
        # We'll use Gaussian elimination over GF(2)
        
        # Build the equations
        equations = []
        for u, v, x in conditions:
            path = get_path(u, v)
            sum_path = 0
            for i in range(len(path)-1):
                sum_path ^= (1 if path[i+1] == parent[path[i]] else 0)
            # The equation is sum_path = x
            # We'll represent this as a row in the matrix
            row = [0]*(n+1)
            for i in range(len(path)-1):
                if path[i+1] == parent[path[i]]:
                    row[path[i]] = 1
            equations.append(row)
        
        # Gaussian elimination over GF(2)
        rank = 0
        for col in range(n):
            pivot = -1
            for row in range(rank, len(equations)):
                if equations[row][col] == 1:
                    pivot = row
                    break
            if pivot == -1:
                continue
            equations[rank], equations[pivot] = equations[pivot], equations[rank]
            for row in range(len(equations)):
                if row != rank and equations[row][col] == 1:
                    for c in range(col, n+1):
                        equations[row][c] ^= equations[rank][c]
            rank += 1
        
        # The number of free variables is n - rank
        # The answer is 2^(number of free variables)
        ans = pow(2, n - rank, MOD)
        print(ans)

if __name__ == '__main__':
    solve()