import sys

def solve():
    import bisect
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N = int(input[idx])
        idx += 1
        speeds = list(map(int, input[idx:idx+N+1]))
        idx += N+1
        S0 = speeds[0]
        count = 0
        for i in range(1, N+1):
            if speeds[i] > S0:
                count += 1
        print(count)

if __name__ == '__main__':
    solve()