import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        n = int(data[idx])
        idx += 1
        h = list(map(int, data[idx:idx + n]))
        idx += n
        
        min_ops = float('inf')
        
        for i in range(n):
            for j in range(i, n):
                length = j - i + 1
                if length == 1:
                    ops = 0
                else:
                    x = (length - 1) // 2
                    if length % 2 == 0:
                        x += 1
                    ops = 0
                    for k in range(i, j + 1):
                        if k < i + x:
                            required = k - i + 1
                        else:
                            required = (j - k) + 1
                        ops += max(0, h[k] - required)
                min_ops = min(min_ops, ops)
        
        results.append(str(min_ops))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()