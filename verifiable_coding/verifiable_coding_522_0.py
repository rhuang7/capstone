import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    N = int(input().split()[0])
    
    count = 0
    for x in range(1, N):
        for y in range(1, N):
            z = N - y * x
            if z >= 1 and z <= N:
                count += 1
    print(count)

if __name__ == '__main__':
    solve()