import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    for i in range(1, T + 1):
        N = int(input[i])
        series = [str(x) for x in range(1, N + 1)] + [str(x) for x in range(N - 1, 0, -1)]
        print(' '.join(series))
        sum_cubes = sum(x**3 for x in range(1, N + 1) + range(N - 1, 0, -1))
        print(sum_cubes)

if __name__ == '__main__':
    solve()