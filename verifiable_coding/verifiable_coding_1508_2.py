import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    for i in range(1, T + 1):
        K = int(input[i])
        for j in range(K):
            if j % 2 == 0:
                print(''.join(str(x) for x in range(j, -1, -1)), end='')
            else:
                print(''.join(str(x) for x in range(j, -1, -1)), end='')
        print()

if __name__ == '__main__':
    solve()