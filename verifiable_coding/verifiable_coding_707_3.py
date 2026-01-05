import sys
import heapq

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        adj = [[] for _ in range(N + 1)]
        for _ in range(N - 1):
            X = int(data[idx])
            Y = int(data[idx + 1])
            adj[X].append(Y)
            adj[Y].append(X)
            idx += 2
        
        # Perform BFS to determine the level of each node
        level = [0] * (N + 1)
        visited = [False] * (N + 1)
        q = [1]
        visited[1] = True
        level[1] = 1
        
        while q:
            u = q.pop(0)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    level[v] = level[u] + 1
                    q.append(v)
        
        # Extract nodes in order of increasing level
        result = []
        for i in range(1, N + 1):
            result.append(str(i))
        
        # Output the result
        print(' '.join(result))
        
if __name__ == '__main__':
    solve()