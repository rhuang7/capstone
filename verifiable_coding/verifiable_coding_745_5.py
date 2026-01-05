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
                if length == 1:
                    ops = 0
                elif length % 2 == 0:
                    ops = (length // 2 - 1) * 2
                else:
                    ops = (length // 2) * 2
                # Check if the current segment can form a temple
                valid = True
                for k in range(i, j + 1):
                    if h[k] < (length - abs(k - i)):
                        valid = False
                        break
                if valid:
                    min_ops = min(min_ops, ops)
        
        results.append(str(min_ops))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()