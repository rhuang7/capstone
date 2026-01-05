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
        unlock_values = [a[i] for i in unlocked]
        
        # Sort the unlocked values to minimize the maximum j where prefix sum is negative
        # We want to place the smallest values first to keep prefix sums as low as possible
        unlock_values.sort()
        
        # Prepare the result array
        result = [0] * n
        for i in range(n):
            if l[i] == 1:
                result[i] = a[i]
            else:
                result[i] = unlock_values.pop(0)
        
        results.append(' '.join(map(str, result)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()