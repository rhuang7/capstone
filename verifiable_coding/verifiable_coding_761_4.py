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
        
        white = C
        black = D
        
        # Sort white buttons in descending order
        white.sort(reverse=True)
        # Sort black buttons in descending order
        black.sort(reverse=True)
        
        # For each day, calculate the potential reduction in uncompleted tasks
        # Uncompleted tasks = A[i] - B[i]
        # We can use white buttons to reduce A[i] and black buttons to increase B[i]
        # We need to choose which buttons to use optimally
        
        # Use a priority queue (max heap) for white buttons
        white_heap = white
        # Use a priority queue (max heap) for black buttons
        black_heap = black
        
        # For each day, calculate the maximum possible reduction
        # We can use a greedy approach: use the largest possible white button on days where A[i] - B[i] is large
        # and the largest possible black button on days where B[i] is small
        
        # Create a list of (uncompleted, A[i], B[i]) for each day
        days = []
        for i in range(N):
            uncompleted = A[i] - B[i]
            days.append((uncompleted, A[i], B[i]))
        
        # Sort days by uncompleted in descending order
        days.sort(reverse=True)
        
        # Use white buttons on days with the highest uncompleted
        # Use black buttons on days with the lowest B[i]
        # We can use a priority queue for B[i] (min heap)
        B_min_heap = []
        for i in range(N):
            heapq.heappush(B_min_heap, (B[i], i))
        
        # Use white buttons on the first K days with highest uncompleted
        # Use black buttons on the first M days with lowest B[i]
        # But we need to ensure that we don't use the same button more than once
        
        # We need to track which buttons are used
        used_white = [False] * K
        used_black = [False] * M
        
        # Use white buttons on the first K days with highest uncompleted
        white_used = 0
        for i in range(N):
            if white_used >= K:
                break
            if days[i][0] > 0:
                # Try to use a white button
                if white_heap:
                    x = white_heap[0]
                    if days[i][1] >= x:
                        # Use this white button
                        days[i] = (days[i][0] - x, days[i][1], days[i][2])
                        white_used += 1
                        heapq.heappop(white_heap)
        
        # Use black buttons on the first M days with lowest B[i]
        black_used = 0
        while black_used < M and B_min_heap:
            b, i = heapq.heappop(B_min_heap)
            if days[i][2] + black_heap[0] <= days[i][1]:
                # Use this black button
                days[i] = (days[i][0], days[i][1], days[i][2] + black_heap[0])
                black_used += 1
                heapq.heappop(black_heap)
        
        # Calculate the total uncompleted tasks
        total = 0
        for uncompleted, _, _ in days:
            total += uncompleted
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()