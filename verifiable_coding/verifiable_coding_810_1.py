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
        
        # For each position, store a sorted list of values to the right
        right_sorted = [ [] for _ in range(N) ]
        for i in range(N-2, -1, -1):
            right_sorted[i] = right_sorted[i+1].copy()
            bisect.insort(right_sorted[i], a[i+1])
        
        for _ in range(Q):
            query = data[idx]
            if query == b'1':
                # Type 1 query: update a[A] to B
                A = int(data[idx+1])
                B = int(data[idx+2])
                idx += 3
                a[A] = B
                # Update the right_sorted arrays
                for i in range(A, N-1):
                    right_sorted[i] = right_sorted[i+1].copy()
                    bisect.insort(right_sorted[i], a[i+1])
            else:
                # Type 2 query: find next greater value to the right of A
                A = int(data[idx+1])
                idx += 2
                val = a[A]
                # Find the first value in right_sorted[A] that is greater than val
                # and has no duplicates before it
                # We need to find the first value in right_sorted[A] that is greater than val
                # and is the first occurrence of that value
                # So we search in right_sorted[A] for the first value > val
                # and check if it's the first occurrence
                # Since right_sorted[A] is sorted, we can use bisect
                pos = bisect.bisect_right(right_sorted[A], val)
                if pos < len(right_sorted[A]):
                    # Check if this value is the first occurrence
                    # We need to find the first occurrence of right_sorted[A][pos]
                    # in the right_sorted[A] list
                    # Since the list is sorted, we can use bisect_left
                    first_pos = bisect.bisect_left(right_sorted[A], right_sorted[A][pos])
                    if first_pos == pos:
                        results.append(str(right_sorted[A][pos]))
                    else:
                        results.append("-1")
                else:
                    results.append("-1")
    
    print("\n".join(results))