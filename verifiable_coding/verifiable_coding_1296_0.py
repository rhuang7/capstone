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
            u = int(data[idx])
            v = int(data[idx+1])
            graph[u].append(v)
            graph[v].append(u)
            idx += 2
        A = int(data[idx])
        idx += 1
        
        # Build tree with A as root
        tree = defaultdict(list)
        visited = [False] * (N + 1)
        q = deque()
        q.append(A)
        visited[A] = True
        while q:
            u = q.popleft()
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    tree[u].append(v)
                    q.append(v)
        
        # Compute the number of ways
        # The tree is rooted at A, and we need to count the number of ways to traverse all nodes
        # This is equivalent to the number of ways to traverse a tree in a specific order
        # The answer is (number of ways to traverse the tree) = (product of (size of each subtree - 1)!) 
        # But since we are starting at A, the answer is (product of (size of each subtree - 1)!) 
        # Because for each subtree, we can choose the order in (size - 1)! ways
        
        # Compute sizes of all subtrees
        sizes = [0] * (N + 1)
        
        def dfs(u, parent):
            size = 1
            for v in tree[u]:
                if v != parent:
                    size += dfs(v, u)
            sizes[u] = size
            return size
        
        dfs(A, -1)
        
        # Compute the product of (size of each subtree - 1)!
        result = 1
        for u in range(1, N + 1):
            if sizes[u] > 1:
                fact = 1
                for i in range(1, sizes[u]):
                    fact = fact * i % MOD
                result = result * fact % MOD
        
        results.append(result)
    
    for res in results:
        print(res)