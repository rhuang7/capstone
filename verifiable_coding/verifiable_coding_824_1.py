import sys
import sys
sys.setrecursionlimit(1 << 25)

def main():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    edges = [[] for _ in range(N + 1)]
    idx = 1
    for _ in range(N - 1):
        u = int(data[idx])
        v = int(data[idx + 1])
        edges[u].append(v)
        edges[v].append(u)
        idx += 2
    
    # Compute the depth of each node
    depth = [0] * (N + 1)
    visited = [False] * (N + 1)
    
    def dfs(u, parent):
        visited[u] = True
        for v in edges[u]:
            if not visited[v] and v != parent:
                depth[v] = depth[u] + 1
                dfs(v, u)
    
    dfs(1, -1)
    
    # Count the number of leaves at each depth
    from collections import defaultdict
    leaf_count = defaultdict(int)
    for i in range(1, N + 1):
        if len(edges[i]) == 1 and i != 1:
            leaf_count[depth[i]] += 1
    
    # The maximum number of components is the number of leaves at the deepest level
    max_depth = max(depth[1:])
    result = leaf_count.get(max_depth, 0)
    
    print(result)

if __name__ == '__main__':
    main()