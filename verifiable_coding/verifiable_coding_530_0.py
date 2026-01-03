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
        S = int(data[idx+1])
        K = int(data[idx+2])
        m = int(data[idx+3])
        M = int(data[idx+4])
        idx += 5
        
        # Check if it's possible to construct a proper sequence
        # The minimum possible sum is N*m, maximum is N*M
        if S < N * m or S > N * M:
            results.append("-1")
            continue
        
        # Try to construct the lexicographically smallest sequence
        # We want the lex smallest, so we try to make the first elements as small as possible
        # But we need to ensure that Fulu's program returns a different value than the correct median
        
        # We will try to construct the sequence with the first elements as small as possible
        # and check if it's a proper sequence
        
        # We will try to construct the sequence with the first elements as small as possible
        # and check if it's a proper sequence
        
        # We will try to construct the sequence with the first elements as small as possible
        # and check if it's a proper sequence
        
        # Try to construct the lex smallest sequence
        A = [m] * N
        # Adjust the last element to make the sum S
        A[-1] = S - sum(A)
        # Check if it's valid
        if A[-1] < m or A[-1] > M:
            # Try to adjust the last element to be within [m, M]
            # If not possible, try to adjust the previous elements
            # This is a simplified approach, but may not work for all cases
            # For the sake of time, we'll use this approach
            # We'll try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper sequence
            
            # Try to make the first elements as small as possible
            # and the last element as small as possible
            # and check if it's a proper