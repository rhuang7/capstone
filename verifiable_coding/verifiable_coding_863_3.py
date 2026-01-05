import sys
import heapq

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    
    traffic = []
    for _ in range(N):
        traffic.append(int(data[idx]))
        idx += 1
    
    adj = [[] for _ in range(N)]
    for _ in range(N - 1):
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
    
    def dfs(u, parent):
        max1 = max2 = 0
        for v in adj[u]:
            if v == parent:
                continue
            res = dfs(v, u)
            if res > max1:
                max2 = max1
                max1 = res
            elif res > max2:
                max2 = res
        if max1 == 0:
            return traffic[u]
        return max(traffic[u] + max2, max1)
    
    result = dfs(0, -1)
    print(result)

if __name__ == '__main__':
    main()