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
            C_i = len(rows[i])
            if C_i % 2 == 1:
                total += rows[i][0]
            if C_i % 2 == 0:
                total += rows[i][-1]
        results.append(total)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()