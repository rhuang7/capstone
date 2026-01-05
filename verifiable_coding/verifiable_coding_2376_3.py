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
        
        leaves = []
        for i in range(n):
            if len(adj[i]) == 1:
                leaves.append(i)
        
        count = 0
        while leaves:
            freq = collections.defaultdict(int)
            for leaf in leaves:
                parent = adj[leaf][0]
                freq[parent] += 1
            new_leaves = []
            for parent, cnt in freq.items():
                if cnt >= k:
                    count += cnt // k
                    new_leaves.extend([parent] * (cnt // k * k))
            leaves = new_leaves
        
        results.append(str(count))
    
    print('\n'.join(results))