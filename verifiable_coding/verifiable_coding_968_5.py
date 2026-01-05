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
    result = [0] * (N+1)
    min_val = math.inf
    for i in range(1, N+1):
        min_val = min(min_val, A[i-1])
        result[i] = min_val
    
    # Traverse the tree in post-order to compute the path cost
    # Since we need to go from root to leaves, we can do a BFS or DFS from root
    # We'll use BFS
    from collections import deque
    queue = deque()
    queue.append(1)
    visited = [False] * (N+1)
    visited[1] = True
    min_val = math.inf
    result[1] = min_val = A[0]
    
    while queue:
        node = queue.popleft()
        for child in tree[node]:
            if not visited[child]:
                visited[child] = True
                min_val = min(min_val, A[child-1])
                result[child] = min_val
                queue.append(child)
    
    print(' '.join(map(str, result[1:N+1])))

if __name__ == '__main__':
    solve()