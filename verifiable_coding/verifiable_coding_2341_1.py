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
        
        # The answer is the (n - k - m + 1)-th smallest element in the array
        # Because we can control k people, and we are in position m
        # So we can ensure that we get the (n - k - m + 1)-th smallest element
        # as the minimum guaranteed value
        x = sorted_a[n - k - m]
        results.append(str(x))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()