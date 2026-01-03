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
        
        # Use a priority queue (max heap) for white buttons
        white_heap = C
        # Use a priority queue (max heap) for black buttons
        black_heap = D
        
        # Use a priority queue (max heap) for diff
        diff_heap = []
        for i in range(N):
            heapq.heappush(diff_heap, -diff[i])
        
        # Process the buttons
        white_ptr = 0
        black_ptr = 0
        
        for i in range(N):
            # Try to use a white button if possible
            if white_ptr < K and diff[i] >= C[white_ptr]:
                # Use the white button
                diff[i] -= C[white_ptr]
                white_ptr += 1
                # Update the diff heap
                heapq.heappush(diff_heap, -diff[i])
            
            # Try to use a black button if possible
            if black_ptr < M and B[i] + D[black_ptr] <= A[i]:
                # Use the black button
                B[i] += D[black_ptr]
                black_ptr += 1
                # Update the diff heap
                heapq.heappush(diff_heap, -diff[i])
        
        # Calculate the total uncompleted tasks
        total = sum(-x for x in diff_heap)
        results.append(str(total))
    
    print('\n'.join(results))