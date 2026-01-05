import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]

    for N in cases:
        n = int(N)
        if n == 1:
            print(10)
        else:
            res = 0
            for i in range(1, 11):
                res += i * (10 ** (i - 1))
            res += n - 1
            print(res)

if __name__ == '__main__':
    solve()