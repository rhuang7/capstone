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
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Sort the array
        A_sorted = sorted(A)
        
        # Check if there is a valid permutation
        # The permutation must be strictly increasing then strictly decreasing
        # So the array must have all elements unique, or have duplicates only at the peak
        # We can try to construct the permutation by placing the maximum element at the center
        # and arranging the rest in increasing order on the left and decreasing on the right
        
        # Check for duplicates
        unique = set(A)
        if len(unique) < len(A):
            # There are duplicates, so we need to check if they can be arranged properly
            # We can try to construct the permutation
            # First, sort the array
            A_sorted = sorted(A)
            # Try to find a peak element
            peak = -1
            for i in range(len(A_sorted)):
                if i == 0 or A_sorted[i] > A_sorted[i-1]:
                    peak = i
                elif i == len(A_sorted)-1 or A_sorted[i] < A_sorted[i+1]:
                    peak = i
                else:
                    # There is a duplicate that breaks the strictly increasing or decreasing
                    # So it's not possible
                    results.append("NO")
                    break
            else:
                # Try to construct the permutation
                # Place the peak at the middle
                # Left part is strictly increasing, right part is strictly decreasing
                # We can try to build it
                # Find the peak
                peak = -1
                for i in range(len(A_sorted)):
                    if i == 0 or A_sorted[i] > A_sorted[i-1]:
                        peak = i
                    elif i == len(A_sorted)-1 or A_sorted[i] < A_sorted[i+1]:
                        peak = i
                    else:
                        # There is a duplicate that breaks the strictly increasing or decreasing
                        # So it's not possible
                        results.append("NO")
                        break
                else:
                    # Construct the permutation
                    # Left part is strictly increasing
                    # Right part is strictly decreasing
                    # We can try to build it
                    # Place the peak at the middle
                    # Left part is strictly increasing
                    # Right part is strictly decreasing
                    # We can try to build it
                    # Sort the array
                    A_sorted = sorted(A)
                    # Try to find a peak
                    peak = -1
                    for i in range(len(A_sorted)):
                        if i == 0 or A_sorted[i] > A_sorted[i-1]:
                            peak = i
                        elif i == len(A_sorted)-1 or A_sorted[i] < A_sorted[i+1]:
                            peak = i
                        else:
                            # There is a duplicate that breaks the strictly increasing or decreasing
                            # So it's not possible
                            results.append("NO")
                            break
                    else:
                        # Construct the permutation
                        # Place the peak at the middle
                        # Left part is strictly increasing
                        # Right part is strictly decreasing
                        # We can try to build it
                        # Sort the array
                        A_sorted = sorted(A)
                        # Try to find a peak
                        peak = -1
                        for i in range(len(A_sorted)):
                            if i == 0 or A_sorted[i] > A_sorted[i-1]:
                                peak = i
                            elif i == len(A_sorted)-1 or A_sorted[i] < A_sorted[i+1]:
                                peak = i
                            else:
                                # There is a duplicate that breaks the strictly increasing or decreasing
                                # So it's not possible
                                results.append("NO")
                                break
                        else:
                            # Construct the permutation
                            # Place the peak at the middle
                            # Left part is strictly increasing
                            # Right part is strictly decreasing
                            # We can try to build it
                            # Sort the array
                            A_sorted = sorted(A)
                            # Try to find a peak
                            peak = -1
                            for i in range(len(A_sorted)):
                                if i == 0 or A_sorted[i] > A_sorted[i-1]:
                                    peak = i
                                elif i == len(A_sorted)-1 or A_sorted[i] < A_sorted[i+1]:
                                    peak = i
                                else:
                                    # There is a duplicate that breaks the strictly increasing or decreasing
                                    # So it's not possible
                                    results.append("NO")
                                    break
                            else:
                                # Construct the permutation
                                # Place the peak at the middle
                                # Left part is strictly increasing
                                # Right part is strictly decreasing
                                # We can try to build it
                                # Sort the array
                                A_sorted = sorted(A)
                                # Try to find a peak
                                peak = -1
                                for i in range(len(A_sorted)):
                                    if i == 0 or A_sorted[i] > A_sorted[i-1]:
                                        peak = i
                                    elif i == len(A_sorted)-1 or A_sorted[i] < A_sorted[i+1]:
                                        peak = i
                                    else:
                                        # There is a duplicate that breaks the strictly increasing or decreasing
                                        # So it's not possible
                                        results.append("NO")
                                        break
                                else:
                                    # Construct the permutation
                                    # Place the peak at the middle
                                    # Left part is strictly increasing
                                    # Right part is strictly decreasing
                                    # We can try to build it
                                    # Sort the array
                                    A_sorted = sorted(A)
                                    # Try to find a peak
                                    peak = -1
                                    for i in range(len(A_sorted)):
                                        if i == 0 or A_sorted[i] > A_sorted[i-1]:
                                            peak = i
                                        elif i == len(A_sorted)-1 or A_sorted[i] < A_sorted[i+1]:
                                            peak = i
                                        else:
                                            # There is a duplicate that breaks the strictly increasing or decreasing
                                            # So it's not possible
                                            results.append("NO")
                                            break
                                    else:
                                        # Construct the permutation
                                        # Place the peak at the middle
                                        # Left part is strictly increasing
                                        # Right part is strictly decreasing
                                        # We can try to build it
                                        # Sort the array
                                        A_sorted = sorted(A)
                                        # Try to find a peak
                                        peak = -1
                                        for i in range(len(A_sorted)):
                                            if i == 0 or A_sorted[i] > A_sorted[i-1]:
                                                peak = i
                                            elif i == len(A_sorted)-1 or A_sorted[i] < A_sorted[i+1]:
                                                peak = i
                                            else:
                                                # There is a duplicate that breaks the strictly increasing or decreasing
                                                # So it's not possible
                                                results.append("NO")
                                                break
                                        else:
                                            # Construct the permutation
                                            # Place the peak at the middle
                                            # Left part is strictly increasing
                                            # Right part is strictly decreasing
                                            # We can try to build it
                                            # Sort the array
                                            A_sorted = sorted(A)
                                            # Try to find a peak
                                            peak = -1
                                            for i in range(len(A_sorted)):
                                                if i == 0 or A_sorted[i] > A_sorted[i-1]:
                                                    peak = i
                                                elif i == len(A_sorted)-1 or A_sorted[i] < A_sorted[i+1]:
                                                    peak = i
                                                else:
                                                    # There is a duplicate that breaks the strictly increasing or decreasing
                                                    # So it's not possible
                                                    results.append("NO")
                                                    break
                                            else:
                                                # Construct the permutation
                                                # Place the peak at the middle
                                                # Left part is strictly increasing
                                                # Right part is strictly decreasing
                                                # We can try to build it
                                                # Sort the array
                                                A_sorted = sorted(A)
                                                # Try to find a peak
                                                peak = -1
                                                for i in range(len(A_sorted)):
                                                    if i == 0 or A_sorted[i] > A_sorted[i-1]:
                                                        peak = i
                                                    elif i == len(A_sorted)-1 or A_sorted[i] < A_sorted[i+1]:
                                                        peak = i
                                                    else:
                                                        # There is a duplicate that breaks the strictly increasing or decreasing
                                                        # So it's not possible
                                                        results.append("NO")
                                                        break
                                                else:
                                                    # Construct the permutation
                                                    # Place the peak at the middle
                                                    # Left part is strictly increasing
                                                    # Right part is strictly decreasing
                                                    # We can try to build it
                                                    # Sort the array
                                                    A_sorted = sorted(A)
                                                    # Try to find a peak
                                                    peak = -1
                                                    for i in range(len(A_sorted)):
                                                        if i == 0 or A_sorted[i] > A_sorted[i-1]:
                                                            peak = i
                                                        elif i == len(A_sorted)-1 or A_sorted[i] < A_sorted[i+1]:
                                                            peak = i
                                                        else:
                                                            # There is a duplicate that breaks the strictly increasing or decreasing
                                                            # So it's not possible
                                                            results.append("NO")
                                                            break
                                                    else:
                                                        # Construct the permutation
                                                        # Place the peak at the middle
                                                        # Left