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
        
        # If K is 1, the monkey can only move to next cell if it's same parity
        if K == 1:
            # Check if all cells have same parity
            parity = A[0] % 2
            possible = True
            for i in range(1, N):
                if A[i] % 2 != parity:
                    possible = False
                    break
            if possible:
                results.append(str(N))
            else:
                results.append("-1")
            continue
        
        # BFS approach
        from collections import deque
        
        # For each position, track the minimum steps to reach it
        dist = [-1] * N
        dist[0] = 1
        
        # Use a priority queue (Dijkstra's algorithm) to process cells in order of steps
        heap = [(1, 0)]  # (steps, position)
        
        while heap:
            steps, pos = heapq.heappop(heap)
            if pos == N - 1:
                results.append(str(steps))
                break
            if dist[pos] < steps:
                continue
            # Check if we can jump to the end
            if N - pos - 1 < K:
                results.append(str(steps + 1))
                break
            # Try to jump to cells j where j > pos, j - pos <= K, and A[pos] % 2 == A[j] % 2
            parity = A[pos] % 2
            for j in range(pos + 1, min(pos + K + 1, N)):
                if A[j] % 2 == parity:
                    if dist[j] == -1 or dist[j] > steps + 1:
                        dist[j] = steps + 1
                        heapq.heappush(heap, (steps + 1, j))
        else:
            results.append("-1")
    
    print("\n".join(results))