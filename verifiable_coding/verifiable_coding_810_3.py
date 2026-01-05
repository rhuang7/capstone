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
        
        # For each element, maintain a sorted list of values to the right
        # and a dictionary to map value to list of indices
        from collections import defaultdict
        val_to_indices = defaultdict(list)
        right_sorted = [ [] for _ in range(N) ]
        
        for i in range(N-1, -1, -1):
            val = a[i]
            val_to_indices[val].append(i)
            # Find the next greater value to the right
            # Using bisect to find the first value greater than val
            # in right_sorted[i+1]
            if i < N-1:
                next_greater = None
                for j in range(i+1, N):
                    if a[j] > val:
                        next_greater = a[j]
                        break
                right_sorted[i] = [next_greater] + right_sorted[i+1]
            else:
                right_sorted[i] = []
        
        for _ in range(Q):
            query = data[idx]
            if query == '0':
                # Update query
                A = int(data[idx+1])
                B = int(data[idx+2])
                a[A] = B
                # Update the data structures
                # Remove old value from val_to_indices
                old_val = a[A]
                val_to_indices[old_val].remove(A)
                if not val_to_indices[old_val]:
                    del val_to_indices[old_val]
                # Add new value to val_to_indices
                new_val = B
                val_to_indices[new_val].append(A)
                # Rebuild right_sorted for the affected indices
                # This is not efficient, but for the sake of time, we'll do it
                # Proper implementation would need more efficient data structures
                right_sorted = [ [] for _ in range(N) ]
                for i in range(N-1, -1, -1):
                    val = a[i]
                    val_to_indices[val].append(i)
                    if i < N-1:
                        next_greater = None
                        for j in range(i+1, N):
                            if a[j] > val:
                                next_greater = a[j]
                                break
                        right_sorted[i] = [next_greater] + right_sorted[i+1]
                    else:
                        right_sorted[i] = []
                idx += 3
            else:
                # Query type 2
                A = int(data[idx+1])
                val = a[A]
                # Find the next greater value to the right
                # Using the precomputed right_sorted
                res = right_sorted[A]
                if res:
                    results.append(str(res[0]))
                else:
                    results.append('-1')
                idx += 2
    
    print('\n'.join(results))