import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    for i in range(1, T + 1):
        N = input[i]
        print(''.join(sorted(N, reverse=True)))

if __name__ == '__main__':
    solve()