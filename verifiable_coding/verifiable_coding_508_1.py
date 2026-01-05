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
    # Use a pointer to track current roadwork
    ptr = 0
    # Use a list to store answers
    ans = [-1] * Q

    for i in range(Q):
        D_i = D[i]
        # Add all roadworks that start before or at D_i
        while ptr < N and roadworks[ptr][0] <= D_i:
            S, T, X = roadworks[ptr]
            heapq.heappush(heap, (T, X))
            ptr += 1
        # Remove all roadworks that ended before D_i
        while heap and heap[0][0] <= D_i:
            heapq.heappop(heap)
        # If there are active roadworks, find the one with the smallest X
        if heap:
            T, X = heap[0]
            # The person will stop at X if they reach it before the roadwork ends
            # Time to reach X is X
            if X <= D_i + X:
                ans[i] = X
            else:
                ans[i] = -1
        else:
            ans[i] = -1

    for a in ans:
        print(a)

if __name__ == '__main__':
    solve()