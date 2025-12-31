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
        R = int(data[idx])
        G = int(data[idx+1])
        B = int(data[idx+2])
        M = int(data[idx+3])
        idx +=4
        r = list(map(int, data[idx:idx+R]))
        idx += R
        g = list(map(int, data[idx:idx+G]))
        idx += G
        b = list(map(int, data[idx:idx+B]))
        idx += B
        # Sort each list in descending order
        r.sort(reverse=True)
        g.sort(reverse=True)
        b.sort(reverse=True)
        # Apply M operations
        for _ in range(M):
            # Find the maximum among the three lists
            max_val = max(r[0], g[0], b[0])
            if r[0] == max_val:
                r[0] //= 2
            elif g[0] == max_val:
                g[0] //= 2
            else:
                b[0] //= 2
        # Find the maximum value after all operations
        result = max(max(r), max(g), max(b))
        results.append(str(result))
    print('\n'.join(results))