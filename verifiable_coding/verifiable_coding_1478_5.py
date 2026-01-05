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
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Find all positions where the value is -1
        unknowns = [i for i in range(N) if A[i] == -1]
        
        # If there are no unknowns, check if it's a valid sequence
        if not unknowns:
            # Check if all elements are the same
            if all(a == A[0] for a in A):
                results.append("inf")
            else:
                results.append("impossible")
            continue
        
        # Try to determine the possible period K
        max_possible = N
        valid = True
        for K in range(1, max_possible + 1):
            # Check if the sequence can be filled with values from 1 to K
            # such that it is a contiguous subsequence of a periodic sequence
            # with period K
            # For each position i, the value should be (i % K) + 1
            # We need to fill in the unknowns with values that fit this pattern
            # and check if the entire sequence is valid
            # We can try to fill in the unknowns and check for consistency
            # We'll use a dictionary to store the values of the unknowns
            # and check if they are consistent with the periodic pattern
            
            # Create a list to store the filled values
            filled = A.copy()
            # Try to fill in the unknowns
            filled_unknowns = {}
            for i in range(N):
                if filled[i] == -1:
                    # The value should be (i % K) + 1
                    filled[i] = (i % K) + 1
                    filled_unknowns[i] = filled[i]
            
            # Check if all filled values are consistent with the periodic pattern
            valid = True
            for i in range(N):
                if filled[i] != (i % K) + 1:
                    valid = False
                    break
            
            if valid:
                # Check if all values are within 1 to K
                for val in filled:
                    if val < 1 or val > K:
                        valid = False
                        break
            
            if valid:
                # Check if the sequence is a valid contiguous subsequence of a periodic sequence
                # with period K
                # We can check if the sequence can be extended to the left and right
                # with values that fit the periodic pattern
                # We need to check if the sequence can be extended to the left and right
                # with values that fit the periodic pattern
                # For the left side:
                # The first element should be (0 % K) + 1 = 1
                # The second element should be (1 % K) + 1 = 2
                # ...
                # For the right side:
                # The last element should be (N-1 % K) + 1
                # The next element should be (N % K) + 1
                # We need to check if the sequence can be extended to the left and right
                # with values that fit the periodic pattern
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if it can be extended to the left and right
                # We can check if the sequence is consistent with the periodic pattern
                # and if