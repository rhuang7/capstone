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
    min_vals = []
    
    # Perform DFS from root
    def dfs(node):
        # Current node's value
        current_min = A[node-1]
        # Add current value to min_vals
        min_vals.append(current_min)
        # Recursively process children
        for child in tree[node]:
            dfs(child)
        # After processing children, backtrack
        min_vals.pop()
    
    dfs(1)
    
    # Compute the sum of min_vals in reverse order
    total = 0
    for i in range(N, 0, -1):
        total += min_vals[i-1]
        result[i] = total
    
    # Output the result for nodes 1 to N
    print(' '.join(map(str, result[1:N+1])))

if __name__ == '__main__':
    solve()