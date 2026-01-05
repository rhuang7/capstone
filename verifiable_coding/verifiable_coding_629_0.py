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
        idx += 4
        
        r = list(map(int, data[idx:idx+R]))
        idx += R
        g = list(map(int, data[idx:idx+G]))
        idx += G
        b = list(map(int, data[idx:idx+B]))
        idx += B
        
        # Sort each color in descending order
        r.sort(reverse=True)
        g.sort(reverse=True)
        b.sort(reverse=True)
        
        # Perform M operations, each time choosing the color with the largest potion
        for _ in range(M):
            max_val = max(r[0], g[0], b[0])
            if r[0] == max_val:
                r[0] //= 2
            elif g[0] == max_val:
                g[0] //= 2
            else:
                b[0] //= 2
        
        # Find the maximum value among all potions
        max_potion = max(max(r), max(g), max(b))
        results.append(str(max_potion))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()