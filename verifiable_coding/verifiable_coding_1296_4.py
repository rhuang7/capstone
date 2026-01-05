import sys
import math
from collections import defaultdict, deque

MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        graph = defaultdict(list)
        for _ in range(N-1):
            u = int(data[idx]) - 1
            v = int(data[idx+1]) - 1
            graph[u].append(v)
            graph[v].append(u)
            idx += 2
        A = int(data[idx]) - 1
        idx += 1
        
        # Compute the number of ways
        # The tree is rooted at A
        # We perform a DFS to compute the number of ways
        # The number of ways is (product of (size of each subtree - 1)!) 
        # because for each subtree, Chef can choose the order of visiting the nodes in (size - 1)! ways
        
        # Compute sizes of subtrees and factorials
        size = [0] * N
        visited = [False] * N
        stack = [(A, -1, False)]
        factorial = [1] * (N + 1)
        for i in range(1, N + 1):
            factorial[i] = (factorial[i - 1] * i) % MOD
        
        while stack:
            node, parent, is_processed = stack.pop()
            if is_processed:
                # Compute size of subtree rooted at node
                size[node] = 1
                for child in graph[node]:
                    if child != parent:
                        size[node] += size[child]
                # Compute the product of (size[child] - 1)! for each child
                res = 1
                for child in graph[node]:
                    if child != parent:
                        res = (res * factorial[size[child] - 1]) % MOD
                results.append(res)
            else:
                stack.append((node, parent, True))
                for child in graph[node]:
                    if child != parent:
                        stack.append((child, node, False))
        
        # The answer is the product of all the results
        ans = 1
        for res in results:
            ans = (ans * res) % MOD
        results[-1] = ans
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()