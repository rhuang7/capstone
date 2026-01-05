import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    for i in range(1, t + 1):
        n = int(data[i])
        if n == 1:
            print(1)
        else:
            if n % 2 == 0:
                print(n // 2)
            else:
                print((n + 1) // 2 - 1)

if __name__ == '__main__':
    solve()