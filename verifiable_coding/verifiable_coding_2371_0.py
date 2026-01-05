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
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        # Check if the array is already good
        def is_good(arr):
            m = len(arr)
            if m == 0:
                return True
            c = []
            b = arr.copy()
            for _ in range(m):
                if not b:
                    return True
                if b[0] <= b[-1]:
                    c.append(b.pop(0))
                else:
                    c.append(b.pop())
            return c == sorted(c)
        
        # Check for the minimal prefix to remove
        min_len = n
        for k in range(n + 1):
            if is_good(a[k:]):
                min_len = k
                break
        
        results.append(str(min_len))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()