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
        for u, v in zip(edges[1], edges[2]):
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
        
        # For each leaf, find the path from root to leaf
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
            
            # Check if it's possible to get K using XOR or AND
            # For each node in path, choose D in [2^(A[i]-1), 2^A[i})
            # We need to find if there exists a set of D's such that XOR or AND of all D's is K
            
            # For XOR:
            # We can choose D_i = 2^(A[i]-1) + x_i where 0 <= x_i < 2^(A[i]-1)
            # So the XOR of all D_i is the XOR of 2^(A[i]-1) for all i, plus some value from the x_i's
            # But since x_i can be anything, the XOR can be anything in the range [0, 2^max_A - 1]
            # However, the D_i's are in the range [2^(A[i]-1), 2^A[i}), so their XOR is in the range [0, 2^max_A - 1]
            # So if K is in this range, it's possible to get it via XOR
            
            # For AND:
            # The AND of all D_i is the AND of the minimum possible values (2^(A[i]-1))
            # Because D_i >= 2^(A[i]-1), so AND is at least the AND of 2^(A[i]-1)
            # But since D_i can be anything in the range, the AND can be anything that is a subset of the bits of the minimum possible values
            # So the AND is the AND of the minimum possible values, which is the AND of 2^(A[i]-1) for all i in path
            
            # So check both possibilities
            xor_min = 0
            and_min = 0
            for i in path:
                a = A[i-1]
                xor_min ^= (1 << (a-1))
                and_min &= (1 << (a-1))
            
            if K <= (1 << max(A)) - 1:
                possible = True
            if and_min == K:
                possible = True
            
            if possible:
                break
        
        results.append("YES" if possible else "NO")
    
    print("\n".join(results))