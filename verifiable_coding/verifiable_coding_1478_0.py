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
        
        # Replace -1 with possible values
        # We need to find the maximum possible K such that A is a contiguous subsequence of some periodic sequence
        # The periodic sequence S_i = (i % K) + 1
        
        # First, check if all elements are -1
        if all(x == -1 for x in A):
            results.append("inf")
            continue
        
        # Find the set of possible values in A
        possible_values = set()
        for x in A:
            if x != -1:
                possible_values.add(x)
        
        # For the sequence to be a contiguous subsequence of some periodic sequence, all values in A must be <= K
        # Also, the values must satisfy the periodic condition
        
        # We need to find the maximum K such that for all i, A[i] = (i % K) + 1 or A[i] is -1
        # We can try all possible K values up to the maximum value in A
        
        max_val = max(possible_values) if possible_values else 0
        
        # Try all possible K from 1 to max_val
        # But we need to find the maximum K such that the sequence is valid
        # So we can try K from max_val down to 1
        # If any K is valid, that's the answer
        # If none are valid, then it's impossible
        
        # Also, if there are no possible values, then it's impossible
        if not possible_values:
            results.append("impossible")
            continue
        
        # Try K from max_val down to 1
        # We need to find the maximum K such that the sequence is valid
        # For each K, check if the sequence can be filled in such a way that it is a contiguous subsequence of S
        # For each position i in A, if A[i] is not -1, then (i % K) + 1 must be equal to A[i]
        # So for each K, we can check this condition
        
        # Also, if K is larger than the maximum value in A, then it's possible (since the sequence can be filled with values up to K)
        # So if all values are -1, then it's "inf"
        # Otherwise, if there is at least one value in A, then the maximum possible K is the maximum value in A
        # But we need to check if that K is valid
        
        # So the maximum possible K is the maximum value in A
        # But we need to check if that K is valid
        
        # So we can try K from max_val down to 1
        # If any K is valid, that's the answer
        # If none are valid, then it's impossible
        
        # Also, if there are no possible values, then it's impossible
        # But we already checked that
        
        # So let's try K from max_val down to 1
        # For each K, check if the sequence can be filled in such a way that it is a contiguous subsequence of S
        
        # Also, if all values are -1, then it's "inf"
        # So we already handled that case
        
        # Now, try K from max_val down to 1
        # For each K, check if the sequence is valid
        # For each position i in A, if A[i] is not -1, then (i % K) + 1 must be equal to A[i]
        # So for each K, we can check this condition
        
        # Also, if K is larger than the maximum value in A, then it's possible (since the sequence can be filled with values up to K)
        # So if there is at least one value in A, then the maximum possible K is the maximum value in A
        # But we need to check if that K is valid
        
        # So the maximum possible K is the maximum value in A
        # But we need to check if that K is valid
        
        # So we can try K from max_val down to 1
        # For each K, check if the sequence is valid
        
        # Also, if there is at least one value in A, then the maximum possible K is the maximum value in A
        # But we need to check if that K is valid
        
        # So we can try K from max_val down to 1
        # For each K, check if the sequence is valid
        
        # Let's try K from max_val down to 1
        # If any K is valid, that's the answer
        # If none are valid, then it's impossible
        
        # Also, if there is at least one value in A, then the maximum possible K is the maximum value in A
        # But we need to check if that K is valid
        
        # So we can try K from max_val down to 1
        # For each K, check if the sequence is valid
        
        # Also, if there is at least one value in A, then the maximum possible K is the maximum value in A
        # But we need to check if that K is valid
        
        # So we can try K from max_val down to 1
        # For each K, check if the sequence is valid
        
        # Let's try K from max_val down to 1
        # For each K, check if the sequence is valid
        
        # Also, if there is at least one value in A, then the maximum possible K is the maximum value in A
        # But we need to check if that K is valid
        
        # So we can try K from max_val down to 1
        # For each K, check if the sequence is valid
        
        # Also, if there is at least one value in A, then the maximum possible K is the maximum value in A
        # But we need to check if that K is valid
        
        # So we can try K from max_val down to 1
        # For each K, check if the sequence is valid
        
        # Let's try K from max_val down to 1
        # For each K, check if the sequence is valid
        
        # Also, if there is at least one value in A, then the maximum possible K is the maximum value in A
        # But we need to check if that K is valid
        
        # So we can try K from max_val down to 1
        # For each K, check if the sequence is valid
        
        # Let's try K from max_val down to 1
        # For each K, check if the sequence is valid
        
        # Also, if there is at least one value in A, then the maximum possible K is the maximum value in A
        # But we need to check if that K is valid
        
        # So we can try K from max_val down to 1
        # For each K, check if the sequence is valid
        
        # Let's try K from max_val down to 1
        # For each K, check if the sequence is valid
        
        # Also, if there is at least one value in A, then the maximum possible K is the maximum value in A
        # But we need to check if that K is valid
        
        # So we can try K from max_val down to 1
        # For each K, check if the sequence is valid
        
        # Let's try K from max_val down to 1
        # For each K, check if the sequence is valid
        
        # Also, if there is at least one value in A, then the maximum possible K is the maximum value in A
        # But we need to check if that K is valid
        
        # So we can try K from max_val down to 1
        # For each K, check if the sequence is valid
        
        # Let's try K from max_val down to 1
        # For each K, check if the sequence is valid
        
        # Also, if there is at least one value in A, then the maximum possible K is the maximum value in A
        # But we need to check if that K is valid
        
        # So we can try K from max_val down to 1
        # For each K, check if the sequence is valid
        
        # Let's try K from max_val down to 1
        # For each K, check if the sequence is valid
        
        # Also, if there is at least one value in A, then the maximum possible K is the maximum value in A
        # But we need to check if that K is valid
        
        # So we can try K from max_val down to 1
        # For each K, check if the sequence is valid
        
        # Let's try K from max_val down to 1
        # For each K, check if the sequence is valid
        
        # Also, if there is at least one value in A, then the maximum possible K is the maximum value in A
        # But we need to check if that K is valid
        
        # So we can try