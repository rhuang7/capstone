import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    c = int(data[idx])
    idx += 1

    heaps = [c] * n

    def add(u, v, k):
        for i in range(u-1, v):
            heaps[i] += k

    def query(p):
        return heaps[p-1]

    for _ in range(m):
        op = data[idx]
        idx += 1
        if op == 'S':
            u = int(data[idx])
            idx += 1
            v = int(data[idx])
            idx += 1
            k = int(data[idx])
            idx += 1
            add(u, v, k)
        else:
            p = int(data[idx])
            idx += 1
            print(query(p))