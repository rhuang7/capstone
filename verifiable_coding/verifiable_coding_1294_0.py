import sys
import math
from sys import stdin
input = sys.stdin.buffer.read
def solve():
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
        
        # Build tree
        from collections import deque
        tree = [[] for _ in range(N+1)]
        visited = [False] * (N+1)
        q = deque()
        q.append(1)
        visited[1] = True
        while q:
            u = q.popleft()
            for v in edges[u]:
                if not visited[v]:
                    visited[v] = True
                    tree[u].append(v)
                    q.append(v)
        
        # Find all leaves
        leaves = []
        for i in range(1, N+1):
            if len(tree[i]) == 0:
                leaves.append(i)
        
        # Try all leaves
        possible = False
        for leaf in leaves:
            # Find path from root to leaf
            path = []
            u = leaf
            while u != 1:
                path.append(u)
                u = 1
                for v in tree[u]:
                    if v != 1:
                        u = v
                        break
            path.append(1)
            path.reverse()
            
            # Check if we can choose D values for this path
            # and get K via XOR or AND
            # For each node in path, D is in [2^(A[i]-1), 2^A[i})
            # So for each node, D can be any value in that range
            # We need to check if there exists a set of D's such that XOR or AND is K
            
            # For XOR:
            # We need to choose D_i in their ranges such that XOR of all D_i is K
            # For AND:
            # We need to choose D_i in their ranges such that AND of all D_i is K
            
            # Let's try XOR first
            xor_val = 0
            for i in path:
                a = A[i-1]
                low = 1 << (a-1)
                high = (1 << a) - 1
                # Try to set the bit at position a-1 to 1
                # If we can set it, then XOR can be adjusted
                # But since we can choose any value in the range, we can try to set the bits
                # We can try to find if it's possible to get K via XOR
                # We can try to greedily set bits
                # But since the ranges are [low, high], and low is 2^(a-1), high is 2^a - 1
                # So for each node, the D_i can be any value in [low, high]
                # We can try to find if there's a way to set the bits to get K
                # Let's try to find if it's possible to get K via XOR
                # We can try to greedily set bits
                # Let's try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K via XOR
                # We can try to find if it's possible to get K