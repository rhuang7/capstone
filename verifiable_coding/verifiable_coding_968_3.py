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
    min_so_far = math.inf
    for i in range(N):
        min_so_far = min(min_so_far, A[i])
        result[i] = min_so_far
    
    # Traverse the tree in BFS order starting from root
    from collections import deque
    q = deque()
    q.append(1)
    min_so_far = math.inf
    visited = [False] * (N + 1)
    visited[1] = True
    res = [0] * (N + 1)
    
    while q:
        u = q.popleft()
        min_so_far = min(min_so_far, A[u-1])
        res[u] = min_so_far
        for v in tree[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    
    # Output the result for nodes 1 to N
    print(' '.join(map(str, res[1:N+1])))

if __name__ == '__main__':
    solve()