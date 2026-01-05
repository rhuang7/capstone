import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        l = list(map(int, data[idx:idx + n]))
        idx += n
        
        unlocked = []
        locked = []
        for i in range(n):
            if l[i] == 0:
                unlocked.append(a[i])
            else:
                locked.append(a[i])
        
        # Sort unlocked elements to minimize the maximum j where p_j < 0
        unlocked.sort()
        
        # Prepare the result array
        res = []
        unlock_idx = 0
        for i in range(n):
            if l[i] == 1:
                res.append(locked.pop(0))
            else:
                res.append(unlocked[unlock_idx])
                unlock_idx += 1
        
        results.append(' '.join(map(str, res)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()