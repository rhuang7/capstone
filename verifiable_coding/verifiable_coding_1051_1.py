import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    for i in range(1, T + 1):
        K = int(input[i])
        print("0")
        for j in range(1, K + 1):
            print("*" * j + str(j))

if __name__ == '__main__':
    solve()