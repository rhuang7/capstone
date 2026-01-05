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
        q = deque()
        # First step: can jump to any cell 1..K
        for i in range(K):
            if not visited[i]:
                q.append((i, 1))
                visited[i] = True
        
        found = False
        answer = -1
        while q:
            pos, steps = q.popleft()
            if pos == N - 1:
                answer = steps
                found = True
                break
            # Check if we can jump to the end
            if N - pos < K:
                answer = steps + 1
                found = True
                break
            # Next positions: j > pos, j - pos <= K, A[pos]%2 == A[j]%2
            for j in range(pos + 1, min(pos + K + 1, N)):
                if parity[j] == parity[pos] and not visited[j]:
                    visited[j] = True
                    q.append((j, steps + 1))
        
        results.append(str(answer) if found else "-1")
    
    print('\n'.join(results))