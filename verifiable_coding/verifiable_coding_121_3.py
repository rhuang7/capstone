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
        
        # The optimal way is to have one class of size 1 and the other of size 2n-1
        # Or vice versa. The median of the class of size 1 is the element itself.
        # The median of the class of size 2n-1 is the nth element in the sorted array.
        # So the minimal difference is the difference between a[n-1] and a[n]
        # Because the class of size 1 can be either a[n-1] or a[n], and the other class will have median a[n] or a[n-1]
        # So the minimal difference is |a[n] - a[n-1]|
        min_diff = abs(a[n] - a[n-1])
        results.append(str(min_diff))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()