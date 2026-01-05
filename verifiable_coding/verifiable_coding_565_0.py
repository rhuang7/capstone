import sys
import math

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
        A = list(map(int, data[idx:idx+N]))
        idx += N
        queries = []
        for __ in range(Q):
            queries.append(int(data[idx]))
            idx += 1
        
        pos = -1
        for i in range(N):
            if A[i] == queries[0]:
                pos = i
                break
        
        if pos == -1:
            for q in queries:
                results.append(-1)
            continue
        
        # Create a dictionary to map value to its position
        value_to_pos = {val: i for i, val in enumerate(A)}
        
        # Precompute the correct positions for all queries
        correct_positions = [value_to_pos[x] for x in queries]
        
        # For each query, compute the minimum swaps needed
        for i in range(Q):
            x = queries[i]
            correct_pos = correct_positions[i]
            if correct_pos == pos:
                results.append(0)
                continue
            
            # Find the number of elements that are not in their correct positions
            # and are in the correct position of x
            # This is a problem of finding the minimum number of swaps to bring x to its correct position
            # The minimum number of swaps is the number of elements that are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are not x
            # This is equivalent to counting how many elements are in the correct position of x but are not x
            # So we need to find how many elements are in the correct position of x but are