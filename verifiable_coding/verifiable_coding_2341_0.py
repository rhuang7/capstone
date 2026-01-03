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
        
        # Preprocess: sort the array to find the x-th smallest element
        sorted_a = sorted(a)
        x = sorted_a[n - m]
        results.append(str(x))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()