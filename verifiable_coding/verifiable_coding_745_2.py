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
        h = list(map(int, data[idx:idx+n]))
        idx += n
        
        min_ops = float('inf')
        
        for i in range(n):
            for j in range(i, n):
                length = j - i + 1
                if length % 2 == 0:
                    continue
                x = (length - 1) // 2
                expected = [k for k in range(1, x+1)] + [x] + [k for k in range(x-1, 0, -1)]
                ops = 0
                for k in range(len(expected)):
                    if h[i + k] < expected[k]:
                        ops += (expected[k] - h[i + k])
                min_ops = min(min_ops, ops)
        
        results.append(str(min_ops))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()