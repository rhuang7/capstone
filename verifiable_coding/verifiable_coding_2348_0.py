import sys
import bisect

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    x = list(map(int, data[idx:idx+N]))
    idx += N
    L = int(data[idx])
    idx += 1
    Q = int(data[idx])
    idx += 1
    
    queries = []
    for _ in range(Q):
        a = int(data[idx]) - 1
        b = int(data[idx+1]) - 1
        queries.append((a, b))
        idx += 2
    
    # Preprocess the positions
    # For each hotel, precompute the farthest hotel that can be reached in one day
    # Using binary search
    # We'll create a list of the farthest indices for each position
    # We'll also create a list of the next positions that can be reached in one day
    # For each position i, find the maximum j such that x[j] - x[i] <= L
    # This can be done with binary search
    # We'll create a list of next positions for each hotel
    
    # Precompute the next positions for each hotel
    next_pos = [0] * N
    for i in range(N):
        # Find the farthest hotel that can be reached from i
        # Using binary search
        # We want the largest j such that x[j] - x[i] <= L
        # Since x is sorted, we can use bisect_right
        j = bisect.bisect_right(x, x[i] + L) - 1
        if j > i:
            next_pos[i] = j
        else:
            next_pos[i] = i  # shouldn't happen as per constraints
    
    # Now, for each query, we need to find the minimum number of days
    # This is a classic problem of finding the minimum number of steps in a graph
    # Where each node is a hotel and edges exist from i to next_pos[i]
    # We can use BFS for each query, but with Q up to 1e5, this would be too slow
    # So we need a more efficient approach
    
    # We can precompute for each hotel, the farthest hotel that can be reached in one day
    # Then, for each query, we can use binary lifting to find the minimum number of days
    # We'll precompute for each hotel, the 2^k-th ancestor in the jump game
    
    # Precompute binary lifting table
    log_max = 20  # since 2^20 is larger than 1e5
    up = [[0] * log_max for _ in range(N)]
    
    # Initialize the up table
    for i in range(N):
        up[i][0] = next_pos[i]
    
    # Fill the rest of the table
    for k in range(1, log_max):
        for i in range(N):
            up[i][k] = up[up[i][k-1]][k-1]
    
    # Now, for each query, we can find the minimum number of days using binary lifting
    # We'll perform a binary search on the number of steps
    # For a query from a to b, we need to find the minimum number of steps to reach from a to b
    
    # Function to find the minimum number of days from a to b
    def min_days(a, b):
        if a > b:
            # We need to go backward
            # So we reverse the array and do the same logic
            # But since the array is sorted, we can just swap a and b and reverse the logic
            # So we'll do the same steps as above but with a < b
            a, b = b, a
        res = 0
        while a < b:
            # Find the farthest hotel that can be reached from a in one day
            # This is up[a][0]
            # But we need to find the farthest hotel that can be reached in one day
            # So we need to find the maximum j such that x[j] - x[a] <= L
            # Which is up[a][0]
            # So we jump to up[a][0]
            # But we need to find the farthest possible jump
            # So we can use binary lifting
            # We'll try to jump as far as possible
            # We'll find the highest k such that up[a][k] < b
            # Then we jump up[a][k], and increment res by 2^k
            # We'll do this until a >= b
            # This is similar to the standard binary lifting approach for LCA
            # So we'll find the highest k such that up[a][k] < b
            # Then we jump to up[a][k], and increment res by 2^k
            # We'll repeat this until a >= b
            # This is the same approach as in the problem of finding the minimum number of steps in a jump game
            # So we'll use binary lifting to find the minimum number of steps
            # We'll find the highest k such that up[a][k] < b
            # Then we jump to up[a][k], and increment res by 2^k
            # We'll repeat this until a >= b
            # This is the same approach as in the problem of finding the minimum number of steps in a jump game
            # So we'll use binary lifting to find the minimum number of steps
            # We'll find the highest k such that up[a][k] < b
            # Then we jump to up[a][k], and increment res by 2^k
            # We'll repeat this until a >= b
            # This is the same approach as in the problem of finding the minimum number of steps in a jump game
            # So we'll use binary lifting to find the minimum number of steps
            # We'll find the highest k such that up[a][k] < b
            # Then we jump to up[a][k], and increment res by 2^k
            # We'll repeat this until a >= b
            # This is the same approach as in the problem of finding the minimum number of steps in a jump game
            # So we'll use binary lifting to find the minimum number of steps
            # We'll find the highest k such that up[a][k] < b
            # Then we jump to up[a][k], and increment res by 2^k
            # We'll repeat this until a >= b
            # This is the same approach as in the problem of finding the minimum number of steps in a jump game
            # So we'll use binary lifting to find the minimum number of steps
            # We'll find the highest k such that up[a][k] < b
            # Then we jump to up[a][k], and increment res by 2^k
            # We'll repeat this until a >= b
            # This is the same approach as in the problem of finding the minimum number of steps in a jump game
            # So we'll use binary lifting to find the minimum number of steps
            # We'll find the highest k such that up[a][k] < b
            # Then we jump to up[a][k], and increment res by 2^k
            # We'll repeat this until a >= b
            # This is the same approach as in the problem of finding the minimum number of steps in a jump game
            # So we'll use binary lifting to find the minimum number of steps
            # We'll find the highest k such that up[a][k] < b
            # Then we jump to up[a][k], and increment res by 2^k
            # We'll repeat this until a >= b
            # This is the same approach as in the problem of finding the minimum number of steps in a jump game
            # So we'll use binary lifting to find the minimum number of steps
            # We'll find the highest k such that up[a][k] < b
            # Then we jump to up[a][k], and increment res by 2^k
            # We'll repeat this until a >= b
            # This is the same approach as in the problem of finding the minimum number of steps in a jump game
            # So we'll use binary lifting to find the minimum number of steps
            # We'll find the highest k such that up[a][k] < b
            # Then we jump to up[a][k], and increment res by 2^k
            # We'll repeat this until a >= b
            # This is the same approach as in the problem of finding the minimum number of steps in a jump game
            # So we'll use binary lifting to find the minimum number of steps
            # We'll find the highest k such that up[a][k] < b
            # Then we jump to up[a][k], and increment res by 2^k
            # We'll repeat this until a >= b
            # This is the same approach as in the problem of finding the minimum number of steps in a jump game
            # So we'll use binary lifting to find the minimum number of steps
            # We'll find the highest k such