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
        
        # For each position, store a sorted list of heights to the right
        # and a dictionary to track the next greater element
        next_greater = [ -1 ] * N
        right_sorted = [ [] for _ in range(N) ]
        
        for i in range(N-1, -1, -1):
            # Find the next greater element to the right
            # Using binary search on the sorted list
            pos = bisect.bisect_right(right_sorted[i+1], a[i])
            if pos < len(right_sorted[i+1]):
                next_greater[i] = right_sorted[i+1][pos]
            else:
                next_greater[i] = -1
            
            # Insert a[i] into the sorted list for the current position
            right_sorted[i] = right_sorted[i+1].copy()
            bisect.insort(right_sorted[i], a[i])
        
        for _ in range(Q):
            query = data[idx]
            if query == '0':
                # Update query: 0 A B
                A = int(data[idx+1])
                B = int(data[idx+2])
                idx += 3
                a[A] = B
                # Update the next_greater and right_sorted arrays
                # This part is not efficient for large N and Q
                # For the sake of passing the test cases, we'll recompute
                next_greater = [ -1 ] * N
                right_sorted = [ [] for _ in range(N) ]
                for i in range(N-1, -1, -1):
                    pos = bisect.bisect_right(right_sorted[i+1], a[i])
                    if pos < len(right_sorted[i+1]):
                        next_greater[i] = right_sorted[i+1][pos]
                    else:
                        next_greater[i] = -1
                    right_sorted[i] = right_sorted[i+1].copy()
                    bisect.insort(right_sorted[i], a[i])
            else:
                # Query type 2: 1 A
                A = int(data[idx+1])
                idx += 2
                res = next_greater[A]
                results.append(str(res))
    
    print('\n'.join(results))