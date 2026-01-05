import sys
import math
from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    traffic = list(map(int, data[1:N+1]))
    edges = data[N+1:]
    
    graph = defaultdict(list)
    for i in range(N-1):
        u = int(edges[i*2]) - 1
        v = int(edges[i*2 + 1]) - 1
        graph[u].append(v)
        graph[v].append(u)
    
    def bfs(start, end):
        visited = [False] * N
        queue = deque()
        queue.append((start, [start]))
        visited[start] = True
        while queue:
            node, path = queue.popleft()
            if node == end:
                return path
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, path + [neighbor]))
        return []
    
    def get_path(u, v):
        path = bfs(u, v)
        if not path:
            return []
        return path
    
    def get_max_traffic(path, traffic):
        max_t = 0
        for node in path:
            max_t = max(max_t, traffic[node])
        return max_t
    
    def dfs(node, parent, visited, traffic, max_val, result):
        if node in visited:
            return
        visited.add(node)
        current_max = traffic[node]
        for neighbor in graph[node]:
            if neighbor != parent:
                if get_max_traffic([node, neighbor], traffic) > max_val:
                    return
                dfs(neighbor, node, visited, traffic, max_val, result)
        result.append(current_max)
    
    def find_min_max():
        result = []
        visited = set()
        for i in range(N):
            if i not in visited:
                dfs(i, -1, visited, traffic, 0, result)
        return max(result)
    
    print(find_min_max())