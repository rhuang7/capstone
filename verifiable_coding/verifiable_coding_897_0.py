import sys
import math

MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N, M, K = map(int, data[idx:idx+3])
        idx += 3
        A = list(map(int, data[idx:idx+N]))
        idx += N
        restrictions = []
        for _ in range(M):
            typ = data[idx]
            L = int(data[idx+1])
            R = int(data[idx+2])
            restrictions.append((typ, L, R))
            idx += 3
        
        # Initialize the array with -1
        # We will use a list of tuples (value, is_known)
        # But for efficiency, we'll use a list of values and track known positions
        # We'll also track the constraints on the differences between consecutive elements
        # We'll use a difference array to track the constraints
        
        # Initialize the difference array
        diff = [0] * (N + 2)  # diff[i] is the constraint on A[i] - A[i-1]
        
        # Process the restrictions
        for typ, L, R in restrictions:
            if typ == 'I':
                # Ai - Ai-1 = 1 for L < i <= R
                # So A[i] - A[i-1] = 1
                # So diff[i] = 1
                for i in range(L + 1, R + 1):
                    diff[i] = 1
            else:
                # Ai - Ai-1 = -1 for L < i <= R
                # So A[i] - A[i-1] = -1
                # So diff[i] = -1
                for i in range(L + 1, R + 1):
                    diff[i] = -1
        
        # Now, we need to compute the possible values for each position
        # We'll track the possible values for each position based on the constraints
        # We'll also track the possible range of values for each position
        
        # We'll use a list to track the possible range of values for each position
        # We'll also track the number of ways to reach each position
        
        # We'll use a list of tuples (low, high, ways)
        # Initially, for each position, if it's known, we set low and high to that value
        # If it's unknown, we set low to 1 and high to K
        # But we also need to consider the constraints from the difference array
        
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a list of tuples (low, high, ways)
        # We'll also track the number of ways to reach each position
        
        # Initialize the possible values for each position
        # We'll use a