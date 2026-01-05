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
    # Use a priority queue to track active roadworks
    heap = []
    # Use a pointer to track the current roadwork
    ptr = 0
    # Result array
    res = []

    for d in D:
        # Add all roadworks that start before or at d
        while ptr < N and roadworks[ptr][0] <= d:
            S, T, X = roadworks[ptr]
            heapq.heappush(heap, (T, X))
            ptr += 1
        # If no roadworks are active, the person walks forever
        if not heap:
            res.append(-1)
            continue
        # Find the earliest ending roadwork
        T, X = heap[0]
        # The person reaches X at time d + X
        # If this time is before the roadwork ends, they stop
        if d + X < T:
            res.append(X)
        else:
            # Remove the roadwork from the heap
            heapq.heappop(heap)
            res.append(-1)

    for r in res:
        print(r)

if __name__ == '__main__':
    solve()