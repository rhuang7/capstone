import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    D = int(data[1])
    L = list(map(int, data[2:2+N]))
    
    L.sort()
    count = 0
    i = 0
    while i < N:
        if i + 1 < N and L[i+1] - L[i] <= D:
            count += 1
            i += 2
        else:
            i += 1
    print(count)

if __name__ == '__main__':
    solve()