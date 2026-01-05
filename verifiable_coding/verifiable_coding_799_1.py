import sys

def solve():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    count = 0
    idx = 1
    for _ in range(n):
        a = data[idx]
        b = data[idx+1]
        c = data[idx+2]
        idx += 3
        if a == b == 1 or a == c == 1 or b == c == 1:
            count += 1
    print(count)

if __name__ == '__main__':
    solve()