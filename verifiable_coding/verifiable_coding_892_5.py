import sys
import math
from collections import deque

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Precompute parity of each cell
        parity = [a % 2 for a in A]
        
        # BFS to find minimum steps
        visited = [False] * N
        queue = deque()
        
        # First step: can jump to any cell 1..K
        for i in range(min(K, N)):
            if not visited[i]:
                visited[i] = True
                queue.append((i, 1))
        
        found = False
        answer = -1
        
        while queue:
            pos, steps = queue.popleft()
            
            # Check if we can reach the end in one step
            if N - pos < K:
                answer = steps + 1
                found = True
                break
            
            # Check next possible positions
            for j in range(pos + 1, min(pos + K + 1, N)):
                if j >= N:
                    continue
                if not visited[j] and parity[j] == parity[pos]:
                    visited[j] = True
                    queue.append((j, steps + 1))
        
        results.append(str(answer) if found else "-1")
    
    print("\n".join(results))