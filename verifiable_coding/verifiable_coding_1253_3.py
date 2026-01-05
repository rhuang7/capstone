import sys

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
        s = data[idx]
        idx += 1
        D = int(data[idx])
        idx += 1
        P = list(map(int, data[idx:idx+D]))
        idx += D
        
        # Convert string to list for easier manipulation
        infected = list(map(int, s))
        # Track blocked positions
        blocked = [False] * (N + 2)  # 1-based indexing
        
        for day in range(D):
            p = P[day]
            # Block p-1 from p
            blocked[p-1] = True
            blocked[p] = True
        
        # Simulate the spread of infection
        # We'll use a BFS approach to track when each position gets infected
        # We'll use a queue to process the spread
        # We'll also track the earliest day each position gets infected
        # Initially, all 1s are infected on day 0
        # We'll also track the blocked positions
        # We'll use a list to track the earliest day each position is infected
        # Initialize the earliest_day array
        earliest_day = [-1] * N
        queue = []
        
        for i in range(N):
            if infected[i] == 1:
                earliest_day[i] = 0
                queue.append(i)
        
        # Directions: left and right
        directions = [-1, 1]
        
        while queue:
            pos = queue.pop(0)
            for d in directions:
                new_pos = pos + d
                if 0 <= new_pos < N:
                    if not blocked[new_pos] and earliest_day[new_pos] == -1:
                        earliest_day[new_pos] = earliest_day[pos] + 1
                        queue.append(new_pos)
        
        # Count the number of infected people
        count = sum(1 for day in earliest_day if day != -1)
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()