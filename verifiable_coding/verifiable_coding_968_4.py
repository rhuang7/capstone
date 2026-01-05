import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    parents = list(map(int, data[1:N]))
    A = list(map(int, data[N+1:]))
    
    # Build the tree
    tree = [[] for _ in range(N+1)]
    for i in range(1, N):
        parent = parents[i-1]
        tree[parent].append(i)
    
    # Compute the result
    result = [0] * N
    min_val = math.inf
    for i in range(N):
        min_val = min(min_val, A[i])
        result[i] = min_val
    
    # Traverse the tree in post-order to compute the path cost
    # We need to compute the path cost from each node to root
    # We'll use a stack for DFS
    stack = [(1, False)]
    path_min = [0] * (N + 1)  # path_min[i] is the minimum value from root to node i
    path_min[1] = A[0]
    
    while stack:
        node, visited = stack.pop()
        if visited:
            # Compute the path cost for this node
            current_min = min(path_min[node], A[node-1])
            result[node-1] = current_min
            # Update the path_min for children
            for child in tree[node]:
                path_min[child] = min(path_min[child], current_min)
            continue
        # Push the node back with visited=True
        stack.append((node, True))
        # Push children
        for child in reversed(tree[node]):
            stack.append((child, False))
            path_min[child] = min(path_min[child], path_min[node])
    
    print(' '.join(map(str, result)))

if __name__ == '__main__':
    solve()