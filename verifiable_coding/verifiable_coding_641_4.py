import sys
import heapq

def solve():
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    traffic = list(map(int, data[1:N+1]))
    edges = data[N+1:]
    
    from collections import defaultdict
    graph = defaultdict(list)
    for i in range(N-1):
        u = int(edges[2*i])
        v = int(edges[2*i + 1])
        graph[u].append(v)
        graph[v].append(u)
    
    def dfs(u, parent):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                res += dfs(v, u)
        return res
    
    total = sum(traffic)
    if total <= 0:
        print(0)
        return
    
    def can_split(max_val):
        visited = [False] * (N + 1)
        def dfs2(u, parent, cnt):
            if cnt > max_val:
                return False
            visited[u] = True
            for v in graph[u]:
                if not visited[v]:
                    if not dfs2(v, u, cnt + traffic[v-1]):
                        return False
            return True
        
        for i in range(1, N+1):
            if not visited[i]:
                if not dfs2(i, -1, traffic[i-1]):
                    return False
        return True
    
    low = 1
    high = total
    answer = total
    while low <= high:
        mid = (low + high) // 2
        if can_split(mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    print(answer)

if __name__ == '__main__':
    solve()