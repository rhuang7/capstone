import sys
import heapq

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    Q = int(data[idx])
    idx += 1
    
    roadworks = []
    for _ in range(N):
        S = int(data[idx])
        idx += 1
        T = int(data[idx])
        idx += 1
        X = int(data[idx])
        idx += 1
        roadworks.append((S, T, X))
    
    D = []
    for _ in range(Q):
        D.append(int(data[idx]))
        idx += 1
    
    # Sort roadworks by start time
    roadworks.sort()
    
    # Use a priority queue to keep track of active roadworks
    heap = []
    # Use a pointer to track the current roadwork
    ptr = 0
    
    # For each person, determine the farthest point they can reach
    for d in D:
        # Add all roadworks that start before or at the current person's start time
        while ptr < N and roadworks[ptr][0] <= d:
            S, T, X = roadworks[ptr]
            heapq.heappush(heap, (T, X))
            ptr += 1
        
        # If there are no active roadworks, the person walks forever
        if not heap:
            print(-1)
            continue
        
        # Find the earliest ending roadwork
        T, X = heapq.heappop(heap)
        
        # The person can reach X if they arrive at X at or before T
        # The time to reach X is X (since they walk at speed 1)
        # If X <= d, then they would have already passed this roadwork
        # So we need to check if X > d
        if X > d:
            print(X)
        else:
            # Reinsert the roadwork back into the heap
            heapq.heappush(heap, (T, X))
            print(-1)
    
if __name__ == '__main__':
    solve()