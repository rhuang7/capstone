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
        rows = []
        for _ in range(N):
            C_i = int(data[idx])
            idx += 1
            A = list(map(int, data[idx:idx + C_i]))
            idx += C_i
            rows.append(A)
        total = 0
        left = 0
        right = 0
        for i in range(N):
            if len(rows[i]) == 0:
                continue
            if left < len(rows[i]):
                total += rows[i][left]
                left += 1
            if right < len(rows[i]):
                total -= rows[i][right]
                right += 1
        results.append(str(total))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()