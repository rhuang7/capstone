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
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Sort the array
        a.sort()
        
        # The maximum possible difference is achieved by taking the largest elements
        # and moving all their water to one barrel
        # We can do this in k steps: take the k largest elements and pour all their water into the largest one
        # The maximum difference is the sum of the k largest elements minus the smallest element (or zero if all are zero)
        
        # If all elements are zero, the difference is zero
        if a[-1] == 0:
            results.append('0')
            continue
        
        # Take the k largest elements and sum them
        total = sum(a[-k:])
        
        # The minimum possible value is the smallest element (or zero if all are zero)
        min_val = a[0] if a[0] != 0 else 0
        
        # The maximum difference is total - min_val
        results.append(str(total - min_val))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()