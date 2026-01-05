import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    count = 0
    idx = 2
    for _ in range(n):
        ti = int(data[idx])
        idx += 1
        if ti % k == 0:
            count += 1
    print(count)

if __name__ == '__main__':
    solve()