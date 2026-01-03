import sys
import math
from collections import deque

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    traffic = list(map(int, data[1:N+1]))
    edges = data[N+1:]
    
    adj = [[] for _ in range(N)]
    for i in range(N-1):
        u = int(edges[2*i]) - 1
        v = int(edges[2*i + 1]) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    def bfs(start, end):
        visited = [False] * N
        q = deque()
        q.append((start, [start]))
        visited[start] = True
        while q:
            node, path = q.popleft()
            if node == end:
                return path
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append((neighbor, path + [neighbor]))
        return []
    
    def get_path(u, v):
        path = bfs(u, v)
        return path
    
    def get_traffic(path):
        return sum(traffic[i] for i in path)
    
    def is_valid_assignment(assignment):
        for i in range(3):
            if len(assignment[i]) == 0:
                continue
            max_traffic = 0
            for station in assignment[i]:
                max_traffic = max(max_traffic, traffic[station])
            if max_traffic > 1000000000:
                return False
        return True
    
    def dfs(node, color, assignment, max_traffic):
        if color == 3:
            if is_valid_assignment(assignment):
                return True
            return False
        for neighbor in adj[node]:
            if neighbor not in assignment[color]:
                if dfs(neighbor, color, assignment, max_traffic):
                    return True
        return False
    
    def find_assignment():
        assignment = [[], [], []]
        for i in range(N):
            for j in range(3):
                if i not in assignment[j]:
                    assignment[j].append(i)
        return assignment
    
    def min_max_traffic():
        assignment = find_assignment()
        max_traffic = 0
        for i in range(3):
            if len(assignment[i]) == 0:
                continue
            current_max = 0
            for station in assignment[i]:
                current_max = max(current_max, traffic[station])
            max_traffic = max(max_traffic, current_max)
        return max_traffic
    
    def binary_search():
        low = 0
        high = 1000000000
        answer = high
        while low <= high:
            mid = (low + high) // 2
            assignment = [[], [], []]
            for i in range(N):
                for j in range(3):
                    if i not in assignment[j]:
                        assignment[j].append(i)
            valid = True
            for i in range(3):
                if len(assignment[i]) == 0:
                    continue
                current_max = 0
                for station in assignment[i]:
                    current_max = max(current_max, traffic[station])
                if current_max > mid:
                    valid = False
                    break
            if valid:
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        return answer
    
    print(binary_search())