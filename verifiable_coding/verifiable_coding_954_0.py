import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    for i in range(1, T + 1):
        N = int(input[i])
        series = list(range(1, N + 1)) + list(range(N - 1, 0, -1))
        sum_cubes = sum(x ** 3 for x in series)
        print(sum_cubes)

if __name__ == '__main__':
    solve()