import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    for i in range(1, T + 1):
        N = input[i]
        if int(N) % 2 == 0:
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    solve()