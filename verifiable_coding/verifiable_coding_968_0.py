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
        tree[parents[i-1]].append(i)
    
    # Compute the result
    result = [0] * (N+1)
    
    # Perform DFS from root
    stack = [(1, 0)]  # (node, parent)
    min_so_far = []
    
    while stack:
        node, parent = stack.pop()
        # Compute the min_so_far for this node
        if parent == 0:
            min_so_far = [A[node-1]]
        else:
            min_so_far = [min(min_so_far[0], A[node-1])]
        
        # Update the result for this node
        result[node] = sum(min_so_far)
        
        # Push children to stack
        for child in tree[node]:
            stack.append((child, node))
    
    # Output the result for nodes 1 to N
    print(' '.join(map(str, result[1:N+1])))

if __name__ == '__main__':
    solve()