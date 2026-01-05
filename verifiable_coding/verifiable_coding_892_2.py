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
        steps[0] = 1  # Starting at position 0 (1st cell)
        queue = deque([0])
        
        # For each position, track the parity of A[i]
        parity = [A[i] % 2 for i in range(N)]
        
        while queue:
            pos = queue.popleft()
            if pos == N - 1:
                # Reached the last cell, but need to check if we can jump out
                # If distance from last cell is less than K, we can jump out
                if N - pos - 1 < K:
                    results.append(steps[pos])
                else:
                    # Need to check if we can jump to the last cell in one step
                    if pos + K >= N:
                        results.append(steps[pos] + 1)
                    else:
                        # Check if we can jump from pos to N-1
                        if (A[pos] % 2 == A[N-1] % 2) and (N - pos - 1 <= K):
                            results.append(steps[pos] + 1)
                        else:
                            # Can't reach the end
                            results.append(-1)
                break
            # Jump to any cell within K steps
            for j in range(pos + 1, min(pos + K + 1, N)):
                if j == N - 1:
                    # Check if we can jump out
                    if N - j - 1 < K:
                        results.append(steps[pos] + 1)
                    else:
                        if (A[pos] % 2 == A[j] % 2) and (N - j - 1 <= K):
                            results.append(steps[pos] + 1)
                        else:
                            results.append(-1)
                    break
                if parity[j] == parity[pos] and steps[j] > steps[pos] + 1:
                    steps[j] = steps[pos] + 1
                    queue.append(j)
        else:
            # If we didn't break out of the loop, it means we couldn't reach the end
            results.append(-1)
    
    for res in results:
        print(res)