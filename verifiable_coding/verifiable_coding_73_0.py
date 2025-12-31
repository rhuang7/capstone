import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Check if already non-decreasing
        is_non_decreasing = True
        for i in range(n-1):
            if a[i] > a[i+1]:
                is_non_decreasing = False
                break
        if is_non_decreasing:
            results.append("0")
            results.append("")
            continue
        
        # Try to make the array non-decreasing
        # We will try to fix the array by replacing elements with MEX
        # We will use a greedy approach to fix the array
        
        # Create a copy of the array
        arr = a[:]
        operations = []
        
        # We will try to fix the array by making it non-decreasing
        # We will iterate through the array and fix each element
        # If the current element is not in the correct position, we will replace it with MEX
        # We will do this up to 2n times
        
        for _ in range(2 * n):
            # Compute MEX
            mex = 0
            while mex in arr:
                mex += 1
            
            # Try to fix the array
            for i in range(n):
                if arr[i] > arr[i+1] if i < n-1 else False:
                    # Replace arr[i] with mex
                    arr[i] = mex
                    operations.append(i+1)
                    break
            else:
                # If the array is now non-decreasing
                break
        
        # Check if the array is non-decreasing
        is_non_decreasing = True
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                is_non_decreasing = False
                break
        
        # If not, we need to do more operations
        # But according to the problem statement, it is always possible to do it in 2n operations
        # So we can just keep doing operations until the array is non-decreasing
        
        # We will continue until the array is non-decreasing
        while not is_non_decreasing:
            # Compute MEX
            mex = 0
            while mex in arr:
                mex += 1
            
            # Replace the first element with mex
            arr[0] = mex
            operations.append(1)
            is_non_decreasing = True
            for i in range(n-1):
                if arr[i] > arr[i+1]:
                    is_non_decreasing = False
                    break
        
        # Output the result
        results.append(str(len(operations)))
        results.append(' '.join(map(str, operations)))
    
    print('\n'.join(results))