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
        
        # Make a copy to avoid modifying the original
        arr = a[:]
        # We will try to make the array non-decreasing
        # First, check if it is already non-decreasing
        is_non_decreasing = True
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                is_non_decreasing = False
                break
        if is_non_decreasing:
            results.append("0")
            results.append("")
            continue
        
        # Otherwise, we need to perform operations
        # We will try to make the array non-decreasing by fixing elements
        # We will use the MEX to replace elements
        # We will keep track of the operations
        operations = []
        
        # We will try to make the array non-decreasing by fixing elements
        # We will go through each element and try to fix it
        # If the current element is not in the correct position, we will replace it with the MEX
        # We will repeat this process until the array is non-decreasing
        # We will do this in at most 2n operations
        # We will keep track of the current MEX
        mex = 0
        while True:
            # Compute the current MEX
            mex = 0
            while mex in arr:
                mex += 1
            # If the array is already non-decreasing, break
            is_non_decreasing = True
            for i in range(n-1):
                if arr[i] > arr[i+1]:
                    is_non_decreasing = False
                    break
            if is_non_decreasing:
                break
            # Otherwise, find the first element that is not in the correct position
            # and replace it with the MEX
            for i in range(n):
                if arr[i] > arr[i+1] if i < n-1 else False:
                    # Replace this element with the MEX
                    arr[i] = mex
                    operations.append(i+1)
                    break
            # If we have performed 2n operations, break
            if len(operations) >= 2 * n:
                break
        
        results.append(str(len(operations)))
        results.append(' '.join(map(str, operations)))
    
    print('\n'.join(results))