import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        f = list(map(int, data[idx:idx+N]))
        idx += N
        gas = f[0]
        distance = 0
        for i in range(1, N):
            if gas <= 0:
                break
            distance += 1
            gas -= 1
            if gas > 0:
                gas += f[i]
        results.append(str(distance))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()