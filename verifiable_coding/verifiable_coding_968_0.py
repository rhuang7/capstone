import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    parents = list(map(int, data[1:N]))
    A = list(map(int, data[N+1:]))
    
    tree = [[] for _ in range(N+1)]
    for i in range(1, N):
        tree[parents[i-1]].append(i)
    
    result = [0] * (N + 1)
    
    def dfs(u):
        min_val = A[u-1]
        result[u] = min_val
        for v in tree[u]:
            dfs(v)
            min_val = min(min_val, A[v-1])
            result[u] += min_val
    
    dfs(1)
    
    print(' '.join(map(str, result[1:N+1])))

if __name__ == '__main__':
    solve()