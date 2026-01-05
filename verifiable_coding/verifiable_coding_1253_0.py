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
        # Track which positions are blocked (isolated)
        blocked = [False] * (N + 2)  # 1-based indexing
        
        for day in range(D):
            p = P[day]
            # Block p-1 from affecting p
            blocked[p-1] = True
            blocked[p] = True
        
        # Simulate the spread of infection
        # We'll use a BFS approach to track when each position gets infected
        # We'll track the earliest day each position gets infected
        # Initialize with the initial infected positions
        infected_days = [-1] * N
        for i in range(N):
            if infected[i] == 1:
                infected_days[i] = 0
        
        # Use a queue to process the spread
        from collections import deque
        q = deque()
        for i in range(N):
            if infected_days[i] != -1:
                q.append(i)
        
        # Directions: left and right
        directions = [-1, 1]
        
        while q:
            pos = q.popleft()
            for d in directions:
                new_pos = pos + d
                if 0 <= new_pos < N:
                    if infected_days[new_pos] == -1:
                        # Check if the position is not blocked
                        if not blocked[new_pos]:
                            infected_days[new_pos] = infected_days[pos] + 1
                            q.append(new_pos)
        
        # Count the number of infected people
        count = sum(1 for day in infected_days if day != -1)
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()