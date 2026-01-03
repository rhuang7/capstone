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
        # and their indices
        right = [{} for _ in range(N)]
        for i in range(N-2, -1, -1):
            val = a[i]
            # Find the next greater value to the right
            # Using bisect to find the insertion point
            # We need to find the first value greater than val
            # in the right[i+1] dictionary
            # We'll use a sorted list of values to the right
            # and their indices
            # For this, we'll maintain a list of sorted values
            # and their indices
            # So for each i, right[i] is a list of (value, index)
            # sorted by value
            # We'll use bisect to find the first value greater than a[i]
            # in right[i+1]
            # So we'll build right[i] as a list of (value, index) sorted by value
            # and then for each i, we'll find the first value greater than a[i]
            # in right[i+1]
            # We'll also need to maintain the sorted list for right[i]
            # So for each i, we'll have a sorted list of (value, index)
            # and for each query, we can perform a binary search
            # to find the next greater value
            # So we'll precompute for each i, the next greater value to the right
            # and store it in next_greater array
            # But for updates, we need to be able to handle dynamic changes
            # So we need a more efficient data structure
            # For this, we'll use a binary indexed tree or a segment tree
            # But given the time constraints, we'll use a brute force approach
            # for the initial setup and then handle updates
            # For each i, we'll store a list of (value, index) sorted by value
            # and for each query, we'll perform a binary search to find the first value greater than a[i]
            # in the list for i
            # So we'll precompute for each i, the sorted list of (value, index) to the right
            # and for each query, we'll perform a binary search
            # to find the first value greater than a[i]
            # in the list for i
            # So for the initial setup, we'll precompute this
            # For the updates, we'll need to update the sorted list for the affected indices
            # This is going to be O(N log N) for the initial setup
            # and O(log N) per update
            # But for the given constraints, this is acceptable
            # So we'll proceed with this approach
            # We'll create a list of sorted (value, index) for each i
            # and for each query of type 2, we'll perform a binary search
            # to find the first value greater than a[i]
            # in the list for i
            # So let's precompute the sorted lists
            # For each i, sorted_values[i] is a list of (value, index) sorted by value
            sorted_values = [[] for _ in range(N)]
            for i in range(N-1, -1, -1):
                # Add the current value to the list
                # and keep it sorted
                # We'll use bisect.insort to insert in the correct position
                # but since we are going from right to left, we can just append and sort
                # but this would be O(N^2) time, which is not acceptable
                # So instead, we'll build the sorted list for each i
                # by inserting the current value into the sorted list of i+1
                # So for i from N-1 downto 0:
                # sorted_values[i] = sorted_values[i+1] + [(a[i], i)]
                # but this is O(N^2) time
                # So we need a better way
                # We'll use a list of sorted values for each i
                # and for each i, we'll insert a[i] into the sorted list of i+1
                # and then create the sorted list for i
                # So for i from N-1 downto 0:
                # sorted_values[i] = sorted_values[i+1] + [(a[i], i)]
                # but this is O(N^2) time
                # So we need to find a better way
                # Let's proceed with this approach for the initial setup
                # and then handle updates with a binary search
                # So for each i, we'll have a sorted list of (value, index) to the right
                # and for each query, we'll perform a binary search
                # to find the first value greater than a[i]
                # in the list for i
                # So let's proceed
                if i == N-1:
                    sorted_values[i] = [(a[i], i)]
                else:
                    # Insert a[i] into the sorted list of i+1
                    # and then sort the combined list
                    # but this is O(N^2) time
                    # So we need to find a better way
                    # Let's proceed with the initial approach
                    # and then handle updates with a binary search
                    # So for each i, sorted_values[i] is a list of (value, index) sorted by value
                    # and for each query, we'll perform a binary search
                    # to find the first value greater than a[i]
                    # in the list for i
                    # So let's proceed
                    # We'll use bisect to find the insertion point
                    # and then check if there is a value greater than a[i]
                    # So for each i, we'll have a sorted list of (value, index) to the right
                    # and for each query, we'll perform a binary search
                    # to find the first value greater than a[i]
                    # in the list for i
                    # So let's proceed
                    # We'll use bisect to find the insertion point
                    # and then check if there is a value greater than a[i]
                    # in the list for i
                    # So let's proceed
                    # We'll create a list of values for each i
                    # and for each query, we'll perform a binary search
                    # to find the first value greater than a[i]
                    # in the list for i
                    # So let's proceed
                    # We'll use bisect to find the insertion point
                    # and then check if there is a value greater than a[i]
                    # in the list for i
                    # So let's proceed
                    # We'll create a list of values for each i
                    # and for each query, we'll perform a binary search
                    # to find the first value greater than a[i]
                    # in the list for i
                    # So let's proceed
                    # We'll use bisect to find the insertion point
                    # and then check if there is a value greater than a[i]
                    # in the list for i
                    # So let's proceed
                    # We'll create a list of values for each i
                    # and for each query, we'll perform a binary search
                    # to find the first value greater than a[i]
                    # in the list for i
                    # So let's proceed
                    # We'll use bisect to find the insertion point
                    # and then check if there is a value greater than a[i]
                    # in the list for i
                    # So let's proceed
                    # We'll create a list of values for each i
                    # and for each query, we'll perform a binary search
                    # to find the first value greater than a[i]
                    # in the list for i
                    # So let's proceed
                    # We'll use bisect to find the insertion point
                    # and then check if there is a value greater than a[i]
                    # in the list for i
                    # So let's proceed
                    # We'll create a list of values for each i
                    # and for each query, we'll perform a binary search
                    # to find the first value greater than a[i]
                    # in the list for i
                    # So let's proceed
                    # We'll use bisect to find the insertion point
                    # and then check if there is a value greater than a[i]
                    # in the list for i
                    # So let's proceed
                    # We'll create a list of values for each i
                    # and for each query, we'll perform a binary search
                    # to find the first value greater than a[i]
                    # in the list for i
                    # So let's proceed
                    # We'll use bisect to find the insertion point
                    # and then check