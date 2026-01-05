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
        
        # Initialize the maximum values for each color
        max_r = r[0]
        max_g = g[0]
        max_b = b[0]
        
        # Perform M operations, always choosing the color with the highest current maximum
        for _ in range(M):
            if max_r >= max_g and max_r >= max_b:
                # Apply operation to red
                max_r = r[0] // 2
                r[0] = r[0] // 2
                # Update max_r if needed
                if r[0] > max_r:
                    max_r = r[0]
            elif max_g >= max_r and max_g >= max_b:
                # Apply operation to green
                max_g = g[0] // 2
                g[0] = g[0] // 2
                # Update max_g if needed
                if g[0] > max_g:
                    max_g = g[0]
            else:
                # Apply operation to blue
                max_b = b[0] // 2
                b[0] = b[0] // 2
                # Update max_b if needed
                if b[0] > max_b:
                    max_b = b[0]
        
        # The answer is the maximum of the three current maximums
        results.append(max(max_r, max_g, max_b))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()