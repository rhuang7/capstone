import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    for i in range(1, T + 1):
        K = int(input[i])
        pattern = ""
        for j in range(1, K + 1):
            pattern += str(j)
        for j in range(K - 1, 0, -1):
            pattern += str(j)
        print(pattern)

if __name__ == '__main__':
    solve()