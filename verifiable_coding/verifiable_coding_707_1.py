import sys
import heapq

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        adj = [[] for _ in range(N + 1)]
        for _ in range(N - 1):
            X = int(data[idx])
            Y = int(data[idx + 1])
            idx += 2
            adj[X].append(Y)
            adj[Y].append(X)
        
        # BFS to find the order
        visited = [False] * (N + 1)
        queue = []
        heapq.heappush(queue, (1, 1))  # (level, node)
        visited[1] = True
        order = []
        
        while queue:
            level, node = heapq.heappop(queue)
            order.append(node)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    heapq.heappush(queue, (level + 1, neighbor))
        
        results.append(' '.join(map(str, order)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()