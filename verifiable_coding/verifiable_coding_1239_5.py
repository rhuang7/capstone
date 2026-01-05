import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    for i in range(1, T + 1):
        K = int(input[i])
        for j in range(K, 0, -1):
            print(str(j) * j)
        for j in range(K - 1, 0, -1):
            print(str(j) * j)

if __name__ == '__main__':
    solve()