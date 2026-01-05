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
        
        # For each element, store a sorted list of values to the right
        # and a dictionary to map value to list of indices
        from collections import defaultdict
        val_to_indices = defaultdict(list)
        right_sorted = [ [] for _ in range(N) ]
        
        for i in range(N-1, -1, -1):
            val = a[i]
            val_to_indices[val].append(i)
            # Insert into right_sorted[i] in sorted order
            bisect.insort(right_sorted[i], val)
        
        for _ in range(Q):
            query = data[idx]
            if query == '0':
                # Type 1: update
                A = int(data[idx+1])
                B = int(data[idx+2])
                idx += 3
                a[A] = B
                # Update val_to_indices and right_sorted
                old_val = a[A]
                new_val = B
                # Remove old_val from val_to_indices
                val_to_indices[old_val].remove(A)
                if len(val_to_indices[old_val]) == 0:
                    del val_to_indices[old_val]
                # Add new_val to val_to_indices
                val_to_indices[new_val].append(A)
                # Update right_sorted for A
                bisect.insort(right_sorted[A], new_val)
                bisect.insort(right_sorted[A], new_val)
            else:
                # Type 2: query
                A = int(data[idx+1])
                idx += 2
                val = a[A]
                # Find the next greater value to the right of A
                # that is not present in the values up to A
                # We need to find the smallest value greater than val
                # in right_sorted[A]
                # and check if it's not in the values up to A
                # We can use a set to store the values up to A
                # but for efficiency, we can use a binary search
                # on the right_sorted[A]
                # Since right_sorted[A] is sorted, we can find the first value > val
                # and check if it's not in the values up to A
                # However, since the values up to A are not stored, we can't do that
                # So we need to find the first value > val in right_sorted[A]
                # and check if it's not in the values up to A
                # But how?
                # We can use a set of values up to A
                # But since we can't store it for each A, we need to find it on the fly
                # So we can use a binary search on right_sorted[A]
                # to find the first value > val
                # and then check if that value is not in the values up to A
                # But how to check if it's not in the values up to A?
                # We can use a set of values up to A
                # But since we can't store it for each A, we need to find it on the fly
                # So we can use a binary search on right_sorted[A]
                # to find the first value > val
                # and then check if that value is not in the values up to A
                # But how to check if it's not in the values up to A?
                # We can use a binary search on the values up to A
                # But since we can't store them, we need to find them on the fly
                # So we can use a binary search on the array a[0..A]
                # to find if the value exists
                # But that would be O(N) per query, which is too slow
                # So we need a better approach
                # We can precompute for each position A, a set of values up to A
                # But that would take O(N^2) space, which is not feasible
                # So we need to find a way to check if a value exists in a[0..A]
                # using a binary search on the array
                # So we can use a binary search on the array a[0..A]
                # to find if the value exists
                # But how?
                # We can use a binary search on the array a[0..A]
                # to find if the value exists
                # So for the value found in right_sorted[A], we can check if it exists in a[0..A]
                # If it does, we need to find the next one
                # So the algorithm is:
                # 1. Find the first value in right_sorted[A] that is > val
                # 2. Check if that value exists in a[0..A]
                # 3. If it does, move to the next one
                # 4. Repeat until we find a value that does not exist in a[0..A]
                # 5. If none found, return -1
                # But how to check if a value exists in a[0..A]?
                # We can use a binary search on the array a[0..A]
                # So for each candidate value, we can perform a binary search on a[0..A]
                # to see if it exists
                # This is O(log N) per check
                # So the total time per query is O(log N * log N)
                # Which is acceptable for N=1e4 and Q=1e4
                # So let's implement this
                # Find the first value in right_sorted[A] that is > val
                # Using bisect
                pos = bisect.bisect_right(right_sorted[A], val)
                if pos < len(right_sorted[A]):
                    candidate = right_sorted[A][pos]
                    # Check if candidate exists in a[0..A]
                    # Binary search in a[0..A]
                    left = 0
                    right = A
                    found = False
                    while left <= right:
                        mid = (left + right) // 2
                        if a[mid] == candidate:
                            found = True
                            break
                        elif a[mid] < candidate:
                            left = mid + 1
                        else:
                            right = mid - 1
                    if not found:
                        results.append(str(candidate))
                    else:
                        # Need to find the next one
                        # So we need to find the next value in right_sorted[A] that is > val
                        # and not in a[0..A]
                        # We can loop through the right_sorted[A] starting from pos
                        # and check each value
                        # But this could be O(N) in the worst case
                        # So we need a way to find the next value efficiently
                        # So we can loop through the right_sorted[A] starting from pos
                        # and for each value, check if it exists in a[0..A]
                        # If not, return it
                        # If yes, continue
                        # This is O(K log N) where K is the number of values to check
                        # Which is acceptable for small K
                        # So we can do this
                        found_val = -1
                        for i in range(pos, len(right_sorted[A])):
                            candidate = right_sorted[A][i]
                            left = 0
                            right = A
                            found = False
                            while left <= right:
                                mid = (left + right) // 2
                                if a[mid] == candidate:
                                    found = True
                                    break
                                elif a[mid] < candidate:
                                    left = mid + 1
                                else:
                                    right = mid - 1
                            if not found:
                                found_val = candidate
                                break
                        results.append(str(found_val) if found_val != -1 else "-1")
                else:
                    results.append("-1")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()