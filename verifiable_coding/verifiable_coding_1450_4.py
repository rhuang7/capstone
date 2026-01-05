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
        # Use a pointer to track the current position
        ptr = 0
        
        # Iterate through the array and build the result
        while ptr < N:
            # Find the next element that is smaller than the current element
            # This is the peak element
            peak = arr[ptr]
            # Find the next element that is smaller than the peak
            next_smaller = None
            for i in range(ptr + 1, N):
                if arr[i] < peak:
                    next_smaller = arr[i]
                    break
            # If no next smaller element, use the last element
            if next_smaller is None:
                next_smaller = arr[-1]
            # Add the peak and next smaller to the result
            result.append(peak)
            result.append(next_smaller)
            # Move the pointer to the next position after the next smaller
            ptr = i + 1
        
        # Join the result and add to results
        results.append(' '.join(map(str, result)))
    
    # Print all results
    print('\n'.join(results))

if __name__ == '__main__':
    solve()