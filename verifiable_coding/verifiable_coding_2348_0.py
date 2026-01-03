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
    # For each hotel, precompute the farthest hotel reachable in one day
    # Using binary search
    next_pos = [0] * N
    for i in range(N-1):
        # Find the farthest hotel j such that x[j] - x[i] <= L
        # Use binary search
        j = bisect.bisect_right(pos, x[i] + L) - 1
        next_pos[i] = j
    
    # Precompute for each hotel, the farthest hotel reachable in one day
    # Then, use binary lifting to answer queries in O(log N) time
    # Precompute log2(N) levels
    log_max = 20  # since N is up to 1e5, log2(1e5) is about 17
    up = [[0]*N for _ in range(log_max)]
    
    # Initialize the first level
    for i in range(N):
        up[0][i] = next_pos[i]
    
    # Fill the rest levels
    for k in range(1, log_max):
        for i in range(N):
            up[k][i] = up[k-1][up[k-1][i]]
    
    # Function to find the minimum number of days
    def get_days(a, b):
        if a > b:
            # Need to go backwards
            # Find the farthest hotel reachable in one day from b towards a
            # So reverse the array and do the same logic
            # But for simplicity, we can just swap a and b and call the same function
            return get_days(b, a)
        
        days = 0
        current = a
        while current != b:
            days += 1
            # Find the farthest hotel reachable in one day from current
            current = up[0][current]
            # If current is still not b, check higher levels
            # Find the highest level where the jump is still within the range
            # This is a bit more complex, but we can use binary search
            # For simplicity, we'll just keep jumping to the farthest possible
            # and count the days
            # This is not optimal, but for the given constraints, it's acceptable
            # for the problem's time constraints
            # However, for the full solution, we need to use binary lifting properly
            # So let's implement it properly
            # Find the highest level k such that up[k][current] != current
            # and up[k][current] is not beyond b
            # This is a bit more complex, but we can do it with binary search
            # For the purpose of this problem, we'll use a different approach
            # We'll use binary lifting to find the minimum number of days
            # by jumping as far as possible each time
            # So we'll use a binary lifting approach
            # Let's implement the binary lifting properly
            # Let's find the maximum k such that up[k][current] is not beyond b
            # and then jump to up[k][current]
            # This is the standard binary lifting approach
            # So we'll implement this
            # Find the maximum k such that up[k][current] is not beyond b
            # and up[k][current] is not current
            k = 0
            while (1 << (k+1)) <= log_max and up[k][current] != current and up[k][current] <= b:
                k += 1
            current = up[k][current]
        return days
    
    # Process queries
    for a, b in queries:
        print(get_days(a, b))

if __name__ == '__main__':
    solve()