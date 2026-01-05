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
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Sort the array in non-decreasing order
        a.sort()
        
        # Initialize the total number of operations
        total_ops = 0
        
        # We can perform operations on the smallest elements
        # to accumulate the sum without exceeding k
        # We use a greedy approach to maximize the number of operations
        # by always adding the smallest possible element to the next one
        # and keeping track of the sum
        
        # We use a priority queue (min-heap) to efficiently get the smallest elements
        import heapq
        heap = a.copy()
        heapq.heapify(heap)
        
        while True:
            # If there are less than two elements, we can't perform any more operations
            if len(heap) < 2:
                break
            
            # Get the two smallest elements
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            
            # If adding x to y would exceed k, we can't perform this operation
            if x + y > k:
                # Put back the smaller one (since we can't add it to the larger one)
                heapq.heappush(heap, x)
                break
            
            # Perform the operation
            total_ops += 1
            # The new value is x + y, and we push it back into the heap
            heapq.heappush(heap, x + y)
        
        results.append(str(total_ops))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()