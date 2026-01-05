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
        
        # For each day, compute the potential reduction in uncompleted tasks
        # Uncompleted tasks = A[i] - B[i]
        # We can reduce this by using a white button (if A[i] >= x) or increase B[i] by using a black button (if B[i] + x <= A[i])
        
        # Sort white buttons and black buttons
        C.sort()
        D.sort()
        
        # For each day, compute the maximum possible reduction
        # We can use a white button to reduce A[i] by x (if A[i] >= x)
        # Or a black button to increase B[i] by x (if B[i] + x <= A[i])
        
        # Use a priority queue to select the best buttons for each day
        # We'll use a max heap for white buttons and a max heap for black buttons
        white_heap = []
        black_heap = []
        
        for x in C:
            heapq.heappush(white_heap, -x)
        
        for x in D:
            heapq.heappush(black_heap, -x)
        
        # For each day, compute the best possible reduction
        total_uncompleted = 0
        used_white = 0
        used_black = 0
        
        for i in range(N):
            ai = A[i]
            bi = B[i]
            uncompleted = ai - bi
            total_uncompleted += uncompleted
            
            # Try to use a white button
            if white_heap:
                x = -heapq.heappop(white_heap)
                if ai >= x:
                    uncompleted -= x
                    total_uncompleted -= x
                    used_white += 1
            
            # Try to use a black button
            if black_heap:
                x = -heapq.heappop(black_heap)
                if bi + x <= ai:
                    uncompleted += x
                    total_uncompleted += x
                    used_black += 1
        
        results.append(total_uncompleted)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()