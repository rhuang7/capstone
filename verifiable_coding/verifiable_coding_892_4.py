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
        
        # BFS approach
        from collections import deque
        visited = [False] * N
        queue = deque()
        # Initial positions: 0 (cell 1)
        queue.append((0, 0))  # (position, steps)
        visited[0] = True
        
        # Special case: if the first cell is the last cell
        if N == 1:
            results.append(1)
            continue
        
        # Use a priority queue for Dijkstra's algorithm
        # Since we want the minimum steps, we can use a priority queue
        # But for this problem, BFS is sufficient as all steps are same weight
        # However, due to the constraints, we need to use a priority queue to handle the cases efficiently
        # So we use Dijkstra's algorithm with a priority queue
        import heapq
        heap = []
        heapq.heappush(heap, (0, 0))  # (steps, position)
        visited = [False] * N
        visited[0] = True
        
        found = False
        answer = -1
        
        while heap:
            steps, pos = heapq.heappop(heap)
            if pos == N - 1:
                answer = steps
                found = True
                break
            # Check if we can jump to the end
            if N - pos - 1 < K:
                answer = steps + 1
                found = True
                break
            # Check all possible next positions
            for j in range(pos + 1, min(pos + K + 1, N)):
                if j >= N:
                    continue
                if not visited[j] and A[pos] % 2 == A[j] % 2:
                    visited[j] = True
                    heapq.heappush(heap, (steps + 1, j))
        
        results.append(answer if found else -1)
    
    for res in results:
        print(res)