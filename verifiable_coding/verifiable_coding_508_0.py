import sys
import heapq

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    Q = int(data[1])
    
    idx = 2
    roadworks = []
    for _ in range(N):
        S = int(data[idx])
        T = int(data[idx+1])
        X = int(data[idx+2])
        roadworks.append((S, T, X))
        idx += 3
    
    D = list(map(int, data[idx:idx+Q]))
    
    # Sort roadworks by start time
    roadworks.sort()
    
    # Use a priority queue to track active roadworks
    heap = []
    res = []
    
    for d in D:
        # Add all roadworks that start before or at d
        while roadworks and roadworks[0][0] <= d:
            S, T, X = roadworks.pop(0)
            heapq.heappush(heap, (T, X))
        
        # If no active roadworks, the person walks forever
        if not heap:
            res.append(-1)
            continue
        
        # Find the earliest ending roadwork
        T, X = heapq.heappop(heap)
        
        # The person reaches X at time d + X
        # If this time is before the roadwork ends, they get blocked
        if d + X < T:
            res.append(X)
        else:
            # Put the roadwork back into the heap
            heapq.heappush(heap, (T, X))
            res.append(-1)
    
    for r in res:
        print(r)

if __name__ == '__main__':
    solve()