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
        # Track which positions are isolated
        isolated = [False] * (N + 2)  # 1-based indexing
        
        for day in range(D):
            p = P[day]
            isolated[p] = True
        
        # Simulate the spread of infection
        for day in range(D):
            new_infected = [False] * N
            for i in range(N):
                if infected[i]:
                    if i + 1 < N and not isolated[i + 1]:
                        new_infected[i + 1] = True
                    if i - 1 >= 0 and not isolated[i - 1]:
                        new_infected[i - 1] = True
            for i in range(N):
                if new_infected[i]:
                    infected[i] = True
        
        results.append(sum(infected))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()