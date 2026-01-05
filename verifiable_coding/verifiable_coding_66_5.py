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
        
        # If not, try a different permutation of b
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                # Swap b[i] and b[j]
                b_new = b[:]
                b_new[i], b_new[j] = b_new[j], b_new[i]
                x_new = a
                y_new = b_new
                sums_new = [x_new[k] + y_new[k] for k in range(n)]
                if len(set(sums_new)) == n:
                    results.append(' '.join(map(str, x_new)))
                    results.append(' '.join(map(str, y_new)))
                    break
            else:
                continue
            break
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()