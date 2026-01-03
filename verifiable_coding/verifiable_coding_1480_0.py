import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx+1])
        idx += 2
        cabs = []
        for _ in range(N):
            x = int(data[idx])
            y = int(data[idx+1])
            cabs.append((x, y))
            idx += 2
        M_val = int(data[idx])
        idx += 1
        customers = []
        for _ in range(M_val):
            sx = int(data[idx])
            sy = int(data[idx+1])
            dx = int(data[idx+2])
            dy = int(data[idx+3])
            customers.append((sx, sy, dx, dy))
            idx += 4
        for cust in customers:
            min_dist = float('inf')
            min_cab = -1
            for i in range(N):
                x, y = cabs[i]
                dx = x - cust[0]
                dy = y - cust[1]
                dist = dx*dx + dy*dy
                if dist < min_dist or (dist == min_dist and i+1 < min_cab):
                    min_dist = dist
                    min_cab = i+1
            print(min_cab)

if __name__ == '__main__':
    solve()