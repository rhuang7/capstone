import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    for i in range(1, T + 1):
        K = int(data[i])
        for j in range(K):
            row = ''
            for k in range(K):
                row += str((k + j) % K + 1)
            print(row)

if __name__ == '__main__':
    solve()