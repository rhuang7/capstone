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
    
    traffic = [0] * (N + 1)
    for i in range(1, N + 1):
        traffic[i] = int(data[idx])
        idx += 1
    
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u = int(data[idx])
        v = int(data[idx + 1])
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
        # Choose the best option for this node
        # Either take it and the max of its children not taken
        # Or not take it and take the max of its children
        take = traffic[u] + max2
        not_take = max1
        return max(take, not_take)
    
    result = dfs(1, -1)
    print(result)

if __name__ == '__main__':
    main()