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
        a = list(map(int, data[idx:idx+n]))
        idx += n
        b = list(map(int, data[idx:idx+n]))
        idx += n
        
        a.sort()
        b.sort()
        x = a
        y = b
        
        # Check if the current assignment works
        sums = [x[i] + y[i] for i in range(n)]
        if len(set(sums)) == n:
            results.append(' '.join(map(str, x)))
            results.append(' '.join(map(str, y)))
            continue
        
        # Try a different permutation of b
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                # Swap b[i] and b[j]
                b[i], b[j] = b[j], b[i]
                sums = [x[k] + b[k] for k in range(n)]
                if len(set(sums)) == n:
                    results.append(' '.join(map(str, x)))
                    results.append(' '.join(map(str, b)))
                    b[i], b[j] = b[j], b[i]
                    break
            else:
                continue
            break
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()