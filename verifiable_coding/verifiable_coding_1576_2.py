import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    for i in range(1, T + 1):
        K = int(input[i])
        for j in range(K):
            row = ''
            for k in range(K):
                row += str((k + j) % K + 1)
            print(row)

if __name__ == '__main__':
    solve()