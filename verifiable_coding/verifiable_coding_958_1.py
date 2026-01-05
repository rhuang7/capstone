import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    for i in range(1, T + 1):
        K = int(data[i])
        for row in range(K):
            if row == 0 or row == K - 1:
                print('*' * K)
            else:
                print('*' + ' ' * (2 * (row - 1)) + '*')
        if i < T:
            print()