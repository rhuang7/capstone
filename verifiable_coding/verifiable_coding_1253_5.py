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
        s_list = list(s)
        # Track which positions are blocked (isolated)
        blocked = [False] * (N + 2)  # 1-based indexing, extra for safety
        
        for p in P:
            blocked[p] = True
        
        # Simulate the spread of infection
        for day in range(D):
            # Create a new list to store the next state
            new_s = s_list[:]
            # Iterate from left to right
            for i in range(1, N + 1):
                if s_list[i - 1] == '1':
                    # Check right neighbor
                    if i + 1 <= N and not blocked[i + 1] and new_s[i] == '0':
                        new_s[i] = '1'
                if s_list[i] == '1':
                    # Check left neighbor
                    if i - 1 >= 1 and not blocked[i - 1] and new_s[i - 1] == '0':
                        new_s[i - 1] = '1'
            s_list = new_s
        
        # Count the number of '1's
        count = s_list.count('1')
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()