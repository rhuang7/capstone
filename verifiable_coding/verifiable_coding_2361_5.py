import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    results = []
    
    idx = 1
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        a = [0] * n
        for i in range(1, n + 1):
            l = 0
            r = n - 1
            while l <= r:
                mid = (l + r) // 2
                if a[mid] == 0:
                    break
                else:
                    if a[mid] % 2 == 1:
                        l = mid + 1
                    else:
                        r = mid - 1
            if (r - l + 1) % 2 == 1:
                pos = (l + r) // 2
            else:
                pos = (l + r - 1) // 2
            a[pos] = i
        
        results.append(' '.join(map(str, a)))
    
    print('\n'.join(results))