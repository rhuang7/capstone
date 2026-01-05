import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    K = int(data[1])
    h = list(map(int, data[2:2+N]))
    h.sort()
    min_diff = float('inf')
    for i in range(N - K + 1):
        min_diff = min(min_diff, h[i + K - 1] - h[i])
    print(min_diff)

if __name__ == '__main__':
    solve()