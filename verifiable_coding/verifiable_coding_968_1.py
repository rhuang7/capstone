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
    result = [0] * (N + 1)
    min_so_far = math.inf
    for i in range(N, 0, -1):
        min_so_far = min(min_so_far, A[i-1])
        result[i] = min_so_far
    
    # Traverse the tree and compute the path cost
    path_cost = [0] * (N + 1)
    stack = [(1, 0)]
    while stack:
        node, parent = stack.pop()
        path_cost[node] = result[node]
        for child in tree[node]:
            stack.append((child, node))
    
    # Output the result for nodes 1 to N
    print(' '.join(map(str, path_cost[1:N+1])))

if __name__ == '__main__':
    solve()