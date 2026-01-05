import sys
import math
from collections import defaultdict

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
            u = int(data[idx])
            v = int(data[idx+1])
            graph[u].append(v)
            graph[v].append(u)
            idx += 2
        A = int(data[idx])
        idx += 1
        
        # Compute the number of ways to traverse the tree
        # The tree is rooted at A, and we need to count the number of ways to traverse all nodes
        # This is equivalent to counting the number of linear extensions of the tree rooted at A
        # The number of ways is (size of subtree - 1)! * product of (size of each subtree - 1)! for each child
        
        # Compute the size of each subtree and the factorial
        fact = [1] * (N + 1)
        for i in range(1, N + 1):
            fact[i] = (fact[i-1] * i) % MOD
        
        # Compute the size of each subtree and the product of (size - 1)!
        visited = [False] * (N + 1)
        stack = [(A, False)]
        subtree_size = [1] * (N + 1)
        product = 1
        
        while stack:
            node, processed = stack.pop()
            if processed:
                # Compute the product of (size of each child subtree - 1)!
                for child in graph[node]:
                    if not visited[child]:
                        product = (product * fact[subtree_size[child] - 1]) % MOD
                continue
            visited[node] = True
            stack.append((node, True))
            for child in graph[node]:
                if not visited[child]:
                    stack.append((child, False))
                    subtree_size[node] += subtree_size[child]
        
        # The answer is (size of tree - 1)! * product of (size of each child subtree - 1)!
        # The size of the tree is N, so (N-1)! * product
        ans = (fact[N-1] * product) % MOD
        results.append(ans)
    
    for res in results:
        print(res)