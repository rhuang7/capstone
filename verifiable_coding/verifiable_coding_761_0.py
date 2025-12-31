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
        N, K, M = map(int, data[idx:idx+3])
        idx += 3
        A = list(map(int, data[idx:idx+N]))
        idx += N
        B = list(map(int, data[idx:idx+N]))
        idx += N
        C = list(map(int, data[idx:idx+K]))
        idx += K
        D = list(map(int, data[idx:idx+M]))
        idx += M
        
        # For each day, calculate the difference between planned and completed
        diff = [A[i] - B[i] for i in range(N)]
        
        # Sort white buttons in descending order
        C.sort(reverse=True)
        # Sort black buttons in descending order
        D.sort(reverse=True)
        
        # Use a max-heap for white buttons (simulated with negative values)
        white_heap = [-x for x in C]
        heapq.heapify(white_heap)
        
        # Use a max-heap for black buttons (simulated with negative values)
        black_heap = [-x for x in D]
        heapq.heapify(black_heap)
        
        # For each day, try to apply the best possible button
        total_uncompleted = 0
        for i in range(N):
            # Try to apply a white button if possible
            if white_heap:
                x = -heapq.heappop(white_heap)
                if A[i] >= x:
                    # Apply the white button
                    A[i] -= x
                    total_uncompleted += (A[i] - B[i])
                else:
                    # Put the button back
                    heapq.heappush(white_heap, -x)
            # Try to apply a black button if possible
            if black_heap:
                x = -heapq.heappop(black_heap)
                if B[i] + x <= A[i]:
                    # Apply the black button
                    B[i] += x
                    total_uncompleted += (A[i] - B[i])
                else:
                    # Put the button back
                    heapq.heappush(black_heap, -x)
        
        results.append(total_uncompleted)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()