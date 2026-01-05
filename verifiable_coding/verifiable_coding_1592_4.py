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
            A = list(map(int, data[idx+1:idx+1+C_i]))
            rows.append(A)
            idx += 1 + C_i
        total = 0
        left = 0
        right = 0
        for row in rows:
            if len(row) == 0:
                continue
            if len(row) % 2 == 1:
                total += row[0]
                left += 1
            else:
                total += row[0]
                right += 1
        results.append(total)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()