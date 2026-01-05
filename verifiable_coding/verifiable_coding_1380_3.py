import sys

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        N = int(data[i])
        results.append(str(N * (N - 1) // 2))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()