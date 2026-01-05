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
    # For each person, track the earliest time they can reach a point
    # and the distance they can walk
    res = []
    
    for d in D:
        # Add all roadworks that start before or at the current person's start time
        while roadworks and roadworks[0][0] <= d:
            s, t, x = roadworks.pop(0)
            heapq.heappush(heap, (t, x))
        
        # The person starts at time d, and walks at speed 1
        # The earliest time they can reach a point is d + x
        # So we need to find the earliest roadwork that ends after d + x
        # and has x as its position
        
        # If there are no active roadworks, the person walks forever
        if not heap:
            res.append(-1)
            continue
        
        # Find the earliest roadwork that ends after d + x
        # We use a priority queue to get the roadwork with the earliest end time
        # and check if it blocks the person's path
        while heap:
            t, x = heap[0]
            if t > d + x:
                # This roadwork blocks the person's path
                res.append(x)
                break
            else:
                # This roadwork has already passed, remove it
                heapq.heappop(heap)
        else:
            res.append(-1)
    
    for r in res:
        print(r)

if __name__ == '__main__':
    solve()