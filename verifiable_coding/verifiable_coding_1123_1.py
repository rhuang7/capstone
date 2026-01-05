import sys
import sys
from sys import stdin
from collections import defaultdict, deque

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx+1])
        idx += 2
        graph = defaultdict(list)
        for _ in range(M):
            A = int(data[idx])
            B = int(data[idx+1])
            graph[A].append(B)
            graph[B].append(A)
            idx += 2
        Q = int(data[idx])
        idx += 1
        visited = [False] * N
        for _ in range(Q):
            X = int(data[idx])
            Y = int(data[idx+1])
            idx += 2
            # Find connected component of X
            queue = deque()
            queue.append(X)
            visited[X] = True
            found = False
            while queue:
                node = queue.popleft()
                if node == Y:
                    found = True
                    break
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            results.append("YO" if found else "NO")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()