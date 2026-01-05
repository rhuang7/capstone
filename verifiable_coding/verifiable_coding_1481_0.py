import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]

    for s in cases:
        n = len(s)
        if n % 2 != 0:
            print(-1)
            continue

        zero = 0
        one = 0
        for c in s:
            if c == '0':
                zero += 1
            else:
                one += 1

        if zero != one:
            print(-1)
            continue

        print(0)

if __name__ == '__main__':
    solve()