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
            if current_gas >= i:
                current_gas -= i
                total_distance += i
            else:
                break
        results.append(total_distance)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()