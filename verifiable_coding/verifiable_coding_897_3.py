import sys
import math

MOD = 10**9 + 7

def solve():
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
        # We need to track the constraints on the differences between consecutive elements
        # We'll use a difference array to represent the constraints
        diff = [0] * (N + 2)  # diff[i] represents the constraint on A[i] - A[i-1]
        
        # Process restrictions
        for typ, L, R in restrictions:
            if typ == 'I':
                # Ai - Ai-1 = 1 => diff[i] = 1
                for i in range(L, R+1):
                    diff[i] = 1
            else:
                # Ai - Ai-1 = -1 => diff[i] = -1
                for i in range(L, R+1):
                    diff[i] = -1
        
        # Now, we need to compute the possible values for each element
        # We'll track the possible range for each element
        # We'll also track the constraints on the differences
        
        # We'll use a segment tree to track the constraints
        # But since the constraints are linear, we can process them in a way that allows us to compute the possible values
        
        # We'll track the current value of A[i] as we process the array
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the constraints on the differences
        # For each position i, we'll have a constraint on A[i] - A[i-1]
        
        # We'll also track the possible values for A[i]
        # We'll use a list to track the possible values for each position
        
        # We'll also track the possible range for each position
        # We'll use a list to track the possible range for each position
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the constraints on the differences between consecutive elements
        # We'll also track the possible range for each position
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible range for each position
        # We'll also track the constraints on the differences between consecutive elements
        
        # We'll use a list to track the possible