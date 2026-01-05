import sys

def solve():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    idx = 1
    for _ in range(n):
        a = float(data[idx])
        e = int(data[idx+1])
        idx += 2
        result = a * (10 ** e)
        print("{0:.2f}".format(result))

if __name__ == '__main__':
    solve()