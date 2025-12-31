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
        return path
    
    def get_max_traffic(path, traffic):
        max_t = 0
        for node in path:
            max_t = max(max_t, traffic[node])
        return max_t
    
    def dfs(node, parent, visited, traffic, max_t, result):
        if visited[node]:
            return
        visited[node] = True
        current_max = traffic[node]
        for neighbor in graph[node]:
            if neighbor != parent:
                current_max = max(current_max, traffic[neighbor])
                dfs(neighbor, node, visited, traffic, current_max, result)
        result.append(current_max)
    
    def find_min_max():
        visited = [False] * N
        result = []
        dfs(0, -1, visited, traffic, 0, result)
        return max(result)
    
    def binary_search():
        left = 0
        right = sum(traffic)
        answer = right
        while left <= right:
            mid = (left + right) // 2
            visited = [False] * N
            count = 0
            for i in range(N):
                if not visited[i]:
                    path = get_path(i, 0)
                    max_t = get_max_traffic(path, traffic)
                    if max_t > mid:
                        break
                    count += 1
                    for node in path:
                        visited[node] = True
            if count == N:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        return answer
    
    print(binary_search())

if __name__ == '__main__':
    solve()