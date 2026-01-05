import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    R = int(data[1])
    H = list(map(int, data[2:2 + n]))
    
    H.sort()
    
    max_x = 0
    for i in range(n):
        if i == 0:
            diff = abs(H[i] - R)
        else:
            diff = abs(H[i] - H[i-1])
        max_x = min(max_x, diff)
    
    print(max_x)

if __name__ == '__main__':
    solve()