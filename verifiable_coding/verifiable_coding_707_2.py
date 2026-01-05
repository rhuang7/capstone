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
        graph = [[] for _ in range(N + 1)]
        for _ in range(N - 1):
            X = int(data[idx])
            Y = int(data[idx + 1])
            idx += 2
            graph[X].append(Y)
            graph[Y].append(X)
        
        # BFS to find the order
        visited = [False] * (N + 1)
        q = []
        heapq.heappush(q, (1, 1))  # (level, node)
        visited[1] = True
        order = []
        
        while q:
            level, node = heapq.heappop(q)
            order.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    heapq.heappush(q, (level + 1, neighbor))
        
        results.append(' '.join(map(str, order)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()