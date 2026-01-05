import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    Q = int(data[idx])
    idx += 1

    row_add = [0] * (N + 1)
    col_add = [0] * (N + 1)

    for _ in range(Q):
        op = data[idx]
        idx += 1
        r = int(data[idx])
        idx += 1
        x = int(data[idx])
        idx += 1
        if op == 'RowAdd':
            row_add[r] += x
        else:
            col_add[r] += x

    max_val = 0
    for i in range(1, N + 1):
        current = row_add[i] + col_add[i]
        if current > max_val:
            max_val = current
    print(max_val)

if __name__ == '__main__':
    solve()