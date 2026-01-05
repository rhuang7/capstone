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
        total_distance = 0
        current_gas = f[0]
        for i in range(1, N):
            if current_gas <= 0:
                break
            distance = min(current_gas, i - 1)
            total_distance += distance
            current_gas -= distance
            current_gas += f[i]
        results.append(str(total_distance))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()