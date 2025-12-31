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
        N = int(data[idx])
        Q = int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+N]))
        idx += N
        
        # For each element, store a sorted list of values to the right
        # and a dictionary to map value to list of indices
        from collections import defaultdict
        val_to_indices = defaultdict(list)
        right_sorted = [ [] for _ in range(N) ]
        
        for i in range(N-1, -1, -1):
            val = a[i]
            val_to_indices[val].append(i)
            # For the current i, find the next greater value to the right
            # using binary search on the right_sorted[i+1]
            if i < N-1:
                right_sorted[i] = right_sorted[i+1].copy()
            # Find the first value in right_sorted[i] that is greater than a[i]
            # using bisect
            pos = bisect.bisect_right(right_sorted[i], a[i])
            if pos < len(right_sorted[i]):
                right_sorted[i] = right_sorted[i][pos]
            else:
                right_sorted[i] = []
        
        for _ in range(Q):
            query = data[idx]
            idx += 1
            if query == '0':
                # Type 1 query: update a[A] to B
                A = int(data[idx])
                B = int(data[idx+1])
                idx += 2
                a[A] = B
                # Update the val_to_indices and right_sorted
                old_val = a[A]
                new_val = B
                # Remove old_val from val_to_indices
                for i in val_to_indices[old_val]:
                    if i == A:
                        val_to_indices[old_val].remove(i)
                        break
                # Add new_val to val_to_indices
                val_to_indices[new_val].append(A)
                # Rebuild right_sorted for A
                right_sorted[A] = []
                for i in range(A+1, N):
                    right_sorted[A].append(a[i])
                right_sorted[A].sort()
                # Find the first value in right_sorted[A] that is greater than a[A]
                pos = bisect.bisect_right(right_sorted[A], a[A])
                if pos < len(right_sorted[A]):
                    right_sorted[A] = right_sorted[A][pos]
                else:
                    right_sorted[A] = []
            else:
                # Type 2 query: find the next greater value to the right of A
                A = int(data[idx])
                idx += 1
                if not right_sorted[A]:
                    results.append("-1")
                else:
                    results.append(str(right_sorted[A]))
    
    print('\n'.join(results))