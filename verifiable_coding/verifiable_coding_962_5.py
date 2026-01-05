import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    for i in range(1, T+1):
        K = int(data[i])
        for j in range(1, K+1):
            print(j, end='')
        print()
        for j in range(K-1, 0, -1):
            print(j, end='')
        print()

if __name__ == '__main__':
    solve()