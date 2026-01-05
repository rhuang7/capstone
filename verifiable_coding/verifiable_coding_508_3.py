import sys
import bisect

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
    # For each person, find the earliest roadwork that they encounter
    # We'll use a priority queue to track active roadworks
    import heapq
    heap = []
    res = []

    for d in D:
        # Add all roadworks that start before or at d
        while roadworks and roadworks[0][0] <= d:
            S, T, X = roadworks.pop(0)
            heapq.heappush(heap, (T, X))
        # Check if there is an active roadwork
        if heap:
            # The earliest ending roadwork is the one we need to check
            T, X = heap[0]
            # The person reaches X at time d + X
            # If this time is <= T, then they hit the roadwork
            if d + X <= T:
                res.append(X)
            else:
                res.append(-1)
        else:
            res.append(-1)

    for r in res:
        print(r)

if __name__ == '__main__':
    solve()