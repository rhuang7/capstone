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
    
    # BFS to find the maximum traffic in a tree
    def bfs(start):
        visited = [False] * N
        q = deque()
        q.append(start)
        visited[start] = True
        max_traffic = 0
        while q:
            node = q.popleft()
            max_traffic = max(max_traffic, traffic[node])
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)
        return max_traffic
    
    # Try all possible splits of the tree into three parts
    # We use binary search to find the minimum possible maximum traffic
    low = max(traffic)
    high = sum(traffic)
    
    answer = high
    
    while low <= high:
        mid = (low + high) // 2
        # Check if it's possible to split the tree into 3 parts with max traffic <= mid
        # We use BFS to check if we can split the tree into 3 parts with max traffic <= mid
        # We need to find 3 subtrees such that the sum of traffic in each is <= mid
        # We use a modified BFS to check this
        
        # We'll use a visited array to mark nodes that are already assigned
        visited = [False] * N
        count = 0
        for i in range(N):
            if not visited[i]:
                # BFS to find the subtree starting at i
                q = deque()
                q.append(i)
                visited[i] = True
                subtree_sum = 0
                while q:
                    node = q.popleft()
                    subtree_sum += traffic[node]
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            q.append(neighbor)
                if subtree_sum > mid:
                    # Not possible to split
                    break
                count += 1
                if count == 3:
                    # Possible to split
                    answer = mid
                    high = mid - 1
                    break
        else:
            # Not possible to split
            low = mid + 1
    
    print(answer)

if __name__ == '__main__':
    solve()