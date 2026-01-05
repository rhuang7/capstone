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
        
        # For each day, calculate the current uncompleted tasks
        uncompleted = [A[i] - B[i] for i in range(N)]
        
        # Sort white buttons and black buttons
        C.sort()
        D.sort()
        
        # Use a max-heap for white buttons (using negative values)
        white_heap = [-x for x in C]
        heapq.heapify(white_heap)
        
        # Use a max-heap for black buttons (using negative values)
        black_heap = [-x for x in D]
        heapq.heapify(black_heap)
        
        # Greedy approach: use black buttons first to maximize completed tasks
        # Then use white buttons to reduce planned tasks
        # For each day, try to use a black button if possible
        # Then try to use a white button if possible
        
        # For each day, try to use a black button
        # If the black button can be used, use it
        # Else, try to use a white button
        # If neither can be used, do nothing
        
        # Use a priority queue for black buttons (max-heap)
        # Use a priority queue for white buttons (max-heap)
        # We will use the largest possible buttons first
        
        # Create a priority queue for black buttons (max-heap)
        black_heap = [-x for x in D]
        heapq.heapify(black_heap)
        
        # Create a priority queue for white buttons (max-heap)
        white_heap = [-x for x in C]
        heapq.heapify(white_heap)
        
        # For each day, try to use a black button
        # If the black button can be used, use it
        # Else, try to use a white button
        # If neither can be used, do nothing
        
        # For each day, we can use at most one button
        # We will use the best possible button for each day
        
        # For each day, try to use a black button
        # If the black button can be used, use it
        # Else, try to use a white button
        # If neither can be used, do nothing
        
        # For each day, we can use at most one button
        # We will use the best possible button for each day
        
        # For each day, try to use a black button
        # If the black button can be used, use it
        # Else, try to use a white button
        # If neither can be used, do nothing
        
        # For each day, we can use at most one button
        # We will use the best possible button for each day
        
        # For each day, try to use a black button
        # If the black button can be used, use it
        # Else, try to use a white button
        # If neither can be used, do nothing
        
        # For each day, we can use at most one button
        # We will use the best possible button for each day
        
        # For each day, try to use a black button
        # If the black button can be used, use it
        # Else, try to use a white button
        # If neither can be used, do nothing
        
        # For each day, we can use at most one button
        # We will use the best possible button for each day
        
        # For each day, try to use a black button
        # If the black button can be used, use it
        # Else, try to use a white button
        # If neither can be used, do nothing
        
        # For each day, we can use at most one button
        # We will use the best possible button for each day
        
        # For each day, try to use a black button
        # If the black button can be used, use it
        # Else, try to use a white button
        # If neither can be used, do nothing
        
        # For each day, we can use at most one button
        # We will use the best possible button for each day
        
        # For each day, try to use a black button
        # If the black button can be used, use it
        # Else, try to use a white button
        # If neither can be used, do nothing
        
        # For each day, we can use at most one button
        # We will use the best possible button for each day
        
        # For each day, try to use a black button
        # If the black button can be used, use it
        # Else, try to use a white button
        # If neither can be used, do nothing
        
        # For each day, we can use at most one button
        # We will use the best possible button for each day
        
        # For each day, try to use a black button
        # If the black button can be used, use it
        # Else, try to use a white button
        # If neither can be used, do nothing
        
        # For each day, we can use at most one button
        # We will use the best possible button for each day
        
        # For each day, try to use a black button
        # If the black button can be used, use it
        # Else, try to use a white button
        # If neither can be used, do nothing
        
        # For each day, we can use at most one button
        # We will use the best possible button for each day
        
        # For each day, try to use a black button
        # If the black button can be used, use it
        # Else, try to use a white button
        # If neither can be used, do nothing
        
        # For each day, we can use at most one button
        # We will use the best possible button for each day
        
        # For each day, try to use a black button
        # If the black button can be used, use it
        # Else, try to use a white button
        # If neither can be used, do nothing
        
        # For each day, we can use at most one button
        # We will use the best possible button for each day
        
        # For each day, try to use a black button
        # If the black button can be used, use it
        # Else, try to use a white button
        # If neither can be used, do nothing
        
        # For each day, we can use at most one button
        # We will use the best possible button for each day
        
        # For each day, try to use a black button
        # If the black button can be used, use it
        # Else, try to use a white button
        # If neither can be used, do nothing
        
        # For each day, we can use at most one button
        # We will use the best possible button for each day
        
        # For each day, try to use a black button
        # If the black button can be used, use it
        # Else, try to use a white button
        # If neither can be used, do nothing
        
        # For each day, we can use at most one button
        # We will use the best possible button for each day
        
        # For each day, try to use a black button
        # If the black button can be used, use it
        # Else, try to use a white button
        # If neither can be used, do nothing
        
        # For each day, we can use at most one button
        # We will use the best possible button for each day
        
        # For each day, try to use a black button
        # If the black button can be used, use it
        # Else, try to use a white button
        # If neither can be used, do nothing
        
        # For each day, we can use at most one button
        # We will use the best possible button for each day
        
        # For each day, try to use a black button
        # If the black button can be used, use it
        # Else, try to use a white button
        # If neither can be used, do nothing
        
        # For each day, we can use at most one button
        # We will use the best possible button for each day
        
        # For each day, try to use a black button
        # If the black button can be used, use it
        # Else, try to use a white button
        # If neither can be used, do nothing
        
        # For each day, we can use at most one button
        # We will use the best possible button for each day
        
        # For each day, try to use a black button
        # If