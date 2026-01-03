import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        k = int(data[idx])
        idx += 1
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        total = sum(a)
        if total >= k:
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    solve()