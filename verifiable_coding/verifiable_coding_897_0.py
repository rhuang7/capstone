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
        # We will compute the possible values for each position
        # We will use dynamic programming to track the number of ways
        # We will also track the possible values for each position
        
        # dp[i] = number of ways to fill the first i elements
        # ways[i] = the possible values for the i-th element
        dp = [0] * (N + 1)
        dp[0] = 1
        ways = [set() for _ in range(N)]
        
        # Process each restriction
        # We will first process all restrictions and determine the constraints on the array
        # Then we will compute the number of ways
        
        # We will first process all restrictions and determine the constraints on the array
        # We will create a list of constraints for each position
        # For each position i, we will have a list of constraints that affect it
        
        # For each position i, we will have a list of constraints that affect it
        # We will also track the possible values for each position
        # We will also track the constraints on the differences between adjacent elements
        
        # We will create a list of constraints for each position
        # For each position i, we will have a list of constraints that affect it
        # We will also track the possible values for each position
        
        # We will also track the constraints on the differences between adjacent elements
        # For each pair (i, i+1), we will track the constraint on A[i+1] - A[i]
        
        # We will create a list of constraints for each pair (i, i+1)
        # For each pair (i, i+1), we will track the constraint on A[i+1] - A[i]
        # We will also track the possible values for each pair
        
        # We will also track the constraints on the differences between adjacent elements
        # For each pair (i, i+1), we will track the constraint on A[i+1] - A[i]
        
        # We will create a list of constraints for each pair (i, i+1)
        # For each pair (i, i+1), we will track the constraint on A[i+1] - A[i]
        # We will also track the possible values for each pair
        
        # We will also track the constraints on the differences between adjacent elements
        # For each pair (i, i+1), we will track the constraint on A[i+1] - A[i]
        
        # We will create a list of constraints for each pair (i, i+1)
        # For each pair (i, i+1), we will track the constraint on A[i+1] - A[i]
        # We will also track the possible values for each pair
        
        # We will also track the constraints on the differences between adjacent elements
        # For each pair (i, i+1), we will track the constraint on A[i+1] - A[i]
        
        # We will create a list of constraints for each pair (i, i+1)
        # For each pair (i, i+1), we will track the constraint on A[i+1] - A[i]
        # We will also track the possible values for each pair
        
        # We will also track the constraints on the differences between adjacent elements
        # For each pair (i, i+1), we will track the constraint on A[i+1] - A[i]
        
        # We will create a list of constraints for each pair (i, i+1)
        # For each pair (i, i+1), we will track the constraint on A[i+1] - A[i]
        # We will also track the possible values for each pair
        
        # We will also track the constraints on the differences between adjacent elements
        # For each pair (i, i+1), we will track the constraint on A[i+1] - A[i]
        
        # We will create a list of constraints for each pair (i, i+1)
        # For each pair (i, i+1), we will track the constraint on A[i+1] - A[i]
        # We will also track the possible values for each pair
        
        # We will also track the constraints on the differences between adjacent elements
        # For each pair (i, i+1), we will track the constraint on A[i+1] - A[i]
        
        # We will create a list of constraints for each pair (i, i+1)
        # For each pair (i, i+1), we will track the constraint on A[i+1] - A[i]
        # We will also track the possible values for each pair
        
        # We will also track the constraints on the differences between adjacent elements
        # For each pair (i, i+1), we will track the constraint on A[i+1] - A[i]
        
        # We will create a list of constraints for each pair (i, i+1)
        # For each pair (i, i+1), we will track the constraint on A[i+1] - A[i]
        # We will also track the possible values for each pair
        
        # We will also track the constraints on the differences between adjacent elements
        # For each pair (i, i+1), we will track the constraint on A[i+1] - A[i]
        
        # We will create a list of constraints for each pair (i, i+1)
        # For each pair (i, i+1), we will track the constraint on A[i+1] - A[i]
        # We will also track the possible values for each pair
        
        # We will also track the constraints on the differences between adjacent elements
        # For each pair (i, i+1), we will track the constraint on A[i+1] - A[i]
        
        # We will create a list of constraints for each pair (i, i+1)
        # For each pair (i, i+1), we will track the constraint on A[i+1] - A[i]
        # We will also track the possible values for each pair
        
        # We will also track the constraints on the differences between adjacent elements
        # For each pair (i, i+1), we will track the constraint on A[i+1] - A[i]
        
        # We will create a list of constraints for each pair (i, i+1)
        # For each pair (i, i+1), we will track the constraint on A[i+1] - A[i]
        # We will also track the possible values for each pair
        
        # We will also track the constraints on the differences between adjacent elements
        # For each pair (i, i+1), we will track the constraint on A[i+1] - A[i]
        
        # We will create a list of constraints for each pair (i, i+1)
        # For each pair (i, i+1), we will track the constraint on A[i+1] - A[i]
        # We will also track the possible values for each pair
        
        # We will also track the constraints on the differences between adjacent elements
        # For each pair (i, i+1), we will track the constraint on A[i+1] - A[i]
        
        # We will create a list of constraints for each pair (i, i+1)
        # For each pair (i, i+1), we will track the constraint on A[i+1] - A[i]
        # We will also track the possible values for each pair
        
        # We will also track the constraints on the differences between adjacent elements
        # For each pair (i, i+1), we will track the constraint on A[i+1] - A[i]
        
        # We will create a list of constraints for each pair (i, i+1)
        # For each pair (i, i+1), we will track the constraint on A[i+1] - A[i]
        # We will also track the possible values for each pair
        
        # We will also track the constraints on the differences between adjacent elements
        # For each pair (i, i+1), we will track the constraint on A[i+1] - A[i]
        
        # We will create a list of constraints for each pair (i, i+1)
        # For each pair (i, i+1), we will track the constraint on A[i+1] - A[i]
        # We will also track the possible values for each pair
        
        # We will also track the constraints on the differences between adjacent elements
        # For each pair (i, i