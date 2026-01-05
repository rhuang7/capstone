import sys
import collections

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        adj = collections.defaultdict(list)
        for _ in range(n-1):
            u = int(data[idx]) - 1
            v = int(data[idx+1]) - 1
            adj[u].append(v)
            adj[v].append(u)
            idx += 2
        
        leaves = [i for i in range(n) if len(adj[i]) == 1]
        count = collections.defaultdict(int)
        for leaf in leaves:
            count[adj[leaf][0]] += 1
        
        res = 0
        for v in count:
            res += count[v] // k
        results.append(str(res))
    
    print('\n'.join(results))