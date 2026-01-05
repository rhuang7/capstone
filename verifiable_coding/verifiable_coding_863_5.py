import sys
import collections

def solve():
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    
    traffic = [0] * (N + 1)
    for i in range(1, N + 1):
        traffic[i] = int(data[idx])
        idx += 1
    
    adj = [ [] for _ in range(N + 1) ]
    for _ in range(N - 1):
        u = int(data[idx])
        v = int(data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
    
    # We need to find the maximum weight independent set in a tree
    # We'll use dynamic programming on trees
    
    # For each node, we store two values:
    # 1. The maximum weight if we include the node
    # 2. The maximum weight if we exclude the node
    
    # We'll perform a post-order traversal of the tree
    # To avoid recursion depth issues, we'll use an iterative DFS
    
    # We'll use a stack for DFS
    stack = []
    visited = [False] * (N + 1)
    parent = [0] * (N + 1)
    
    # Start DFS from node 1
    stack.append((1, False))
    while stack:
        node, is_processed = stack.pop()
        if is_processed:
            # Process the node after children are processed
            include = traffic[node]
            exclude = 0
            for neighbor in adj[node]:
                if neighbor != parent[node]:
                    include += dp[neighbor][1]
                    exclude += max(dp[neighbor][0], dp[neighbor][1])
            dp[node][0] = exclude
            dp[node][1] = include
        else:
            # Mark as visited and push back with is_processed=True
            visited[node] = True
            parent[node] = stack[-1][0] if stack else 0
            stack.append((node, True))
            # Push children (neighbors not parent) in reverse order to process them in order
            for neighbor in reversed(adj[node]):
                if not visited[neighbor] and neighbor != parent[node]:
                    stack.append((neighbor, False))
    
    # The answer is the maximum of including or excluding the root (node 1)
    print(max(dp[1][0], dp[1][1]))

# The dp array will be stored as a list of tuples
dp = [ (0, 0) for _ in range(N + 1) ]

if __name__ == '__main__':
    solve()