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
        a = list(map(int, data[idx:idx+n]))
        idx += n
        l = list(map(int, data[idx:idx+n]))
        idx += n
        
        locked = []
        unlocked = []
        for i in range(n):
            if l[i] == 1:
                locked.append(a[i])
            else:
                unlocked.append(a[i])
        
        # Sort unlocked elements
        unlocked.sort()
        
        # Prepare the result array
        res = []
        unlocked_ptr = 0
        for i in range(n):
            if l[i] == 1:
                res.append(locked.pop(0))
            else:
                res.append(unlocked[unlocked_ptr])
                unlocked_ptr += 1
        
        results.append(' '.join(map(str, res)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()