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
        
        # Perform BFS to determine the level of each node
        level = [0] * (N + 1)
        visited = [False] * (N + 1)
        q = [1]
        visited[1] = True
        level[1] = 1
        
        while q:
            node = q.pop(0)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    level[neighbor] = level[node] + 1
                    q.append(neighbor)
        
        # Collect nodes by level
        by_level = [[] for _ in range(N + 1)]
        for i in range(1, N + 1):
            by_level[level[i]].append(i)
        
        # Use a priority queue to get the smallest node at each level
        heap = []
        for i in range(1, N + 1):
            heapq.heappush(heap, (level[i], i))
        
        result = []
        while heap:
            _, node = heapq.heappop(heap)
            result.append(str(node))
        
        results.append(' '.join(result))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()