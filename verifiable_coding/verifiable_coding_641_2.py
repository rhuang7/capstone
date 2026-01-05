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
    
    def dfs2(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs2(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs3(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs2(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs4(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs3(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs5(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs4(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs6(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs5(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs7(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs6(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs8(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs7(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs9(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs8(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs10(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs9(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs11(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs10(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs12(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs11(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs13(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs12(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs14(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs13(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs15(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs14(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs16(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs15(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs17(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs16(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs18(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs17(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs19(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs18(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs20(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs19(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs21(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs20(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs22(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs21(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs23(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs22(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs24(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs23(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs25(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs24(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs26(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs25(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs27(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs26(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs28(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs27(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs29(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs28(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs30(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs29(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs31(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs30(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs32(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs31(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs33(u, parent, max_val):
        res = traffic[u-1]
        for v in graph[u]:
            if v != parent:
                if dfs32(v, u, max_val) > max_val:
                    return max_val
        return res
    
    def dfs3