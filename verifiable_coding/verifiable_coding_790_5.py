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

    heaps = [0] * (n + 1)
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
            for i in range(u, v + 1):
                heaps[i] += k
        else:
            p = int(data[idx])
            idx += 1
            print(heaps[p])

if __name__ == '__main__':
    solve()