import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    n = int(data[0])
    R = int(data[1])
    H = list(map(int, data[2:2+n]))
    
    H.sort()
    
    min_dist = float('inf')
    for h in H:
        dist = abs(h - R)
        if dist < min_dist:
            min_dist = dist
    
    print(min_dist)

if __name__ == '__main__':
    solve()