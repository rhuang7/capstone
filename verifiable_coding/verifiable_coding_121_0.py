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
        a = list(map(int, data[idx:idx + 2 * n]))
        idx += 2 * n
        
        a.sort()
        
        # The optimal way is to have the two classes with sizes 1 and 2n-1, or 3 and 2n-3, etc.
        # The minimal difference is always between the middle elements of the sorted array
        # The minimal difference is between the n-th and (n+1)-th elements in the sorted array
        # Because when you split the sorted array into two parts, the medians will be the middle elements
        # So the minimal difference is a[n] - a[n-1]
        results.append(str(a[n] - a[n-1]))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()