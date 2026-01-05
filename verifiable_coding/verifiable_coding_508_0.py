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
    res = []

    for d in D:
        # Remove roadworks that have ended before the current time
        while heap and heap[0][0] < d:
            heapq.heappop(heap)

        # Add all roadworks that start before or at the current time
        while roadworks and roadworks[0][0] <= d:
            s, t, x = roadworks.pop(0)
            heapq.heappush(heap, (t, x))

        # If there are no active roadworks, the person walks forever
        if not heap:
            res.append(-1)
        else:
            # The person will stop at the closest active roadwork
            # The distance is the x-coordinate of the roadwork
            res.append(heap[0][1])

    for r in res:
        print(r)

if __name__ == '__main__':
    solve()