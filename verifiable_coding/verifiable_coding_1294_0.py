import sys
import math
from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        edges = [[] for _ in range(N+1)]
        for _ in range(N-1):
            u = int(data[idx])
            v = int(data[idx+1])
            edges[u].append(v)
            edges[v].append(u)
            idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Build tree and find leaves
        tree = [[] for _ in range(N+1)]
        for u, v in zip(edges, edges):
            tree[u].append(v)
            tree[v].append(u)
        
        # BFS to find leaves
        visited = [False] * (N+1)
        q = deque()
        q.append(1)
        visited[1] = True
        while q:
            u = q.popleft()
            for v in tree[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        
        leaves = [i for i in range(1, N+1) if not visited[i]]
        
        # Check all paths from root to leaves
        possible = False
        for leaf in leaves:
            path = []
            u = leaf
            while u != 1:
                path.append(u)
                u = 1
                # Find parent of u
                for v in tree[u]:
                    if v != 1:
                        u = v
                        break
            path.append(1)
            path.reverse()
            
            # Check if it's possible to get K from this path
            # For each node in path, choose D in [2^(A[i]-1), 2^A[i})
            # Try XOR and AND
            # Since the range is [2^(A[i]-1), 2^A[i}), the minimum is 2^(A[i]-1), maximum is 2^A[i) - 1
            # So for each node, the D can be 2^(A[i]-1) or 2^A[i) - 1
            # Try all combinations of these two options for each node
            # But since A[i] can be up to 64, this is not feasible for large paths
            # So we need a smarter approach
            
            # For XOR:
            # The XOR of all D's must be K
            # For AND:
            # The AND of all D's must be K
            
            # For each node, the D can be either 2^(A[i]-1) or 2^A[i) - 1
            # So for XOR, we can try to find if there's a way to choose D's such that their XOR is K
            # For AND, we can try to find if there's a way to choose D's such that their AND is K
            
            # Try XOR
            xor_val = 0
            for i in path:
                a = A[i-1]
                min_d = 1 << (a-1)
                max_d = (1 << a) - 1
                if xor_val ^ min_d == K:
                    xor_val = K
                    break
                if xor_val ^ max_d == K:
                    xor_val = K
                    break
            if xor_val == K:
                possible = True
                break
            
            # Try AND
            and_val = (1 << 64) - 1
            for i in path:
                a = A[i-1]
                min_d = 1 << (a-1)
                max_d = (1 << a) - 1
                if and_val & min_d == K:
                    and_val = K
                    break
                if and_val & max_d == K:
                    and_val = K
                    break
            if and_val == K:
                possible = True
                break
        
        results.append("YES" if possible else "NO")
    
    print("\n".join(results))