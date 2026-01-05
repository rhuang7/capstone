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

        cnt0 = s.count('0')
        cnt1 = n - cnt0

        if cnt0 % 2 != 0 or cnt1 % 2 != 0:
            print(-1)
            continue

        print(0)

if __name__ == '__main__':
    solve()