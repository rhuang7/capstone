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
        n, m, k = map(int, data[idx:idx+3])
        idx += 3
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Precompute sorted array
        sorted_a = sorted(a)
        
        # The element you will take is the (m-1)th element in the remaining array
        # After controlling k people, you can choose the best possible element
        # that is guaranteed to be at least x, no matter what the others do
        
        # The maximum x is the (n - k - (m - 1))th element in the sorted array
        # because you can control k people, so you can eliminate k elements
        # and you are the (m-1)th person to take an element
        # So the x is the (n - k - (m - 1))th element in the sorted array
        # but we have to make sure it's not negative
        pos = n - k - (m - 1)
        if pos < 0:
            x = 0
        else:
            x = sorted_a[pos]
        results.append(str(x))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()