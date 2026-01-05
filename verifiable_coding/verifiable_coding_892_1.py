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
        
        # BFS to find minimum steps
        from collections import deque
        
        # For each position, track the minimum steps to reach it
        steps = [float('inf')] * N
        steps[0] = 1  # Starting at position 0 (cell 1)
        queue = deque([0])
        
        # For each position, track the parity of A[i]
        parity = [A[i] % 2 for i in range(N)]
        
        while queue:
            pos = queue.popleft()
            if pos == N - 1:
                # If we reach the last cell, we can jump out in one step
                results.append(steps[pos] + 1)
                break
            # Check if we can jump out from here
            if N - 1 - pos < K:
                results.append(steps[pos] + 1)
                break
            # Jump to next positions
            for j in range(pos + 1, min(pos + K + 1, N)):
                if j == N - 1:
                    # Can jump out in one step
                    results.append(steps[pos] + 1)
                    break
                if parity[pos] == parity[j] and steps[j] > steps[pos] + 1:
                    steps[j] = steps[pos] + 1
                    queue.append(j)
            else:
                continue
            break
        else:
            results.append(-1)
    
    for res in results:
        print(res)