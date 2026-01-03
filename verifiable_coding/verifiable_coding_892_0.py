import sys
import heapq

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
        
        # If K is 1, the monkey can only move to the next cell
        if K == 1:
            # Check if all cells have the same parity
            parity = A[0] % 2
            for i in range(1, N):
                if A[i] % 2 != parity:
                    results.append(-1)
                    break
            else:
                results.append(N)
            continue
        
        # Use BFS to find the minimum steps
        from collections import deque
        
        # Each state is (position, steps, parity)
        # We need to track visited positions and their parity
        visited = [ [False]*2 for _ in range(N) ]
        queue = deque()
        # Start from position 0 (0-based), with 0 steps, and parity of A[0]
        queue.append( (0, 0, A[0] % 2) )
        visited[0][A[0] % 2] = True
        
        found = False
        answer = -1
        
        while queue:
            pos, steps, parity = queue.popleft()
            
            # If we are at the last cell, check if we can jump out
            if pos == N-1:
                # If distance from last cell is less than K, we can jump out
                if N - pos <= K:
                    answer = steps + 1
                    found = True
                    break
                else:
                    # Check if we can jump to the last cell
                    if pos + 1 <= N-1 and (pos + 1 - pos) <= K and (A[pos] % 2 == A[pos+1] % 2):
                        answer = steps + 1
                        found = True
                        break
                continue
            
            # Try to jump to next cells
            for j in range(pos+1, min(pos+K+1, N)):
                if j - pos > K:
                    continue
                if A[j] % 2 == parity:
                    if not visited[j][A[j] % 2]:
                        visited[j][A[j] % 2] = True
                        queue.append( (j, steps + 1, A[j] % 2) )
        
        results.append(answer if found else -1)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()