import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        arr = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Create a new array to store the result
        result = []
        # Use a heap to get the smallest element
        import heapq
        heapq.heapify(arr)
        # Get the smallest element
        smallest = heapq.heappop(arr)
        result.append(smallest)
        
        # Use a heap to get the largest element
        heapq.heapify(arr)
        largest = heapq.heappop(arr)
        result.append(largest)
        
        # Remaining elements
        while arr:
            # Get the smallest and largest elements
            smallest = heapq.heappop(arr)
            largest = heapq.heappop(arr)
            result.append(smallest)
            result.append(largest)
        
        # Check if the length is correct
        if len(result) != N:
            result = result[:N]
        
        results.append(' '.join(map(str, result)))
    
    print('\n'.join(results))