import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    R = int(data[1])
    H = list(map(int, data[2:2+n]))
    
    H.sort()
    
    max_x = 0
    for i in range(n):
        diff = abs(H[i] - R)
        if diff % 2 == 1:
            return 0
        max_x = max(max_x, diff // 2)
    
    return max_x

if __name__ == '__main__':
    print(solve())