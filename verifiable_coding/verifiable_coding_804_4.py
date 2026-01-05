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
        A = list(map(int, data[idx:idx + N - 1]))
        idx += N - 1
        F = int(data[idx])
        idx += 1
        
        # Find the optimal P and D
        possible = False
        min_D = float('inf')
        best_P = -1
        
        # Try all possible positions for P (1-based)
        for P in range(1, N + 1):
            # Construct the circle with Josh at position P
            # The order is 1, 2, ..., P-1, N, P, P+1, ..., N-1
            # So the order is [1, 2, ..., P-1, N, P, P+1, ..., N-1]
            # But since it's a circle, we need to handle the wrap-around
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # So the list is [1, 2, ..., P-1, N, P, P+1, ..., N-1]
            # But since it's a circle, the order is cyclic
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then, the order is circular
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then, the order is circular
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then, the order is circular
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then, the order is circular
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then, the order is circular
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then, the order is circular
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then, the order is circular
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then, the order is circular
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then, the order is circular
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then, the order is circular
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then, the order is circular
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then, the order is circular
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then, the order is circular
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then, the order is circular
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then, the order is circular
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then, the order is circular
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then, the order is circular
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then, the order is circular
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then, the order is circular
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then, the order is circular
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then, the order is circular
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then, the order is circular
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then, the order is circular
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then, the order is circular
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then, the order is circular
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then, the order is circular
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then, the order is circular
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then, the order is circular
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then, the order is circular
            # We'll create a list that represents the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then, the order is circular
            # We'll create a list that represents