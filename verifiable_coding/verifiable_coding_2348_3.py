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
    pos = x
    
    # For each hotel, precompute the farthest hotel it can reach in one day
    # Using binary search
    farthest = [0] * N
    for i in range(N):
        # Find the farthest hotel that is within L distance from x[i]
        # We can use binary search to find the maximum j where x[j] <= x[i] + L
        # Since the array is sorted, we can use bisect_right
        max_pos = x[i] + L
        j = bisect.bisect_right(x, max_pos) - 1
        farthest[i] = j
    
    # Precompute for each hotel, the next hotel it can reach in one day
    # This will help in building the graph
    next_hotel = [0] * N
    for i in range(N):
        next_hotel[i] = farthest[i]
    
    # Precompute for each hotel, the farthest hotel it can reach in one day
    # This is already computed in 'farthest'
    
    # Build a graph where each node points to the farthest hotel it can reach in one day
    # Then, for each query, perform a BFS or binary search to find the minimum number of days
    
    # Since the graph is a DAG (each node points to a higher index), we can use binary search
    # for each query, we can binary search the minimum number of days needed
    
    # Precompute the farthest hotel for each hotel
    # We can use binary search for each query to find the minimum number of days
    
    # For each query (a, b), we need to find the minimum number of days to go from a to b
    # We can use binary search on the number of days
    
    # Precompute for each hotel, the farthest hotel it can reach in one day
    # This is already computed in 'farthest'
    
    # For each query, perform a binary search on the number of days
    # The minimum number of days is the smallest k such that there exists a path from a to b in k days
    
    # To do this efficiently, we can use binary search on k and check if it's possible to reach b from a in k days
    
    # For each query, perform a binary search on k
    # The maximum possible k is N (if you have to go through all hotels)
    
    # Precompute for each hotel, the farthest hotel it can reach in one day
    # This is already computed in 'farthest'
    
    # Now, for each query (a, b), we perform a binary search on the number of days
    # The answer is the minimum k such that there exists a path from a to b in k days
    
    # To check if it's possible to reach b from a in k days, we can use a greedy approach:
    # Start at a, and in each day, move as far as possible (to the farthest hotel reachable in one day)
    # Repeat this until we reach or pass b
    
    # So, for a given k, we can simulate this process and check if we can reach b in k days
    
    # However, this would be too slow for large Q and N
    
    # So, we can precompute for each hotel, the farthest hotel it can reach in one day
    # Then, for each query, we can simulate the process of moving as far as possible each day
    
    # This is O(Q * log N) time, which is acceptable for Q up to 1e5
    
    # So, for each query (a, b), we simulate the process:
    # Start at a, and in each day, move to the farthest hotel possible
    # Count the number of days until we reach or pass b
    
    # This is O(Q * log N) time
    
    # Now, implement this logic
    
    results = []
    
    for a, b in queries:
        current = a
        days = 0
        while current != b:
            # Move as far as possible in one day
            current = farthest[current]
            days += 1
            # If we have passed b, break
            if current > b:
                break
        results.append(days)
    
    for res in results:
        print(res)
    
if __name__ == '__main__':
    solve()