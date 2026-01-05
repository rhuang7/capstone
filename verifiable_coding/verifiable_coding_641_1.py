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
    
    def dfs(u, parent):
        res = traffic[u]
        for v in graph[u]:
            if v != parent:
                res += dfs(v, u)
        return res
    
    def is_possible(max_val):
        color = [-1] * N
        def dfs2(u, parent, color):
            if color[u] != -1:
                return True
            if color[u] == 0:
                return False
            color[u] = 0
            for v in graph[u]:
                if v != parent:
                    if not dfs2(v, u, color):
                        return False
            return True
        
        for i in range(N):
            if color[i] == -1:
                color[i] = 1
                if not dfs2(i, -1, color):
                    return False
        return True
    
    low = max(traffic)
    high = sum(traffic)
    answer = high
    
    while low <= high:
        mid = (low + high) // 2
        if is_possible(mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    
    print(answer)

if __name__ == '__main__':
    solve()