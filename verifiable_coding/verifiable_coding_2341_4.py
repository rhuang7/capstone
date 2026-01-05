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
        
        # Precompute the sorted array
        sorted_a = sorted(a)
        
        # The x we want is the (n - k - (m - 1))th smallest element in the array
        # Because we can control k people, so we can ensure that the remaining (n - k) elements are chosen by others
        # And we are in position m, so we are the (m - 1)th person to choose
        # So the number of elements we can guarantee is (n - k - (m - 1))
        # But we need to make sure it's not negative
        pos = n - k - (m - 1)
        if pos < 0:
            pos = 0
        x = sorted_a[pos]
        results.append(str(x))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()