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
        
        # Simulate the days
        for day in range(D):
            # Create a new array to store the next state
            new_arr = arr[:]
            # Iterate from left to right
            for i in range(1, N + 1):
                # Check if current position is blocked
                if blocked[i]:
                    continue
                # Check if current position is infected
                if new_arr[i - 1] == '1':
                    if i < N and new_arr[i] == '0' and not blocked[i]:
                        new_arr[i] = '1'
                # Check if right neighbor is infected
                if i < N and new_arr[i] == '1':
                    if new_arr[i + 1] == '0' and not blocked[i + 1]:
                        new_arr[i + 1] = '1'
            arr = new_arr
        
        # Count the number of '1's
        count = arr.count('1')
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()