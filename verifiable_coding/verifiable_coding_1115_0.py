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
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        tree = defaultdict(list)
        for _ in range(N-1):
            u = int(data[idx]) - 1
            v = int(data[idx+1]) - 1
            tree[u].append(v)
            tree[v].append(u)
            idx += 2
        
        # Compute subtree sizes and depths for each node
        size = [1] * N
        depth = [0] * N
        parent = [-1] * N
        
        # BFS to compute parent, depth, and size
        q = deque([0])
        visited = [False] * N
        visited[0] = True
        while q:
            u = q.popleft()
            for v in tree[u]:
                if not visited[v] and v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    visited[v] = True
                    q.append(v)
        
        # Post-order traversal to compute size
        def dfs(u):
            for v in tree[u]:
                if v != parent[u]:
                    dfs(v)
                    size[u] += size[v]
        
        dfs(0)
        
        # Compute contribution of each node
        # For each node, its contribution is A[i] * (number of paths that pass through it)
        # The number of paths that pass through a node is (number of leaves in its subtree) * (number of leaves outside its subtree)
        # But since we can permute the values, we should assign the largest A[i] to the node that has the most paths passing through it
        # So we sort the nodes by the number of paths passing through them in descending order and assign the largest A[i] to the node with the most paths
        
        # Compute for each node the number of paths passing through it
        # This is (number of leaves in its subtree) * (number of leaves outside its subtree)
        # But we can compute it as (size[u] * (N - size[u])) if u is a root
        # But for general tree, it's (size[u] * (N - size[u])) if u is not a root
        # However, since we can permute the values, we can assign the largest A[i] to the node with the largest (size[u] * (N - size[u]))
        
        # So we compute for each node the value size[u] * (N - size[u])
        # Then sort the nodes by this value in descending order
        # Then assign the largest A[i] to the node with the largest value
        
        # Compute the value for each node
        values = [size[i] * (N - size[i]) for i in range(N)]
        
        # Sort the nodes by values in descending order
        nodes = sorted(range(N), key=lambda x: -values[x])
        
        # Sort A in descending order
        A.sort(reverse=True)
        
        # Assign the largest A[i] to the node with the largest value
        res = 0
        for i in range(N):
            res = (res + A[i] * values[nodes[i]]) % MOD
        
        results.append(res)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()