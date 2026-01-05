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
        arr = list(s)
        # Track which positions are blocked (isolated)
        blocked = [False] * (N + 2)  # 1-based indexing
        
        for p in P:
            blocked[p] = True
        
        # Simulate the infection process
        for day in range(D):
            # Create a copy of the current state to avoid overwriting
            new_arr = arr.copy()
            for i in range(1, N + 1):
                if arr[i - 1] == '1' and not blocked[i]:
                    if i + 1 <= N and not blocked[i + 1] and new_arr[i] == '0':
                        new_arr[i] = '1'
                if arr[i] == '1' and not blocked[i]:
                    if i - 1 >= 1 and not blocked[i - 1] and new_arr[i - 1] == '0':
                        new_arr[i - 1] = '1'
            arr = new_arr
        
        # Count the number of '1's
        results.append(str(arr.count('1')))
    
    print('\n'.join(results))