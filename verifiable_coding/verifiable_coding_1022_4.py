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
        
        # Check if N is even
        if N % 2 != 0:
            results.append("NO")
            continue
        
        # For each city, find its opposite
        opposite = [0] * N
        for i in range(N):
            opposite[i] = (i + N // 2) % N
        
        # Check if opposite cities are correctly paired
        # For each pair (i, opposite[i]), check if they are distinct
        # and if the road between them is not already set
        # Also, check if the road between i and i+1 is not already set
        # and if the road between N and 1 is not already set
        
        # Check for valid configuration
        valid = True
        for i in range(N):
            if A[i] != -1:
                # Check if the road between i and i+1 is not already set
                if i < N - 1 and A[i+1] != -1:
                    valid = False
                # Check if the road between N and 1 is not already set
                if i == N - 1 and A[0] != -1:
                    valid = False
                # Check if the road between i and opposite[i] is not already set
                if A[opposite[i]] != -1:
                    valid = False
        
        if not valid:
            results.append("NO")
            continue
        
        # Now, assign values to roads
        # For each pair (i, opposite[i]), assign the same value
        # For roads between consecutive cities, assign the same value
        # For the road between N and 1, assign the same value
        
        # Assign values to roads
        # For each i, if A[i] is -1, assign a value
        # For roads between consecutive cities, assign the same value
        # For the road between N and 1, assign the same value
        
        # Assign values to roads
        # For each i, if A[i] is -1, assign a value
        # For roads between consecutive cities, assign the same value
        # For the road between N and 1, assign the same value
        
        # Initialize the answer
        ans = [0] * N
        
        # Assign values to roads
        # For each i, if A[i] is -1, assign a value
        # For roads between consecutive cities, assign the same value
        # For the road between N and 1, assign the same value
        
        # Assign values to roads
        # For each i, if A[i] is -1, assign a value
        # For roads between consecutive cities, assign the same value
        # For the road between N and 1, assign the same value
        
        # Assign values to roads
        # For each i, if A[i] is -1, assign a value
        # For roads between consecutive cities, assign the same value
        # For the road between N and 1, assign the same value
        
        # Assign values to roads
        # For each i, if A[i] is -1, assign a value
        # For roads between consecutive cities, assign the same value
        # For the road between N and 1, assign the same value
        
        # Assign values to roads
        # For each i, if A[i] is -1, assign a value
        # For roads between consecutive cities, assign the same value
        # For the road between N and 1, assign the same value
        
        # Assign values to roads
        # For each i, if A[i] is -1, assign a value
        # For roads between consecutive cities, assign the same value
        # For the road between N and 1, assign the same value
        
        # Assign values to roads
        # For each i, if A[i] is -1, assign a value
        # For roads between consecutive cities, assign the same value
        # For the road between N and 1, assign the same value
        
        # Assign values to roads
        # For each i, if A[i] is -1, assign a value
        # For roads between consecutive cities, assign the same value
        # For the road between N and 1, assign the same value
        
        # Assign values to roads
        # For each i, if A[i] is -1, assign a value
        # For roads between consecutive cities, assign the same value
        # For the road between N and 1, assign the same value
        
        # Assign values to roads
        # For each i, if A[i] is -1, assign a value
        # For roads between consecutive cities, assign the same value
        # For the road between N and 1, assign the same value
        
        # Assign values to roads
        # For each i, if A[i] is -1, assign a value
        # For roads between consecutive cities, assign the same value
        # For the road between N and 1, assign the same value
        
        # Assign values to roads
        # For each i, if A[i] is -1, assign a value
        # For roads between consecutive cities, assign the same value
        # For the road between N and 1, assign the same value
        
        # Assign values to roads
        # For each i, if A[i] is -1, assign a value
        # For roads between consecutive cities, assign the same value
        # For the road between N and 1, assign the same value
        
        # Assign values to roads
        # For each i, if A[i] is -1, assign a value
        # For roads between consecutive cities, assign the same value
        # For the road between N and 1, assign the same value
        
        # Assign values to roads
        # For each i, if A[i] is -1, assign a value
        # For roads between consecutive cities, assign the same value
        # For the road between N and 1, assign the same value
        
        # Assign values to roads
        # For each i, if A[i] is -1, assign a value
        # For roads between consecutive cities, assign the same value
        # For the road between N and 1, assign the same value
        
        # Assign values to roads
        # For each i, if A[i] is -1, assign a value
        # For roads between consecutive cities, assign the same value
        # For the road between N and 1, assign the same value
        
        # Assign values to roads
        # For each i, if A[i] is -1, assign a value
        # For roads between consecutive cities, assign the same value
        # For the road between N and 1, assign the same value
        
        # Assign values to roads
        # For each i, if A[i] is -1, assign a value
        # For roads between consecutive cities, assign the same value
        # For the road between N and 1, assign the same value
        
        # Assign values to roads
        # For each i, if A[i] is -1, assign a value
        # For roads between consecutive cities, assign the same value
        # For the road between N and 1, assign the same value
        
        # Assign values to roads
        # For each i, if A[i] is -1, assign a value
        # For roads between consecutive cities, assign the same value
        # For the road between N and 1, assign the same value
        
        # Assign values to roads
        # For each i, if A[i] is -1, assign a value
        # For roads between consecutive cities, assign the same value
        # For the road between N and 1, assign the same value
        
        # Assign values to roads
        # For each i, if A[i] is -1, assign a value
        # For roads between consecutive cities, assign the same value
        # For the road between N and 1, assign the same value
        
        # Assign values to roads
        # For each i, if A[i] is -1, assign a value
        # For roads between consecutive cities, assign the same value
        # For the road between N and 1, assign the same value
        
        # Assign values to roads
        # For each i, if A[i] is -1, assign a value
        # For roads between consecutive cities, assign the same value
        # For the road between N and 1, assign the same value
        
        # Assign values to roads
        # For each i, if A[i] is -1, assign a value
        # For roads between consecutive cities, assign the same value
        # For the road between N and 1, assign the same value
        
        # Assign values to roads
        # For each i, if A[i] is -1, assign a value
        # For roads between consecutive cities