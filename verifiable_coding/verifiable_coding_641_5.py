import sys
import heapq

def solve():
    import sys
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
    
    # Binary search on the answer
    low = 1
    high = total
    answer = total
    
    while low <= high:
        mid = (low + high) // 2
        visited = [False] * (N + 1)
        cnt = 0
        
        def dfs2(u, parent):
            nonlocal cnt
            if visited[u]:
                return
            visited[u] = True
            if traffic[u-1] > mid:
                return
            for v in graph[u]:
                if v != parent:
                    dfs2(v, u)
            cnt += 1
        
        cnt = 0
        for i in range(1, N+1):
            if not visited[i]:
                dfs2(i, -1)
        
        if cnt <= 3:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    
    print(answer)

if __name__ == '__main__':
    solve()