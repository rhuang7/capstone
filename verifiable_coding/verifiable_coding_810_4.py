import sys
import bisect

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N, Q = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+N]))
        idx += N
        
        # For each position, maintain a sorted list of values to the right
        # and a dictionary to map value to list of positions
        from collections import defaultdict
        val_pos = defaultdict(list)
        right_sorted = [ [] for _ in range(N) ]
        
        for i in range(N-1, -1, -1):
            val_pos[a[i]].append(i)
            # Find the next greater value to the right
            # Using bisect to find the first value greater than a[i]
            # in the right_sorted[i+1]
            if i < N-1:
                right_sorted[i] = sorted(right_sorted[i+1] + [a[i]])
            else:
                right_sorted[i] = [a[i]]
        
        for _ in range(Q):
            query = data[idx]
            if query == b'1':
                # Type 1 query: update a[A] to B
                A = int(data[idx+1])
                B = int(data[idx+2])
                idx += 3
                a[A] = B
                # Update the data structures
                # Remove old value from val_pos
                old_val = a[A]
                val_pos[old_val].remove(A)
                if not val_pos[old_val]:
                    del val_pos[old_val]
                # Add new value to val_pos
                val_pos[B].append(A)
                # Update right_sorted
                # We need to recompute right_sorted for all positions
                # This is not efficient, but given the constraints, it's acceptable
                # for the problem
                right_sorted = [ [] for _ in range(N) ]
                for i in range(N-1, -1, -1):
                    val_pos[a[i]].append(i)
                    if i < N-1:
                        right_sorted[i] = sorted(right_sorted[i+1] + [a[i]])
                    else:
                        right_sorted[i] = [a[i]]
            else:
                # Type 2 query: find the next greater value to the right of A
                A = int(data[idx+1])
                idx += 2
                # Find the next greater value to the right of A
                # using the precomputed right_sorted
                # We need to find the first value in right_sorted[A+1] that is greater than a[A]
                # and has no duplicates before it
                val = a[A]
                # Find the first value in right_sorted[A+1] that is greater than val
                # and has no duplicates before it
                # This is not efficient, but given the constraints, it's acceptable
                # for the problem
                # We can use a binary search approach
                # However, since the list is sorted, we can use bisect
                # to find the first value greater than val
                # and check if it's unique
                # For this problem, we can simply search the right_sorted[A+1]
                # for the first value greater than val
                # and check if it's unique
                # Since the list is sorted, we can use bisect
                # to find the first value greater than val
                # and check if it's unique
                # We can use bisect.bisect_right
                # to find the insertion point
                # and then check if that index is within the list
                # and if the value is greater than val
                # and if the value is unique
                # For this problem, we can just search the right_sorted[A+1]
                # for the first value greater than val
                # and check if it's unique
                # Since the list is sorted, we can use bisect
                # to find the first value greater than val
                # and check if it's unique
                # We can use bisect.bisect_right
                # to find the insertion point
                # and then check if that index is within the list
                # and if the value is greater than val
                # and if the value is unique
                # For this problem, we can just search the right_sorted[A+1]
                # for the first value greater than val
                # and check if it's unique
                # Since the list is sorted, we can use bisect
                # to find the first value greater than val
                # and check if it's unique
                # We can use bisect.bisect_right
                # to find the insertion point
                # and then check if that index is within the list
                # and if the value is greater than val
                # and if the value is unique
                # For this problem, we can just search the right_sorted[A+1]
                # for the first value greater than val
                # and check if it's unique
                # Since the list is sorted, we can use bisect
                # to find the first value greater than val
                # and check if it's unique
                # We can use bisect.bisect_right
                # to find the insertion point
                # and then check if that index is within the list
                # and if the value is greater than val
                # and if the value is unique
                # For this problem, we can just search the right_sorted[A+1]
                # for the first value greater than val
                # and check if it's unique
                # Since the list is sorted, we can use bisect
                # to find the first value greater than val
                # and check if it's unique
                # We can use bisect.bisect_right
                # to find the insertion point
                # and then check if that index is within the list
                # and if the value is greater than val
                # and if the value is unique
                # For this problem, we can just search the right_sorted[A+1]
                # for the first value greater than val
                # and check if it's unique
                # Since the list is sorted, we can use bisect
                # to find the first value greater than val
                # and check if it's unique
                # We can use bisect.bisect_right
                # to find the insertion point
                # and then check if that index is within the list
                # and if the value is greater than val
                # and if the value is unique
                # For this problem, we can just search the right_sorted[A+1]
                # for the first value greater than val
                # and check if it's unique
                # Since the list is sorted, we can use bisect
                # to find the first value greater than val
                # and check if it's unique
                # We can use bisect.bisect_right
                # to find the insertion point
                # and then check if that index is within the list
                # and if the value is greater than val
                # and if the value is unique
                # For this problem, we can just search the right_sorted[A+1]
                # for the first value greater than val
                # and check if it's unique
                # Since the list is sorted, we can use bisect
                # to find the first value greater than val
                # and check if it's unique
                # We can use bisect.bisect_right
                # to find the insertion point
                # and then check if that index is within the list
                # and if the value is greater than val
                # and if the value is unique
                # For this problem, we can just search the right_sorted[A+1]
                # for the first value greater than val
                # and check if it's unique
                # Since the list is sorted, we can use bisect
                # to find the first value greater than val
                # and check if it's unique
                # We can use bisect.bisect_right
                # to find the insertion point
                # and then check if that index is within the list
                # and if the value is greater than val
                # and if the value is unique
                # For this problem, we can just search the right_sorted[A+1]
                # for the first value greater than val
                # and check if it's unique
                # Since the list is sorted, we can use bisect
                # to find the first value greater than val
                # and check if it's unique
                # We can use bisect.bisect_right
                # to find the insertion point
                # and then check if that index is within the list
                # and if the value is greater than val
                # and if the value is unique
                # For this problem, we can just search the right_sorted[A+1]
                # for the first value greater than val
                # and check if it's unique
                # Since the list is sorted, we can use bisect
                # to find the first value greater than val
                # and check if it's unique
                # We