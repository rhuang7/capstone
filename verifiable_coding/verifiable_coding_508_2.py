import sys
import bisect

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    Q = int(data[1])
    
    roadworks = []
    index = 2
    for _ in range(N):
        S = int(data[index])
        T = int(data[index+1])
        X = int(data[index+2])
        roadworks.append((S, T, X))
        index += 3
    
    D = list(map(int, data[index:index+Q]))
    
    # Sort roadworks by start time
    roadworks.sort()
    
    # For each person, find the earliest roadwork that they encounter
    # We use a priority queue to track active roadworks
    import heapq
    
    # Initialize the priority queue with all roadworks that start at time 0
    # The priority is based on the end time of the roadwork
    heap = []
    for i in range(N):
        if roadworks[i][0] == 0:
            heapq.heappush(heap, (roadworks[i][1], roadworks[i][2]))
    
    # For each person, process the roadworks
    for d in D:
        # Remove roadworks that have ended before the person starts walking
        while heap and heap[0][0] <= d:
            heapq.heappop(heap)
        
        # If there are no active roadworks, the person walks forever
        if not heap:
            print(-1)
            continue
        
        # The earliest roadwork is the one with the earliest end time
        # The person will hit this roadwork at position X
        # The time they reach this position is d + X
        # The roadwork is active from S to T, so we need to check if d + X is within [S, T)
        # Since the roadwork is active at the time the person reaches it, we can just take X
        print(heap[0][1])
    
    return

if __name__ == '__main__':
    solve()