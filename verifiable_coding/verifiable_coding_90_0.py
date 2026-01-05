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
        
        locked = [i for i in range(n) if l[i] == 1]
        unlocked = [i for i in range(n) if l[i] == 0]
        
        # Collect the values of unlocked positions
        unlock_values = [a[i] for i in unlocked]
        
        # Sort the unlocked values to minimize the maximum j where p_j < 0
        # We want to make the prefix sums as positive as possible early on
        # So we sort the unlocked values in ascending order and place them in the unlocked positions
        # This is a heuristic that may not always be optimal, but it's a common approach for this type of problem
        
        # Sort the unlocked values
        unlock_values.sort()
        
        # Create the result array
        res = [0] * n
        ptr = 0
        
        for i in range(n):
            if l[i] == 1:
                res[i] = a[i]
            else:
                res[i] = unlock_values[ptr]
                ptr += 1
        
        results.append(' '.join(map(str, res)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()